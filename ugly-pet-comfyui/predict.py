from cog import BasePredictor, Input, Path
from PIL import Image
import json, uuid, subprocess, os, glob, time

# Default ComfyUI output directory inside the container.
# Change if you configured a different folder in SaveImage.
OUTPUT_DIR = "output"

class Predictor(BasePredictor):
    def setup(self):
        print("ComfyUI predictor ready 🚀")

    def predict(
        self,
        image: Path = Input(description="Pet photo to be uglified"),
        prompt: str = Input(
            description="Prompt for the model",
            default="Change the photo the dog into an ugly sketch of the same dog",
        ),
    ) -> Path:
        # 1️⃣ Save the uploaded photo to /tmp so the workflow can read it
        input_filename = f"input_{uuid.uuid4().hex}.png"
        input_path = f"/tmp/{input_filename}"
        Image.open(image).convert("RGB").save(input_path)

        # 2️⃣ Load the base workflow and inject image + prompt
        with open("workflows/Ugly_LoRa_Comfy_API_Workflow.json") as f:
            wf = json.load(f)

        wf["142"]["inputs"]["image"] = input_path   # LoadImageOutput node
        wf["6"]["inputs"]["text"]   = prompt        # CLIPTextEncode node

        runtime_path = "/tmp/workflow_runtime.json"
        with open(runtime_path, "w") as f:
            json.dump(wf, f)

        # 3️⃣ Run ComfyUI on the edited workflow
        subprocess.run(
            ["python", "main.py", "--workflow", runtime_path],
            check=True,
        )

        # 4️⃣ Give the FS a moment, then pick the newest PNG ComfyUI saved
        time.sleep(1)  # small buffer for I/O
        pngs = sorted(
            glob.glob(f"{OUTPUT_DIR}/**/*.png", recursive=True),
            key=os.path.getmtime,
            reverse=True,
        )
        if not pngs:
            raise RuntimeError("ComfyUI produced no PNG outputs.")

        newest = pngs[0]
        print("Returning image:", newest)
        return Path(newest)
