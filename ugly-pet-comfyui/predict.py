from PIL import Image

def predict(image):
    # Placeholder: actual implementation would route to the running ComfyUI API server
    # and feed the uploaded image + fixed prompt into the workflow
    img = Image.open(image).convert("RGB")
    return img