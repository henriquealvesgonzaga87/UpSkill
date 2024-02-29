from base import TimeStampedModel
from sqlalchemy import Column, Integer, String, ForeignKey, Date, Float, join
from sqlalchemy.orm import Relationship
from main import session
from datetime import datetime


# criar tabela de clientes (id_cliente, primeiro_nome, sobrenome, nif)
class Cliente(TimeStampedModel):
    __tablename__ = "clientes"
    
    id_cliente = Column(Integer, primary_key=True, autoincrement=True)
    primeiro_nome = Column(String(200), nullable=False)
    sobrenome = Column(String(200), nullable=False)
    NIF = Column(Integer, nullable=False, unique=True)

    venda = Relationship("Venda", back_populates="cliente")

    def __repr__(self):
        return f"<Cliente: {self.primeiro_nome} {self.sobrenome} | {self.NIF}>"

    def adicionar(self):
        try:
            nome = input("Primeiro nome: ").capitalize().strip()
            ultimo_nome = input("Sobrenome: ").capitalize().strip()
            NUMERO_FISCAL = int(input("NIF: "))
            cliente = Cliente(
                primeiro_nome=nome,
                sobrenome=ultimo_nome,
                NIF=NUMERO_FISCAL

            )

            session.add(cliente)
            session.commit()
            return cliente

        except Exception:
            print("Algo deu errado")

    def lista_clientes(self):
        print(Cliente.query.all())

    def filtra_por_nome(self):
        nome = input("Informe o nome: ").capitalize().strip()
        print(Cliente.query.filter_by(primeiro_nome=nome).all())

    def filtra_por_sobrenome(self):
        sobrenome = input("Informe o sobrenome: ").capitalize().strip()
        print(Cliente.query.filter_by(sobrenome=sobrenome).all())

    def filtra_por_nif(self):
        nif = int(input("Informe o NIF: "))
        print(Cliente.query.filter_by(NIF=nif).first())

    def atualizar_cliente(self):
        try:
            nif = int(input("Informe o NIF do cliente a ser atualizado: "))
            cliente_a_ser_atualizado = Cliente.query.filter_by(NIF=nif).first()
            if nif == None:
                raise ValueError("NIF não encontrado!")
            nome = input("Primeiro nome: ").capitalize().strip()
            ultimo_nome = input("Sobrenome: ").capitalize().strip()
            cliente_a_ser_atualizado.primeiro_nome = nome
            cliente_a_ser_atualizado.sobrenome = ultimo_nome
            session.commit()
            return cliente_a_ser_atualizado
        except Exception:
            print("Operação não processada por alguma falha de sistema!")

    def deletar_cliente(self):
        try:
            nif = int(input("Informe o NIF do cliente a ser deletado: "))
            if nif == None:
                raise ValueError("NIF não encontrado!")
            cliente_a_ser_deletado = Cliente.query.filter_by(NIF=nif).first()
            session.delete(cliente_a_ser_deletado)
            session.commit()
            return cliente_a_ser_deletado
        except Exception:
            print("Operação não processada por alguma falha de sistema!")


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
        return f"<id: {self.id_marca_produto} | marca: {self.nome_marca}>"

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
    venda = Relationship("Venda", back_populates="produto")

    def __repr__(self):
        return f"<id: {self.id_produto} | produto: {self.nome_produto} | preço compra: {self.preco_acquisicao}>"

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


# criar tabela de registro de vendas (id_cliente, id_produto, preco_venda)
class Venda(TimeStampedModel):
    __tablename__ = "vendas"

    id_venda = Column(Integer, primary_key=True, autoincrement=True)
    id_cliente = Column(Integer, ForeignKey("clientes.id_cliente", ondelete="CASCADE", onupdate="CASCADE"), index=True, nullable=True)
    id_produto = Column(Integer, ForeignKey("produtos.id_produto", ondelete="CASCADE", onupdate="CASCADE"), index=True, nullable=False)
    preco_venda = Column(Float, nullable=False)

    cliente = Relationship("Cliente", back_populates="venda")
    produto = Relationship("Produto", back_populates="venda")

    def __repr__(self):
        return f"""<venda: id: {self.id_venda}; preço venda: {self.preco_venda} | 
produto: id: {self.id_produto}; produto: {self.produto.nome_produto} |>
cliente: id: {self.id_cliente} nome cliente {self.cliente.primeiro_nome} {self.cliente.sobrenome}; NIF {self.cliente.NIF}"""

    def adicionar(self):
        nif_cliente = int(input("Informe o NIF do cliente: "))
        cliente_registro = Cliente.query.filter_by(NIF=nif_cliente).first()
        id_cliente = cliente_registro.id_cliente
        id_produto = int(input("Informe o ID do produto: "))
        preco_venda = float(input("Informe o preço da venda: "))
        try:
            venda = Venda(
                id_cliente=id_cliente,
                id_produto=id_produto,
                preco_venda=preco_venda,
            )
            session.add(venda)
            session.commit()
            return venda
        except Exception:
            return "Não foi possível registrar o produto!"

    def listar_todas_vendas(self):
        print(Venda.query.all())

    def listar_venda_por_cliente(self):
        pesquisa = int(input("Digite o NIF do cliente: "))
        cliente = Cliente.query.filter_by(NIF=pesquisa).first()
        id_cliente = cliente.id_cliente
        filtra_vendas = Venda.query.filter_by(id_cliente=id_cliente).all()
        print(filtra_vendas)

    def listar_venda_por_produto(self):
        pesquisa = int(input("Digite o ID do produto: "))
        produto = Produto.query.filter_by(id_produto=pesquisa).first()
        id_produto = produto.id_produto
        filtra_produto = Venda.query.filter_by(id_produto=id_produto).all()
        print(filtra_produto)

    def atualizar_venda(self):
        pesquisa = int(input("Digite o ID da venda a ser atualizada: "))
        venda = Venda.query.filter_by(id_venda=pesquisa).first()
        novo_preco_venda = float(input("Informe o novo preço de venda: "))
        venda.preco_venda = novo_preco_venda
        session.commit()
        return venda

    def deletar_venda(self):
        pesquisa = int(input("Digite o ID da venda a ser deletada: "))
        venda = Venda.query.filter_by(id_venda=pesquisa).first()
        session.delete(venda)
        session.commit()
        return venda

    def lucro(self):
        lucro_por_venda = self.preco_venda - self.produto.preco_acquisicao
        return lucro_por_venda

