from pista_de_corrida import *
import time


v1 = Veiculo("ABC1234", "Vermelho", 1000, 0, 20, "o/o-")
v2 = Veiculo("CBA4321", "Branco", 300, 0, 10, "OPO-")
v3 = Veiculo("LEO130K", "Preto", 100, 0, 15, "ap-a")

p1 = Pista(1000, [v1, v2, v3])

while True:
    for v in p1.veiculos:
        v.andar()
        print(f"{v.placa}: {v.odometro} KM. {v.tanque} L. Desenho: {"." * (round(v.odometro / 10))}{v.desenho}")
        if v.tanque <=0:
            p1.veiculos.remove(v)
    if len(p1.veiculos) == 0:
        break
    time.sleep(1)

    print(p1.veiculos)