from api import schemas, crud
from fastapi import Query


class CommonFiltersRoutsService:

    def __init__(
            self,
            limit: int | None = Query(50, description="Количество"),
            offset: int | None = Query(0, description="Отступ"),
            order_field: str = Query('id', description="Имя поля сортировки"),
            order_by: schemas.OrderBy = Query(schemas.OrderBy.ASC, description="""Сортировка: 
            DESC — по убыванию, ASC (по умолчанию) — по возрастанию""")

    ):
        self.limit = limit
        self.offset = offset
        self.order_by: schemas.OrderBy = order_by
        self.name_field = order_field