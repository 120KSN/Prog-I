from sqlalchemy import create_engine, String, ForeignKey, select
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, Session, relationship
from sqlalchemy.exc import OperationalError
from dotenv import load_dotenv
import os

class Base(DeclarativeBase):
    pass

class Cliente(Base):
    __tablename__ = "cliente"
    id_cliente: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    nome: Mapped[str] = mapped_column(String(250))
    data_nascimento: Mapped[str] = mapped_column(String(10))
    telefone: Mapped[str] = mapped_column(String(13))

    pedidos: Mapped[list["Pedido"]] = relationship(back_populates="cliente", cascade="all, delete-orphan")

class Pedido(Base):
    __tablename__ = "pedido"
    id_pedido: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    nome: Mapped[str] = mapped_column(String(100))
    empresa_fabricante: Mapped[str] = mapped_column(String(100))
    cliente_id: Mapped[int] = mapped_column(ForeignKey("cliente.id_cliente"))

    cliente: Mapped["Cliente"] = relationship(back_populates="pedidos")

def salvar_dados(dado, engine):
    with Session(engine) as session:
            session.add(dado)
            session.commit()
            print("Dados adicionados com sucesso!")

def verificar_id(engine, id, tabela):
    with Session(engine) as session:
        dado = session.get(tabela, id)
            
        if dado:
            return dado
        else:
            print(f"O ID {id} não foi encontrado.")
            return None

def escolher_engine():
    while True:
        opcao = input("Qual banco de dados você deseja usar?\n1 - MYSQL 2 - SQLITE\n")

        if opcao == "1":
            # ler o arquivo .env
            load_dotenv()

            # buscando as variáveis de ambiente
            MYSQL_USER = os.getenv("MYSQL_USER")
            MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD") or "" 
            MYSQL_HOST = os.getenv("MYSQL_HOST")
            MYSQL_PORT = int(os.getenv("MYSQL_PORT", 3306))
            MYSQL_DATABASE = os.getenv("MYSQL_DATABASE")

            engine = create_engine(f"mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}:{MYSQL_PORT}/{MYSQL_DATABASE}")

            break
        elif opcao == "2":
            nome_banco = input("Nome do Banco de Dados: ")
            
            engine = create_engine(f"sqlite:///{nome_banco}.db")
            break
        else:
            print("Opção não reconhecida!")
    
    return engine

def escolher_opcao(engine):
    while True:
        print("""
Menu Inicial
    1- Adicionar clientes
    2- Adicionar pedidos
    3- Listar clientes
    4- Listar pedidos
    5- Excluir clientes
    6- Excluir pedidos
    7- Trocar de banco
    0- Fechar programa""")

        opcao = input("O que deseja fazer? ")

        if opcao == "1" or opcao == "2":
            adicionar_dado(opcao, engine)
        elif opcao == "3" or opcao == "4":
            listar_dado(opcao, engine)
        elif opcao == "5" or opcao == "6":
            excluir_dado(opcao, engine)
        elif opcao == "7":
            try:
                engine = escolher_engine()
                Base.metadata.create_all(engine)
            except OperationalError as e:
                print(f"Erro Operacional no Banco de Dados: {e}")
                print("""Recomendações:
            1- Verifique se o banco de dados MYSQL ou SQLITE estão instalados e funcionando em seu computador
            2- Caso tenha selecionado o banco de dados MYSQL, verifique se ele está ligado e se o banco de dados selecionado para uso existi no seu computador (localhost)""")
                break
        elif opcao == "0":
            break
        else:
            print("Opção Inválida")

def adicionar_dado(opcao, engine):
    dado = None

    if opcao == "1":
        nome = input("Nome do Cliente: ")

        while True:
            data_nascimento = input("Data de Nascimento: ")
            if len(data_nascimento) > 10 or len(data_nascimento) < 10 or data_nascimento[2] != "/" or data_nascimento[5] != "/":
                print("A data de nascimento deve está no formato: XX/XX/XXXX")
            else:
                break

        while True:
            telefone = input("Telefone: ")
            if len(telefone) > 13 or len(telefone) < 13 or telefone[2] != " " or telefone[8] != "-":
                print("O número de telefone deve estar no formato: XX XXXXX-XXXX")
            else:
                break

        dado = Cliente(nome=nome, data_nascimento=data_nascimento, telefone=telefone)
    elif opcao == "2":
        nome = input("Nome do Pedido: ")
        empresa = input("Empresa Fabricante: ")

        while True:
            op = input("""Como deseja seguir para informar o Cliente que fez o pedido? 
    1 - Informar id do Cliente
    2- Procura por nome para encontrar o id

""")
            if op == "1":
                id_cliente = pedir_id("Cliente")
            elif op == "2":
                while True:
                    clientes = procurar_dado(engine, Cliente)

                    if len(clientes) > 0:
                        for cliente in clientes:
                            print(f"Id: {cliente.id_cliente}, Nome: {cliente.nome}, Data Nascimento: {cliente.data_nascimento}, Telefone: {cliente.telefone}")

                        id_cliente = pedir_id("Cliente")
                        break

                    else:
                        print("Nenhum registro encontrado com esse nome! Tente novamente")

            else:
                print("Opção inválida!")
                continue

            if verificar_id(engine, id_cliente, Cliente):
                dado = Pedido(nome=nome, empresa_fabricante=empresa, cliente_id=id_cliente)
                break
            else:
                print("ID do Cliente inválido! Tente novamente")
    else:
        print("Opção Inválida!")

    if dado is not None:
        salvar_dados(dado, engine)
    else:
        print("Nenhum dado cadastrado... \nVoltando ao Menu Inicial")

