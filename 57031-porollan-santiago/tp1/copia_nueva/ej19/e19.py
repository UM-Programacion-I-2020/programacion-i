from vents import Ventas
import json
import re


class DatoVacio(Exception):
    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = None

    def __str__(self):
        if self.message:
            return 'ValorVacio, {0} '.format(self.message)
        else:
            return 'Dato vacío. Ingrese nuevamente'


def inp(x):
    if x == 0:
        return "monto: "
    elif x == 1:
        return "descripcion: "
    elif x == 2:
        return "nombre y apellido: "
    elif x == 3:
        return "numero tarjeta: "
    elif x == 4:
        return "codigo verificacion: "
    elif x == 5:
        return "tipo tarjeta: "


def check_info(info):
    try:
        if not info:
            raise DatoVacio
    except DatoVacio as dv:
        print(dv)
        return False
    else:
        return True


### contar palabras
class Conteo():
    def __init__(self):
        self.words = {}

    def get_words(self):
        texto = """ """
        for line in open("ventas"):
            texto += line + " "
        for word in re.split(" |, |\n", texto):
            if word not in self.words and len(word) > 1:
                self.words[word] = texto.count(word)

    def fix_size(self):
        while len(self.words) > 20:
            min_key = ""
            for word in self.words:
                if not min_key:
                    min_key = word
                elif self.words[word] < self.words[min_key]:
                    min_key = word
            self.words.pop(min_key)

    def show_words(self):
        while self.words:    
            first = ""
            for word in self.words:
                if not first:
                    first = word
                elif word.lower() < first.lower():
                    first = word
            print(first," se repite: ", self.words[first], " veces")
            self.words.pop(first)


### ejercicio
if __name__ == "__main__":
    stop = False
    venta = Ventas()

    # input
    print(" \"stop\" para terminar")
    while not stop:
        info = input(inp(venta.current))
        if check_info(info):
            stop = venta.set_info(info)
        if venta.current == 6:
            venta.write()
            venta = Ventas()
    
    # mostrar datos
    print("Datos guardados:")
    for line in open("ventas", 'r'):
        print(line.rstrip())

    # convertir a json
    data = {}
    for y, line in enumerate(open("ventas", 'r')):
        d_obj = {}
        tarj = {}
        L = line.split()
        for x in range(0, 4):
            tarj[inp(x+2)[:-2]] = L[x]
        for x in range(4, 6):
            d_obj[inp(x-4)[:-2]] = L[x]
        d_obj["tarjeta"] = tarj
        data[y] = d_obj
    with open("ventas.json", "w") as v:
        json.dump(data, v, indent=4)

    # contar palabras
    print("\nPalabras mas repetidas:")
    words = Conteo()
    words.get_words()
    words.fix_size()
    words.show_words()
