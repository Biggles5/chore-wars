# SightLine correlator. Proprietary. (c) 2026 Ryan Brown / SightLine.
FROM python:3.11-slim
WORKDIR /srv
COPY correlator/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY schemas /srv/schemas
COPY correlator/app.py /srv/correlator/app.py
ENV SIGHTLINE_MQTT_HOST=mosquitto
EXPOSE 8091
CMD ["uvicorn", "correlator.app:app", "--host", "0.0.0.0", "--port", "8091"]
