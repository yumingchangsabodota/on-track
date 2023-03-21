FROM on_track_base_image:latest

WORKDIR /app
COPY main.py main.py
COPY modules modules
COPY lib lib

EXPOSE 8086