from base import TimeStampedModel
from sqlalchemy import Column, Integer, String, ForeignKey, Date, Float
from sqlalchemy.orm import Relationship
from main import session
from datetime import datetime
from .regex_functions import regex_nome, regex_nif


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
            nome = input("Primeiro nome: ").title().strip()
            verifica_nome = regex_nome(nome)
            while verifica_nome == False:
                print("Nome inválido. Deve conter pelo menos duas letras")
                nome = input("Primeiro nome: ").title().strip()
                verifica_nome = regex_nome(nome)
            ultimo_nome = input("Sobrenome: ").title().strip()
            verifica_sobrenome = regex_nome(ultimo_nome)
            while verifica_sobrenome == False:
                print("Sobrenome inválido. Deve conter pelo menos duas letras")
                ultimo_nome = input("Sobrenome: ").title().strip()
                verifica_nome = regex_nome(ultimo_nome)
            NUMERO_FISCAL = int(input("NIF: "))
            verifica_nif = regex_nif(NUMERO_FISCAL)
            while verifica_nif == False:
                print("NIF Inválido, o NIF deve conter 9 digitos")
                NUMERO_FISCAL = int(input("NIF: "))
                verifica_nif = regex_nif(NUMERO_FISCAL)
            cliente = Cliente(
                primeiro_nome=nome,
                sobrenome=ultimo_nome,
                NIF=NUMERO_FISCAL

            )
            session.add(cliente)
            session.commit()
            return cliente
        except Exception as e:
            print("Algo deu errado")
            print(e)

    def lista_clientes(self):
        print(Cliente.query.all())

    def filtra_por_nome(self):
        try:
            nome = input("Informe o nome: ").title().strip()
            cliente = Cliente.query.filter_by(primeiro_nome=nome).all()
            if len(cliente) != 0:
                print(cliente)
            else:
                print("Cliente não encontrado!")
        except ValueError:
            print("O valor digitado está incorreto")
        except NameError:
            print("O nome digitado não foi encontrado")
        except RuntimeError:
            print("Ocorreu uma falha de sistema, tente novamente!")
        except Exception:
            print("Falha ao encontrar")

    def filtra_por_sobrenome(self):
        try:
            sobrenome = input("Informe o sobrenome: ").title().strip()
            cliente = Cliente.query.filter_by(sobrenome=sobrenome).all()
            if len(cliente) != 0:
                print(cliente)
            else:
                print("Cliente não encontrado!")
        except ValueError:
            print("O valor digitado está incorreto")
        except NameError:
            print("O sobrenome digitado não foi encontrado")
        except RuntimeError:
            print("Ocorreu uma falha de sistema, tente novamente!")
        except Exception:
            print("Falha ao encontrar")

    def filtra_por_nif(self):
        try:
            nif = int(input("Informe o NIF: "))
            cliente = Cliente.query.filter_by(NIF=nif).first()
            if cliente != None:
                print(cliente)
            else:
                print("Cliente não encontrado!")
        except ValueError:
            print("O valor digitado está incorreto")
        except NameError:
            print("O NIF digitado não foi encontrado")
        except RuntimeError:
            print("Ocorreu uma falha de sistema, tente novamente!")
        except Exception:
            print("Falha ao encontrar")

    def atualizar_cliente(self):
        try:
            nif = int(input("Informe o NIF do cliente a ser atualizado: "))
            cliente_a_ser_atualizado = Cliente.query.filter_by(NIF=nif).first()
            if cliente_a_ser_atualizado == None:
                raise ValueError("NIF não encontrado!")
            nome = input("Primeiro nome: ").title().strip()
            verifica_nome = regex_nome(nome)
            while verifica_nome == False:
                print("Nome inválido. Deve conter pelo menos duas letras")
                nome = input("Primeiro nome: ").title().strip()
                verifica_nome = regex_nome(nome)
            ultimo_nome = input("Sobrenome: ").title().strip()
            verifica_sobrenome = regex_nome(ultimo_nome)
            while verifica_sobrenome == False:
                print("Sobrenome inválido. Deve conter pelo menos duas letras")
                ultimo_nome = input("Sobrenome: ").title().strip()
                verifica_nome = regex_nome(ultimo_nome)
            NUMERO_FISCAL = int(input("NIF: "))
            verifica_nif = regex_nif(NUMERO_FISCAL)
            while verifica_nif == False:
                print("NIF Inválido, o NIF deve conter 9 digitos")
                NUMERO_FISCAL = int(input("NIF: "))
                verifica_nif = regex_nif(NUMERO_FISCAL)
            cliente_a_ser_atualizado.primeiro_nome = nome
            cliente_a_ser_atualizado.sobrenome = ultimo_nome
            cliente_a_ser_atualizado.NIF = NUMERO_FISCAL
            session.commit()
            return cliente_a_ser_atualizado
        except ValueError:
            print("O valor digitado está incorreto")
        except NameError:
            print("O nome digitado não foi encontrado")
        except RuntimeError:
            print("Ocorreu uma falha de sistema, tente novamente!")
        except Exception:
            print("Falha ao encontrar")

    def deletar_cliente(self):
        try:
            nif = int(input("Informe o NIF do cliente a ser deletado: "))
            cliente_a_ser_deletado = Cliente.query.filter_by(NIF=nif).first()
            if cliente_a_ser_deletado == None:
                raise ValueError("NIF não encontrado!")
            session.delete(cliente_a_ser_deletado)
            session.commit()
            return cliente_a_ser_deletado
        except ValueError:
            print("O valor digitado está incorreto")
        except NameError:
            print("O nome digitado não foi encontrado")
        except RuntimeError:
            print("Ocorreu uma falha de sistema, tente novamente!")
        except Exception:
            print("Falha ao encontrar")


