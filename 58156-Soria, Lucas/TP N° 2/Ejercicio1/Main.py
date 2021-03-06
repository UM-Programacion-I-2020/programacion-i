#!/usr/bin/python
from Billete import (Billete_de_100, Billete_de_200, Billete_de_500,
                     Billete_de_1000)
from Cajero_automatico import Cajero_automatico


def main():
    caj = Cajero_automatico()
    cien_pesos = Billete_de_100("pesos", "$")
    dos_pesos = Billete_de_200("pesos", "$")
    quin_pesos = Billete_de_500("pesos", "$")
    mil_pesos = Billete_de_1000("pesos", "$")
    caj.agregar_dinero([mil_pesos, mil_pesos, mil_pesos, quin_pesos, mil_pesos,
                        quin_pesos, dos_pesos, cien_pesos, quin_pesos])
    print(caj.contar_dinero())
    print(caj.extraer_dinero(3500))
    print(caj.extraer_dinero(1800))
    print(caj.extraer_dinero(4800))
    print(caj.extraer_dinero(468))
    print(caj.extraer_dinero(200))
    print(caj.contar_dinero())


if __name__ == "__main__":
    main()
