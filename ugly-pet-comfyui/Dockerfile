FROM python:3.10-slim

RUN apt-get update && apt-get install -y git wget libgl1-mesa-glx
WORKDIR /app
RUN git clone https://github.com/comfyanonymous/ComfyUI.git .
COPY loras/ ./loras/
COPY workflows/ ./workflows/
COPY requirements.txt .
RUN pip install -r requirements.txt
EXPOSE 8188
CMD [ "python", "main.py", "--listen", "--port", "8188", "--comfyui-api", "--disable-auto-launch" ]