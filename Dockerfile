FROM python:3.10-slim

WORKDIR /app

# Rendszeridő beállítása magyar időzónára (fontos az időzítés miatt!)
RUN apt-get update && apt-get install -y tzdata
ENV TZ=Europe/Budapest

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "main.py"]