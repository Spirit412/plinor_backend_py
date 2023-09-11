from sqlalchemy import inspect


def get_list_relationships(model) -> list[str]:
    inst = inspect(model)
    relationships = [c_attr[0] for c_attr in inst.relationships.items()]
    return relationships


def get_list_attrs_names(model) -> list[str]:
    inst = inspect(model)
    attr_names = [c_attr.key for c_attr in inst.mapper.column_attrs]
    return attr_names