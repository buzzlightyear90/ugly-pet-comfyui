from cog import BasePredictor, Input, Path
from PIL import Image
import torch
import os
import sys
sys.path.append("/workspace/ComfyUI")  # Path to ComfyUI repo

from execution import load_workflow_from_path_and_inputs

class Predictor(BasePredictor):
    def predict(
        self,
        image: Path = Input(description="Input image of the pet"),
        prompt: str = Input(description="Prompt to apply", default="Change the photo the dog into an ugly sketch of the same dog")
    ) -> Path:
        workflow_path = "workflows/Ugly_LoRa_Comfy_API_Workflow.json"
        
        input_map = {
            "image": str(input_image),
            "text": prompt
        }

        output_path = load_workflow_from_path_and_inputs(workflow_path, input_map)

        images = sorted(glob("/workspace/ComfyUI/output/*.png"), key=os.path.getmtime, reverse=True)
        return Path(images[0])