# tabela tipos_produtos(id_tipo_produto, tipo_produto)
class TipoProduto(TimeStampedModel):
    __tablename__ = "tipos_produto"

    id_tipo_produto = Column(Integer, primary_key=True, autoincrement=True)
    tipo_produto = Column(String(50), nullable=False)

    produto = Relationship("Produto", back_populates="tipo_produto", passive_deletes=True, passive_updates=True)

    def __repr__(self):
        return f"<id: {self.id_tipo_produto} | tipo produto: {self.tipo_produto}>"

    def adicionar(self):
        try:
            tipo_user_input = input("Informe o tipo de produto: ").title().strip()
            verifica_nome = regex_nome(tipo_user_input)
            while verifica_nome == False:
                print("O nome do tipo de produto deve conter pelo menos duas letras")
                tipo_user_input = input("Informe o tipo de produto: ").title().strip()
                verifica_nome = regex_nome(tipo_user_input)
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
            if tipo_produto_atualizar is None:
                raise ValueError("Tipo de produto não encontrado")
            novo_tipo_produto = input("Informe o tipo de produto: ").capitalize().strip()
            verifica_nome = regex_nome(novo_tipo_produto)
            while verifica_nome == False:
                print("O nome do tipo de produto deve conter pelo menos duas letras")
                novo_tipo_produto = input("Informe o tipo de produto: ").capitalize().strip()
                verifica_nome = regex_nome(novo_tipo_produto)
            tipo_produto_atualizar.tipo_produto = novo_tipo_produto
            session.commit()
            return tipo_produto_atualizar
        except ValueError:
            print("O valor digitado está incorreto")
        except NameError:
            print("O nome digitado não foi encontrado")
        except RuntimeError:
            print("Ocorreu uma falha de sistema, tente novamente!")
        except Exception:
            print("Falha ao encontrar")

    def deletar_por_nome(self):
        try:
            pesquisa = input("Digite o tipo de produto a ser deletado: ").capitalize().strip()
            item_a_deletar = TipoProduto.query.filter_by(tipo_produto=pesquisa).first()
            if item_a_deletar is None:
                raise ValueError("Cliente não encontrado")
            session.delete(item_a_deletar)
            session.commit()
        except ValueError:
            print("O valor digitado está incorreto")
        except NameError:
            print("O nome digitado não foi encontrado")
        except RuntimeError:
            print("Ocorreu uma falha de sistema, tente novamente!")
        except Exception:
            print("Falha ao deletar")

    def deletar_por_id(self):
        try:
            pesquisa = int(input("Digite o ID do item a ser deletado: "))
            item_a_deletar = TipoProduto.query.filter_by(id_tipo_produto=pesquisa).first()
            if item_a_deletar == None:
                raise ValueError("Cliente não encontrado")
            session.delete(item_a_deletar)
            session.commit()
        except ValueError:
            print("O valor digitado está incorreto")
        except NameError:
            print("O nome digitado não foi encontrado")
        except RuntimeError:
            print("Ocorreu uma falha de sistema, tente novamente!")
        except Exception:
            print("Falha ao deletar")


