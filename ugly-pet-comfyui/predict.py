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
        input_image: Path = Input(description="Input image of the pet"),
    ) -> Path:
        # Load workflow
        workflow_path = "workflows/Ugly_LoRa_Comfy_API_Workflow.json"
        input_map = {
            "input_image": str(input_image)
        }

        output_path = load_workflow_from_path_and_inputs(workflow_path, input_map)

        # Find the most recent PNG output
        from glob import glob
        images = sorted(glob("/workspace/ComfyUI/output/*.png"), key=os.path.getmtime, reverse=True)
        return Path(images[0])
