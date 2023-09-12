**Команды для миграций**

- alembic revision -m "create user table"
- alembic upgrade head

**Откат миграции**
- alembic downgrade -1

- alembic current
- alembic history

Создание ветки
`alembic revision -m "create main branch" --head=base --branch-label=main` 
после нужно
`alembic upgrade heads`
в ответе будет заготовок ветки `-> ade02fa3140c, create main branch` 
создание миграции в ветке
`alembic revision -m "add col table organization_partnership" --head=ade02@head`

**ВDUMP & RESTORE DB PostgreSQL in to Docker**
> ВDUMP & RESTORE DB PostgreSQL in to Docker
`docker exec -i marketplace_backend_py_db_1 /bin/bash -c "postgres=pg_password pg_dump  --clean --username b2market b2market_marketplace_development" > dump_2021-12-08.sql`

> RESTORE
`docker exec -i marketplace_backend_py_db_1 /bin/bash -c "postgres=pg_password psql --username b2market b2market_marketplace_development" < dump_2021-12-08.sql`

> RESTORE TAR FILE
`docker exec -i marketplace_backend_py-db-1 pg_restore -U b2market -c -v -d LOCAL_market-prod < c:\MyPyProjects\dump-market_production-202301231155.tar`