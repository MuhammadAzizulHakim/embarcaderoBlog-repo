import os
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'
from diffusers import UNet2DModel

repo_id = "google/ddpm-church-256"
model = UNet2DModel.from_pretrained(repo_id, use_safetensors=False)

model
model.config

model_random = UNet2DModel(**model.config)

model_random.save_pretrained("my_model")

# Add random gaussian sample
import torch

torch.manual_seed(0)

noisy_sample = torch.randn(1, model.config.in_channels, model.config.sample_size, model.config.sample_size)
noisy_sample.shape

# Inference
with torch.no_grad():
    noisy_residual = model(sample=noisy_sample, timestep=2).sample