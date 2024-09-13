import os
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'
from diffusers import UNet2DModel
from diffusers import DDPMScheduler

repo_id = "google/ddpm-ema-church-256"
model = UNet2DModel.from_pretrained(repo_id, use_safetensors=False)
scheduler = DDPMScheduler.from_pretrained(repo_id)

scheduler.config

scheduler.save_config("my_scheduler")
new_scheduler = DDPMScheduler.from_pretrained("my_scheduler")

# Add random gaussian sample
import torch

torch.manual_seed(0)

noisy_sample = torch.randn(1, model.config.in_channels, model.config.sample_size, model.config.sample_size)
noisy_sample.shape

# Inference
with torch.no_grad():
    noisy_residual = model(sample=noisy_sample, timestep=2).sample

less_noisy_sample = scheduler.step(model_output=noisy_residual, timestep=2, sample=noisy_sample).prev_sample
less_noisy_sample.shape

# Define the denoising loop
import PIL.Image
import numpy as np

def display_sample(sample, i):
    image_processed = sample.cpu().permute(0, 2, 3, 1)
    image_processed = (image_processed + 1.0) * 127.5
    image_processed = image_processed.numpy().astype(np.uint8)

    image_pil = PIL.Image.fromarray(image_processed[0])
    print(f"Image at step {i}")
    image_pil.show()

# Display the progress, at every 50th step
import tqdm

sample = noisy_sample

for i, t in enumerate(tqdm.tqdm(scheduler.timesteps)):
    # 1. predict noise residual
    with torch.no_grad():
        residual = model(sample, t).sample

    # 2. compute less noisy image and set x_t -> x_t-1
    sample = scheduler.step(residual, t, sample).prev_sample

    # 3. optionally look at image
    if (i + 1) % 50 == 0:
        display_sample(sample, i + 1)
