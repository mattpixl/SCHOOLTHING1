from . import customer, menu, orders, promotion, resource, review
from ..dependencies.database import engine, Base


def index():
    Base.metadata.create_all(bind=engine)