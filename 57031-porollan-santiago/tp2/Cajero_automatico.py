import Billete as b


class Cajero_automatico():
    def __init__(self):
        self.almacen_de_billetes = {'100': [], '200': [],
                                    '500': [], '1000': []}
        self.contar_dinero()

    def agregar_dinero(self, billetes):
        for billete in billetes:
            self.almacen_de_billetes[billete.denominacion].append(billete)
        self.contar_dinero()

    def contar_dinero(self):
        self.cantidades = {'100': len(self.almacen_de_billetes['100']),
                           '200': len(self.almacen_de_billetes['200']),
                           '500': len(self.almacen_de_billetes['500']),
                           '1000': len(self.almacen_de_billetes['1000'])}
        self.valores = {'100': self.cantidades['100'] * 100,
                        '200': self.cantidades['200'] * 200,
                        '500': self.cantidades['500'] * 500,
                        '1000': self.cantidades['1000'] * 1000}
        self.valor_total = (self.valores['100'] + self.valores['200'] +
                            self.valores['500'] + self.valores['1000'])

    def extraer_dinero(self, monto):
        if monto % 100 != 0:
            return "Error. El monto es incorrecto"
        if monto > self.valor_total:
            return "Error. Quiero sacar mas dinero de lo que puedo"
        billetes = []
        while monto != 0:
            if monto >= 1000 and self.cantidades['1000'] > 0:
                billetes.append(self.__pop('1000'))
                monto -= 1000
            elif monto >= 500 and self.cantidades['500'] > 0:
                billetes.append(self.__pop('500'))
                monto -= 500
            elif monto >= 200 and self.cantidades['200'] > 0:
                billetes.append(self.__pop('200'))
                monto -= 200
            elif monto >= 100 and self.cantidades['100'] > 0:
                billetes.append(self.__pop('100'))
                monto -= 100
            else:
                self.agregar_dinero(billetes)
                return "Error. No hay una combinacion de billetes que nos permita extraer ese monto"
        return billetes

    def __pop(self, monto):
        self.cantidades[monto] -= 1
        self.valores[monto] -= int(monto)
        self.valor_total -= int(monto)
        return self.almacen_de_billetes[monto].pop(0)

    def extraer_dinero_cambio(self, monto, porcentaje):
        monto_cambio = int(monto * porcentaje / 100)

        # redondear
        if porcentaje > 100 or porcentaje < 0:
            return "D"
        if monto_cambio % 100 != 0:
            monto_cambio += (100 - int(str(monto_cambio)[-2:]))
        monto = monto - monto_cambio

        # extraer
        billetes = []
        agregado = 0
        while monto_cambio != 0:
            if monto_cambio >= 100 and self.cantidades['100'] > 0:
                billetes.append(self.__pop('100'))
                monto_cambio -= 100
            elif monto_cambio >= 200 and self.cantidades['200'] > 0:
                billetes.append(self.__pop('200'))
                monto_cambio -= 200
            elif monto_cambio >= 500 and self.cantidades['500'] > 0:
                billetes.append(self.__pop('500'))
                monto_cambio -= 500
            elif monto_cambio >= 1000 and self.cantidades['1000'] > 0:
                billetes.append(self.__pop('1000'))
                monto_cambio -= 1000
            else:
                monto_cambio += 100
                agregado += 1
            if agregado == 11:
                self.agregar_dinero(billetes)
                return "Error. No hay una combinacion de billetes que nos permita extraer ese monto"
        monto -= agregado * 100
        billetes_ext = self.extraer_dinero(monto)
        if type(billetes_ext) is str:
            self.agregar_dinero(billetes)
            return billetes_ext
        for billete in billetes_ext:
            billetes.append(billete)
        return billetes


if __name__ == '__main__':
    # prueba
    # set up
    c = Cajero_automatico()
    billetes = []
    billetes_de_100 = 1
    billetes_de_200 = 2
    billetes_de_500 = 50
    billetes_de_1000 = 0
    for x in range(billetes_de_100):
        billete = b.Billete_de_100()
        billetes.append(billete)
    for x in range(billetes_de_200):
        billete = b.Billete_de_200()
        billetes.append(billete)
    for x in range(billetes_de_500):
        billete = b.Billete_de_500()
        billetes.append(billete)
    for x in range(billetes_de_1000):
        billete = b.Billete_de_1000()
        billetes.append(billete)
    c.agregar_dinero(billetes)
    print(c.valor_total)

    # extraccion
    billetes_ext = c.extraer_dinero(900)
    for billete in billetes_ext:
        try:
            print(billete.representacion)
        except AttributeError:
            print(billetes_ext)
            break
    print(c.valor_total)
