class Veiculo:
    def __init__(self, placa:str, cor:str, tanque: int, odometro: float, rendimento: float, desenho: str):
        self.placa = placa
        self.cor = cor
        self.tanque = tanque
        self.odometro = odometro
        self.rendimento = rendimento
        self.desenho = desenho

    def andar(self):
        self.tanque -= 1
        self.odometro += self.rendimento


class Pista:
    def __init__(self, extensao, veiculos):
        self.extensao = extensao
        self.veiculos = veiculos