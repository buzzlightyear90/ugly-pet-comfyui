import io
import os
from comfyui import Workflow
from PIL import Image

# Load workflow & LoRA once at startup
wf = Workflow.load("Ugly_LoRa_Comfy_API_Workflow.json")
wf.load_lora("ugly.safetensors")

def predict(input_image: bytes) -> bytes:
    # 1. write the uploaded bytes to disk
    img = Image.open(io.BytesIO(input_image)).convert("RGB")
    tmp_path = "/app/input.png"
    img.save(tmp_path)

    # 2. override the workflow’s Load Image node
    #    (node "142" in your JSON)
    wf.set_node_input("142", "image", tmp_path)

    # 3. run the workflow
    outputs = wf.run()

    # 4. grab the result from the Save Image node ("250")
    #    outputs["250"] is a list of lists; take the first image
    result_image = outputs["250"][0][0]

    # 5. encode back to PNG bytes
    buf = io.BytesIO()
    result_image.save(buf, format="PNG")
    return buf.getvalue()
