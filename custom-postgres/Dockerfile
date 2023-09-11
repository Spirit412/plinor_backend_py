FROM postgres:16rc1-bookworm

ENV POSTGRES_USER plinor
ENV POSTGRES_PASSWORD plinor
ENV POSTGRES_DB plinor

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
    postgresql-16-first-last-agg \
    && rm -rf /var/lib/apt/lists/*

COPY create-extension.sh /docker-entrypoint-initdb.d/

EXPOSE 5432