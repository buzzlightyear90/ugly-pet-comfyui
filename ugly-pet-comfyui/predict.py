from cog import BasePredictor, Input, Path
from PIL import Image
import os

class Predictor(BasePredictor):
    def setup(self):
        print("Model setup complete.")

    def predict(self, image: Path = Input(description="Pet photo")) -> Path:
        output_path = "/tmp/output.png"
        img = Image.open(image).convert("RGB")
        img.save(output_path)
        return Path(output_path)