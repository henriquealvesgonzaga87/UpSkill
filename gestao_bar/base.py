# vou utilizar o sqlalchemy para criar e fazer queries no db

# criar tabela de registro de vendas (id_cliente, id_produto, preco_venda)
from datetime import datetime
from sqlalchemy import Column, DateTime
from sqlalchemy.orm import declarative_base
from main import session

Model = declarative_base()
Model.query = session.query_property()

class TimeStampedModel(Model):
    __abstract__ = True

    created_at = Column(DateTime, default=datetime.utcnow())
    updated_at = Column(DateTime, onupdate=datetime.utcnow())