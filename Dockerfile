FROM python

WORKDIR /app

RUN apt-get update && \
    apt-get install -y postgresql libpq-dev chromium-driver && \
    rm -rf /var/lib/apt/lists/*

ENV POSTGRES_USER=postgres \
    POSTGRES_PASSWORD=postgres \
    POSTGRES_DB=parser \
    PGDATA=/var/lib/postgresql/data/pgdata \
    PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PATH="/usr/lib/chromium/:${PATH}"

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

CMD [ "python", "main.py" ]
