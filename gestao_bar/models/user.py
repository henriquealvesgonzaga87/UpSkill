from base import TimeStampedModel
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import Relationship
from main import session


# criar tabela de clientes (id_cliente, primeiro_nome, sobrenome, nif)
class Cliente(TimeStampedModel):
    __tablename__ = "clientes"
    
    id_cliente = Column(Integer, primary_key=True, autoincrement=True)
    primeiro_nome = Column(String(200), nullable=False)
    sobrenome = Column(String(200), nullable=False)
    NIF = Column(Integer, nullable=False, unique=True)

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
