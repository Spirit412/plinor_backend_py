FROM postgres:16rc1-bookworm

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
    postgresql-16-first-last-agg \
    && rm -rf /var/lib/apt/lists/*

COPY create-extension.sh /docker-entrypoint-initdb.d/