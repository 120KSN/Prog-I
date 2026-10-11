class OrdemServico:
    def __init__(self, data_entrada, veiculo, data_saida, cliente, desconto):
        self.data_entrada = data_entrada
        self.veiculo = veiculo
        self.data_saida = data_saida
        self.cliente = cliente
        self.desconto = desconto
    
    def __str__(self):
        return f"""
Data de Entrada: {self.data_entrada}
Data de Saida: {self.data_saida}
Veiculo: {self.veiculo}
Cliente: {self.cliente}
Desconto: {self.desconto}"""

class Cliente:
    def __init__(self, pessoa, email):
        self.pessoa = pessoa
        self.email = email

    def __str__(self):
        return f"""
{self.pessoa}
Email: {self.email}"""

class ServicoRealizado:
    def __init__(self, servico, mecanico):
        self.servico = servico
        self.mecanico = mecanico

    def __str__(self):
        return f"""
Serviço: {self.servico}
Mecânico: {self.mecanico}"""

class Veiculo:
    def __init__(self, placa, cor):
        self.placa = placa
        self.cor = cor

    def __str__(self):
        return f"""
Placa: {self.placa}
Cor: {self.cor}"""

class Servico:
    def __init__(self, descricao, valor):
        self.descricao = descricao
        self.valor = valor

    def __str__(self):
        return f"""Serviço:
Descrição: {self.descricao}
Valor: {self.valor}"""

class Mecanico:
    def __init__(self, pessoa):
        self.pessoa = pessoa

    def __str__(self):
        return f"""
Mecânico: {self.pessoa}"""

class Pessoa:
    def __init__(self, nome, telefone, data_nascimento):
        self.nome = nome
        self.telefone = telefone
        self.data_nascimento = data_nascimento

    def __str__(self):
        return f"""
Nome: {self.nome}
Telefone: {self.telefone}
Data de Nascimento: {self.data_nascimento}"""

class VeiculoComPassageiros(Veiculo):
    def __init__(self, placa, cor, lugares):
        self.lugares = lugares
        super().__init__(placa, cor)

    def __str__(self):
        return f"""{super().__str__()}
Lugares: {self.lugares}"""

class Moto(Veiculo):
    def __init__(self, placa, cor):
        super().__init__(placa, cor)

    def __str__(self):
        return super().__str__()

class Carro(VeiculoComPassageiros):
    def __init__(self, placa, cor, lugares, portas):
        self.portas = portas
        super().__init__(placa, cor, lugares)

    def __str__(self):
        return f"""{super().__str__()}
Portas: {self.portas}"""

class Onibus(VeiculoComPassageiros):
    def __init__(self, placa, cor, lugares):
        super().__init__(placa, cor, lugares)

    def __str__(self):
        return super().__str__()

pm1 = Pessoa("Leonardo", "10 837838392", "01/01/2001")
m1 = Mecanico(pm1)
s1 = Servico("Troca de pneu", 10000)
sr1 = ServicoRealizado(s1, pm1)

ca1 = Carro("ABC123", "Azul", 5, 5)
p1 = Pessoa("Itallo", "47 984492734", "10/10/2010")
c1 = Cliente(p1, "a@gmail.com")
os1 = OrdemServico("06/07/2067", ca1, "07/06/2076", c1, 10)

print(pm1)
print(m1)
print(s1)
print(sr1)
print(ca1)
print(p1)
print(c1)
print(os1)