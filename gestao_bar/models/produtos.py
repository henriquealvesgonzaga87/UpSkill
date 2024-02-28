from sqlalchemy import Column, Integer, String, ForeignKey, Date, Float
from sqlalchemy.orm import Relationship
from base import TimeStampedModel
from main import session
from datetime import datetime


# tabela tipos_produtos(id_tipo_produto, tipo_produto)
class TipoProduto(TimeStampedModel):
    __tablename__ = "tipos_produto"

    id_tipo_produto = Column(Integer, primary_key=True, autoincrement=True)
    tipo_produto = Column(String, nullable=False)

    produto = Relationship("Produto", back_populates="tipo_produto", passive_deletes=True, passive_updates=True)

    def __repr__(self):
        return f"<id: {self.id_tipo_produto} | tipo produto: {self.tipo_produto}>"

    def adicionar(self):
        try:
            tipo_user_input = input("Informe o tipo de produto: ").capitalize().strip()
            tipo_produto = TipoProduto(
                tipo_produto=tipo_user_input
            )
            session.add(tipo_produto)
            session.commit()
            return tipo_produto
        except Exception:
            print("Alguma falha ocorreu. Impossível gravar")

    def listar_todos_tipos_produtos(self):
        print(TipoProduto.query.all())

    def atualizar_tipo_produto(self):
        try:
            tipo_produto_pesquisa_user = input("Digite o tipo de produto a ser atualizado: ").capitalize().strip()
            tipo_produto_atualizar = TipoProduto.query.filter_by(tipo_produto=tipo_produto_pesquisa_user).first()
            novo_tipo_produto = input("Informe o tipo de produto: ").capitalize().strip()
            tipo_produto_atualizar.tipo_produto = novo_tipo_produto
            session.commit()
            return tipo_produto_atualizar
        except Exception:
            print("Não foi possível atualizar o tipo de produto!")

    def deletar_por_nome(self):
        pesquisa = input("Digite o tipo de produto a ser deletado: ").capitalize().strip()
        item_a_deletar = TipoProduto.query.filter_by(tipo_produto=pesquisa).first()
        session.delete(item_a_deletar)
        session.commit()

    def deletar_por_id(self):
        pesquisa = int(input("Digite o ID do item a ser deletado: "))
        item_a_deletar = TipoProduto.query.filter_by(id_tipo_produto=pesquisa).first()
        session.delete(item_a_deletar)
        session.commit()


# tabela marca_produto(id_marca_produto, nome_marca)
class MarcaProduto(TimeStampedModel):
    __tablename__ = "marcas_produto"

    id_marca_produto = Column(Integer, primary_key=True, autoincrement=True)
    nome_marca = Column(String(100), nullable=False)

    produto = Relationship("Produto", back_populates="marca_produto", passive_deletes=True, passive_updates=True)

    def __repr__(self):
        return f"id: {self.id_marca_produto} | marca: {self.nome_marca}"

    def adicionar(self):
        nome_marca = input("Informe o nome da marca: ").capitalize().strip()
        marca = MarcaProduto(
            nome_marca=nome_marca
        )
        session.add(marca)
        session.commit()
        return marca

    def listar(self):
        print(MarcaProduto.query.all())

    def atualizar_por_nome(self):
        pesquisa = input("Informe a marca a ser atualizada: ").capitalize().strip()
        marca_atualizar = MarcaProduto.query.filter_by(nome_marca=pesquisa).first()
        novo_nome_marca = input("Informe o novo nome da marca: ").capitalize().strip()
        marca_atualizar.nome_marca = novo_nome_marca
        session.commit()
        return marca_atualizar

    def atualizar_por_id(self):
        pesquisa = int(input("Informe o ID da marca a ser atualizada: "))
        marca_atualizar = MarcaProduto.query.filter_by(id_marca_produto=pesquisa).first()
        novo_nome_marca = input("Informe o novo nome da marca: ").capitalize().strip()
        marca_atualizar.nome_marca = novo_nome_marca
        session.commit()
        return marca_atualizar

    def deletar_por_nome(self):
        pesquisa = input("Informe a marca a ser deletada: ").capitalize().strip()
        item_a_deletar = MarcaProduto.query.filter_by(nome_marca=pesquisa).first()
        session.delete(item_a_deletar)
        session.commit()

    def deletar_por_id(self):
        pesquisa = int(input("Informe o ID da marca a ser atualizada: "))
        item_a_deletar = MarcaProduto.query.filter_by(id_marca_produto=pesquisa).first()
        session.delete(item_a_deletar)
        session.commit()


# criar tabela de produtos(id_produto, nome_produto, preço_acquisicao, data_acquisicao, id_tipo_produto, id_marca_produto)
class Produto(TimeStampedModel):
    __tablename__ = "produtos"

    id_produto = Column(Integer, primary_key=True, autoincrement=True)
    nome_produto = Column(String(100), nullable=False)
    preco_acquisicao = Column(Float, nullable=False)
    data_acquisicao = Column(Date, nullable=False)
    id_tipo_produto = Column(
        Integer, ForeignKey("tipos_produto.id_tipo_produto", ondelete="CASCADE", onupdate="CASCADE"), index=True
        )
    id_marca_produto = Column(
        Integer, ForeignKey("marcas_produto.id_marca_produto", ondelete="CASCADE", onupdate="CASCADE"), index=True
    )

    tipo_produto = Relationship("TipoProduto", back_populates="produto")
    marca_produto = Relationship("MarcaProduto", back_populates="produto")

    def __repr__(self):
        return f"id: {self.id_produto} | produto: {self.nome_produto} | preço compra: {self.preco_acquisicao}"

    def adicionar(self):
        try:
            nome_produto = input("Informe o nome do produto: ").capitalize().strip()
            preco_acquisicao = float(input("Informe o preço de compra: "))
            data_acquisicao = input("Informe a data de acquisição(YYYY-mm-dd): ")
            data_acquisicao = datetime.strptime(data_acquisicao, "%Y-%m-%d")
            tipo_produto = int(input("Informe o ID do tipo do produto: "))
            marca = int(input("Informe o ID da marca do produto: "))
            produto = Produto(
                nome_produto=nome_produto,
                preco_acquisicao=preco_acquisicao,
                data_acquisicao=data_acquisicao,
                id_tipo_produto=tipo_produto,
                id_marca_produto=marca
            )
            session.add(produto)
            session.commit()
            return produto
        except Exception:
            print("Não foi possível gravar o produto!")

    def consultar_todos_produtos(self):
        print(Produto.query.all())

    def consultar_por_nome(self):
        pesquisa = input("Informe o nome do produto a ser pesquisado: ").capitalize().strip()
        produto = Produto.query.filter_by(nome_produto=pesquisa).all()
        print(produto)

    def consultar_por_id(self):
        pesquisa = int(input("Informe o ID do produto a ser pesquisado: "))
        produto = Produto.query.filter_by(id_produto=pesquisa).first()
        print(produto)

    def atualizar(self):
        pesquisa = int(input("Informe o ID do produto a ser atualizado: "))
        item_a_ser_atualizado = Produto.query.filter_by(id_produto=pesquisa).first()
        nome_produto_atualizado = input("Informe o novo nome do produto: ").capitalize().strip()
        item_a_ser_atualizado.nome_produto = nome_produto_atualizado
        session.commit()
        return item_a_ser_atualizado

    def deletar(self):
        pesquisa = int(input("Informe o ID do produto a ser deletado: "))
        item_a_ser_deletado = Produto.query.filter_by(id_produto=pesquisa).first()
        session.delete(item_a_ser_deletado)
        session.commit()
        return item_a_ser_deletado
