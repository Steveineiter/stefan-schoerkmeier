FROM nvidia/cuda:12.2.2-base-ubuntu22.04

WORKDIR /app

RUN apt-get update && apt-get install -y python3 python3-pip && \
    apt-get clean && rm -rf /var/lib/apt/lists/*
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
EXPOSE 4242
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "4242"]