FROM python:3.10-slim

WORKDIR /app

# install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# copy everything (including your JSON & safetensors)
COPY . .

# serve via the built-in predict() entrypoint
CMD ["python", "predict.py"]
