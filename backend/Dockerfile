FROM python:3.11

COPY requirements.txt requirements.txt
RUN python -m pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

WORKDIR /app

COPY wsgi.py wsgi.py
COPY app.py app.py
COPY model.py model.py

EXPOSE 8000


ENTRYPOINT [ "gunicorn", "-w", "1", "--bind", "0.0.0.0:8000", "wsgi:app"]

