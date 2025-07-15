FROM r8.im/cog-base:python3.10

# Install system packages
RUN apt-get update -qq && \
    apt-get install -qqy libgl1-mesa-glx libglib2.0-0 git

# Install Python dependencies
COPY requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt

# Clone ComfyUI and copy in your assets
RUN git clone https://github.com/comfyanonymous/ComfyUI.git /workspace/ComfyUI
COPY workflows /workspace/ComfyUI/workflows
COPY loras /workspace/ComfyUI/loras

# Set working directory
WORKDIR /workspace/ComfyUI