# tabela marca_produto(id_marca_produto, nome_marca)
class MarcaProduto(TimeStampedModel):
    __tablename__ = "marcas_produto"

    id_marca_produto = Column(Integer, primary_key=True, autoincrement=True)
    nome_marca = Column(String(100), nullable=False)

    produto = Relationship("Produto", back_populates="marca_produto", passive_deletes=True, passive_updates=True)

    def __repr__(self):
        return f"<id: {self.id_marca_produto} | marca: {self.nome_marca}>"

    def adicionar(self):
        try:
            nome_marca = input("Informe o nome da marca: ").title().strip()
            verifica_nome = regex_nome(nome_marca)
            while verifica_nome == False:
                print("O nome da marca deve conter pelo menos duas letras!")
                nome_marca = input("Informe o nome da marca: ").title().strip()
                verifica_nome = regex_nome(verifica_nome)
            marca = MarcaProduto(
                nome_marca=nome_marca
            )
            session.add(marca)
            session.commit()
            return marca
        except Exception:
            print("Falha ao inserir")

    def listar(self):
        print(MarcaProduto.query.all())

    def atualizar_por_nome(self):
        try:
            pesquisa = input("Informe a marca a ser atualizada: ").title().strip()
            marca_atualizar = MarcaProduto.query.filter_by(nome_marca=pesquisa).first()
            if marca_atualizar is None:
                raise ValueError("Marca não encontrada")
            novo_nome_marca = input("Informe o novo nome da marca: ").title().strip()
            verifica_nome = regex_nome(novo_nome_marca)
            while verifica_nome == False:
                print("O nome da marca deve conter pelo menos duas letras!")
                novo_nome_marca = input("Informe o novo nome da marca: ").title().strip()
                verifica_nome = regex_nome(novo_nome_marca)
            marca_atualizar.nome_marca = novo_nome_marca
            session.commit()
            return marca_atualizar
        except ValueError:
            print("O valor digitado está incorreto")
        except NameError:
            print("O nome digitado não foi encontrado")
        except RuntimeError:
            print("Ocorreu uma falha de sistema, tente novamente!")
        except Exception:
            print("Falha ao atualizar")

    def atualizar_por_id(self):
        try:
            pesquisa = int(input("Informe o ID da marca a ser atualizada: "))
            marca_atualizar = MarcaProduto.query.filter_by(id_marca_produto=pesquisa).first()
            if marca_atualizar == None:
                raise ValueError("Marca não encontrada")
            novo_nome_marca = input("Informe o novo nome da marca: ").title().strip()
            verifica_nome = regex_nome(novo_nome_marca)
            while verifica_nome == False:
                print("O nome da marca deve conter pelo menos duas letras!")
                novo_nome_marca = input("Informe o novo nome da marca: ").title().strip()
                verifica_nome = regex_nome(novo_nome_marca)
            marca_atualizar.nome_marca = novo_nome_marca
            session.commit()
            return marca_atualizar
        except ValueError:
            print("O valor digitado está incorreto")
        except NameError:
            print("O nome digitado não foi encontrado")
        except RuntimeError:
            print("Ocorreu uma falha de sistema, tente novamente!")
        except Exception:
            print("Falha ao atualizar")

    def deletar_por_nome(self):
        try:
            pesquisa = input("Informe a marca a ser deletada: ").title().strip()
            item_a_deletar = MarcaProduto.query.filter_by(nome_marca=pesquisa).first()
            if item_a_deletar is None:
                raise ValueError("Marca não encontrada")
            session.delete(item_a_deletar)
            session.commit()
        except ValueError:
            print("O valor digitado está incorreto")
        except NameError:
            print("O nome digitado não foi encontrado")
        except RuntimeError:
            print("Ocorreu uma falha de sistema, tente novamente!")
        except Exception:
            print("Falha ao deletar")

    def deletar_por_id(self):
        try:
            pesquisa = int(input("Informe o ID da marca a ser atualizada: "))
            item_a_deletar = MarcaProduto.query.filter_by(id_marca_produto=pesquisa).first()
            if item_a_deletar == None:
                raise ValueError("Marca não encontrada")
            session.delete(item_a_deletar)
            session.commit()
        except ValueError:
            print("O valor digitado está incorreto")
        except NameError:
            print("O nome digitado não foi encontrado")
        except RuntimeError:
            print("Ocorreu uma falha de sistema, tente novamente!")
        except Exception:
            print("Falha ao deletar")


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
        return f"<id: {self.id_produto} | produto: {self.nome_produto} | preço compra: ${self.preco_acquisicao:.2f}>"

    def adicionar(self):
        try:
            nome_produto = input("Informe o nome do produto: ").title().strip()
            verifica_nome = regex_nome(nome_produto)
            while verifica_nome == False:
                print("O nome do produto deve conter pelo menos duas letras")
                nome_produto = input("Informe o nome do produto: ").title().strip()
                verifica_nome = regex_nome(nome_produto)
            preco_acquisicao = float(input("Informe o preço de compra: "))
            while preco_acquisicao < 0:
                print("O valor a ser inserido deve ser maior que 0")
                preco_acquisicao = float(input("Informe o preço de compra: "))
            data_acquisicao = input("Informe a data de acquisição(YYYY-mm-dd): ")
            data_acquisicao = datetime.strptime(data_acquisicao, "%Y-%m-%d")
            while data_acquisicao > datetime.now():
                print("a data de acquisição não pode ser posterior a data de hoje")
                data_acquisicao = input("Informe a data de acquisição(YYYY-mm-dd): ")
                data_acquisicao = datetime.strptime(data_acquisicao, "%Y-%m-%d")
            tipo_produto = int(input("Informe o ID do tipo do produto: "))
            while tipo_produto <= 0:
                print("O valor do ID tem sempre um nº positivo. Insira um ID válido")
                tipo_produto = int(input("Informe o ID do tipo do produto: "))
            marca = int(input("Informe o ID da marca do produto: "))
            while marca <= 0:
                print("O valor do ID tem sempre um nº positivo. Insira um ID válido")
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
        try:
            pesquisa = input("Informe o nome do produto a ser pesquisado: ").title().strip()
            produto = Produto.query.filter_by(nome_produto=pesquisa).all()
            if produto is None:
                raise ValueError("Produto não encontrado")
            print(produto)
        except ValueError:
            print("O valor digitado está incorreto")
        except NameError:
            print("O nome digitado não foi encontrado")
        except RuntimeError:
            print("Ocorreu uma falha de sistema, tente novamente!")
        except Exception:
            print("Falha ao pesquisar")

    def consultar_por_id(self):
        try:
            pesquisa = int(input("Informe o ID do produto a ser pesquisado: "))
            produto = Produto.query.filter_by(id_produto=pesquisa).first()
            if produto == None:
                raise ValueError("Produto não encontrado")
            print(produto)
        except ValueError:
            print("O valor digitado está incorreto")
        except NameError:
            print("O nome digitado não foi encontrado")
        except RuntimeError:
            print("Ocorreu uma falha de sistema, tente novamente!")
        except Exception:
            print("Falha ao pesquisar")

    def atualizar(self):
        try:
            pesquisa = int(input("Informe o ID do produto a ser atualizado: "))
            item_a_ser_atualizado = Produto.query.filter_by(id_produto=pesquisa).first()
            if item_a_ser_atualizado == None:
                raise ValueError("Produto não encontrado")
            nome_produto_atualizado = input("Informe o novo nome do produto: ").title().strip()
            verifica_nome = regex_nome(nome_produto_atualizado)
            while verifica_nome == False:
                print("O nome do produto deve conter pelo menos duas letras")
                nome_produto_atualizado = input("Informe o novo nome do produto: ").title().strip()
                verifica_nome = regex_nome(nome_produto_atualizado)
            item_a_ser_atualizado.nome_produto = nome_produto_atualizado
            session.commit()
            return item_a_ser_atualizado
        except ValueError:
            print("O valor digitado está incorreto")
        except NameError:
            print("O nome digitado não foi encontrado")
        except RuntimeError:
            print("Ocorreu uma falha de sistema, tente novamente!")
        except Exception:
            print("Falha ao atualizar")

    def deletar(self):
        try:
            pesquisa = int(input("Informe o ID do produto a ser deletado: "))
            item_a_ser_deletado = Produto.query.filter_by(id_produto=pesquisa).first()
            if item_a_ser_deletado == None:
                raise ValueError("Produto não encontrado")
            session.delete(item_a_ser_deletado)
            session.commit()
            return item_a_ser_deletado
        except ValueError:
            print("O valor digitado está incorreto")
        except NameError:
            print("O nome digitado não foi encontrado")
        except RuntimeError:
            print("Ocorreu uma falha de sistema, tente novamente!")
        except Exception:
            print("Falha ao deletar")


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
        return f"""<venda: id: {self.id_venda}; preço venda: ${self.preco_venda:.2f} | 
produto: id: {self.id_produto}; produto: {self.produto.nome_produto} |
cliente: id: {self.id_cliente} nome cliente {self.cliente.primeiro_nome} {self.cliente.sobrenome}; NIF {self.cliente.NIF}>\n"""

    def adicionar(self):
        nif_cliente = int(input("Informe o NIF do cliente: "))
        cliente_registro = Cliente.query.filter_by(NIF=nif_cliente).first()
        if cliente_registro == None:
            raise ValueError("NIF não encontrado")
        id_cliente = cliente_registro.id_cliente
        id_produto = int(input("Informe o ID do produto: "))
        pesquisa_produto = Produto.query.filter_by(id_produto=id_produto).first()
        if pesquisa_produto == None:
            raise ValueError("Produto não encontrado")
        preco_venda = float(input("Informe o preço da venda: "))
        while preco_venda <= 0:
            print("O nº de ID é sempre positivo. Insira um ID válido")
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
        try:
            pesquisa = int(input("Digite o NIF do cliente: "))
            cliente = Cliente.query.filter_by(NIF=pesquisa).first()
            if cliente == None:
                raise ValueError("Cliente não encontrado")
            id_cliente = cliente.id_cliente
            filtra_vendas = Venda.query.filter_by(id_cliente=id_cliente).all()
            print(filtra_vendas)
        except ValueError:
            print("O valor digitado está incorreto")
        except NameError:
            print("O NIF digitado não foi encontrado")
        except RuntimeError:
            print("Ocorreu uma falha de sistema, tente novamente!")
        except Exception:
            print("Falha ao pesquisar")

    def listar_venda_por_produto(self):
        try:
            pesquisa = int(input("Digite o ID do produto: "))
            produto = Produto.query.filter_by(id_produto=pesquisa).first()
            if produto == None:
                raise ValueError("Produto não encontrado")
            id_produto = produto.id_produto
            filtra_produto = Venda.query.filter_by(id_produto=id_produto).all()
            print(filtra_produto)
        except ValueError:
            print("O valor digitado está incorreto")
        except NameError:
            print("O ID digitado não foi encontrado")
        except RuntimeError:
            print("Ocorreu uma falha de sistema, tente novamente!")
        except Exception:
            print("Falha ao pesquisar")

    def atualizar_venda(self):
        try:
            pesquisa = int(input("Digite o ID da venda a ser atualizada: "))
            venda = Venda.query.filter_by(id_venda=pesquisa).first()
            if venda == None:
                raise ValueError("Venda não encontrada")
            novo_preco_venda = float(input("Informe o novo preço de venda: "))
            while novo_preco_venda <= 0:
                print("O valor deve ser sempre positivo. Insira um valor válido")
                novo_preco_venda = float(input("Informe o novo preço de venda: "))
            venda.preco_venda = novo_preco_venda
            session.commit()
            return venda
        except ValueError:
            print("O valor digitado está incorreto")
        except NameError:
            print("O ID digitado não foi encontrado")
        except RuntimeError:
            print("Ocorreu uma falha de sistema, tente novamente!")
        except Exception:
            print("Falha ao atualizar")

    def deletar_venda(self):
        try:
            pesquisa = int(input("Digite o ID da venda a ser deletada: "))
            venda = Venda.query.filter_by(id_venda=pesquisa).first()
            if venda == None:
                raise ValueError("Venda não encontrada")
            session.delete(venda)
            session.commit()
            return venda
        except ValueError:
            print("O valor digitado está incorreto")
        except NameError:
            print("O ID digitado não foi encontrado")
        except RuntimeError:
            print("Ocorreu uma falha de sistema, tente novamente!")
        except Exception:
            print("Falha ao deletar")

    def lucro(self):
        lucro_por_venda = self.preco_venda - self.produto.preco_acquisicao
        return lucro_por_venda
    
    def recibo(self):
        try:
            venda = int(input("Informe o ID da venda: "))
            pesquisa = Venda.query.filter_by(id_venda=venda).first()
            if pesquisa == None:
                raise ValueError("venda não encontrada")
        except Exception as e:
            print("Não foi possível realizar a operação")
            print(e)
        else:
            print(pesquisa)
