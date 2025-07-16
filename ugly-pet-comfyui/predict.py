import comfyui
from comfyui import Workflow

# load your exported JSON
wf = Workflow.load("my_workflow.json")

# load your LoRA weights
wf.load_lora("my_lora.safetensors")

def predict(prompt: str, negative_prompt: str = "", height: int = 512, width: int = 512):
    # set your nodes’ inputs
    wf.set_input("TextEncode/Prompt", prompt)
    wf.set_input("TextEncode/NegativePrompt", negative_prompt)
    wf.set_input("ImageSize", (width, height))
    # run
    outputs = wf.run()
    # extract image from the node you want:
    image = outputs["SaveImage/output"]
    # return as PNG bytes
    buf = io.BytesIO()
    image.save(buf, format="PNG")
    return buf.getvalue()
