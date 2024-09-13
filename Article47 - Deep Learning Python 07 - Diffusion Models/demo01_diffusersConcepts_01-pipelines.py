from diffusers import DDPMPipeline

image_pipe = DDPMPipeline.from_pretrained("google/ddpm-celebahq-256")
image_pipe.to("cpu")

images = image_pipe().images
# Show an example of the generated image from the Hugging Face Hub (DDPM-CelebHQ)
images[0].show()

# Browse what was the building blocks of the pipeline:
image_pipe