def listar_dado(opcao, engine):
    if opcao == "3":
        with Session(engine) as session:
            clientes = session.execute(select(Cliente)).scalars().all()

        print("\nLista de CLientes: ")
        for c in clientes:
            print(f"Id: {c.id_cliente}, Nome: {c.nome}, Data Nascimento: {c.data_nascimento}, Telefone: {c.telefone}")

    elif opcao == "4":
        with Session(engine) as session:
            pedidos = session.execute(select(Pedido)).scalars().all()

        print("\nLista de Pedidos: ")
        for p in pedidos:
            print(f"Id: {p.id_pedido}, Nome: {p.nome}, Empresa Fabricante: {p.empresa_fabricante}, ID Cliente: {p.cliente_id}")
    else:
        print("Opção Inválida!")

def excluir_dado(opcao, engine):

    if opcao == "5":
        while True:
            op = input("""Como deseja seguir com a exclusão? 
1 - Informar id para exclusão
2- Procura por nome para encontrar o id

""")
            if op == "1":
                id = pedir_id("Cliente")
                break
            elif op == "2":
                while True:
                    clientes = procurar_dado(engine, Cliente)
                    if len(clientes) > 0:
                        for cliente in clientes:
                            print(f"Id: {cliente.id_cliente}, Nome: {cliente.nome}, Data Nascimento: {cliente.data_nascimento}, Telefone: {cliente.telefone}")

                        id = pedir_id("Cliente")
                        break

                    else:
                        print("Nenhum registro encontrado com esse nome! Tente novamente")

                break

            else:
                print("Opção Inválida!")

        with Session(engine) as session:
            cliente_para_deletar = session.get(Cliente, id)

            if cliente_para_deletar:
                session.delete(cliente_para_deletar)
                session.commit()

                print("Cliente excluído com sucesso!")
                print("Pedidos do Cliente excluídos com sucesso!")
            else:
                print("Cliente não encontrado.")

    elif opcao == "6":
        while True:
            op = input("""Como deseja seguir com a exclusão? 
1 - Informar id para exclusão
2- Procura por nome para encontrar o id
""")
            if op == "1":
                id = pedir_id("Pedido")
                break
            elif op == "2":
                while True:
                    pedidos = procurar_dado(engine, Pedido)
                    if len(pedidos) > 0:
                        for pedido in pedidos:
                            print(f"Id: {pedido.id_pedido}, Nome: {pedido.nome}, Empresa Fabricante: {pedido.empresa_fabricante}, ID Cliente: {pedido.cliente_id}")

                        id = pedir_id("Pedido")
                        break

                    else:
                        print("Nenhum registro encontrado com esse nome! Tente novamente")

                break
            else:
                print("Opção Inválida!")

        with Session(engine) as session:
            pedido_para_deletar = session.get(Pedido, id)
        
            if pedido_para_deletar:
                session.delete(pedido_para_deletar)
                session.commit()
        
                print("Pedido excluído com sucesso!")
            else:
                print("Pedido não encontrado.")
    else:
        print("Opção Inválida!")

def pedir_id(tabela):
    while True:
        try:
            id = int(input(f"Id do {tabela}: "))
            break
        except ValueError:
            print("O ID deve ser um número!")

    return id


def procurar_dado(engine, tabela):
    with Session(engine) as session:
        # Código pego do exemplo do professor (localizando_pessoa.py)
        n = input("Qual nome deseja buscar?")
        # vamos especificar praticamente um SQL SELECT com WHERE, 
        # usando a sintaxe do SQLAlchemy
        sql = select(tabela).where(tabela.nome.like(f"%{n}%"))
        # executar a consulta e obter os resultados
        dados = session.scalars(sql).all()

    return dados

def main():
    try:
        engine = escolher_engine()
        Base.metadata.create_all(engine)
        escolher_opcao(engine)
    except OperationalError as e:
        print(f"Erro Operacional no Banco de Dados: {e}")
        print("""Recomendações:
    1- Verifique se o banco de dados MYSQL ou SQLITE estão instalados e funcionando em seu computador
    2- Caso tenha selecionado o banco de dados MYSQL, verifique se ele está ligado, se o banco de dados selecionado para uso existi no seu computador (localhost)""")

    print("Programa encerrado!")

if __name__ == "__main__":
    main()