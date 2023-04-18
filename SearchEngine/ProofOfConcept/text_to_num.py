import re

Small = {
    'uno': 1,
    'dos': 2,
    'tres': 3,
    'cuatro': 4,
    'cinco': 5,
    'seis': 6,
    'siete': 7,
    'ocho': 8,
    'nueve': 9,
    'diez': 10,
    'once': 11,
    'doce': 12,
    'trece': 13,
    'catorce': 14,
    'quince': 15,
    'dieciseis': 16,
    'diecisiete': 17,
    'dieciocho': 18,
    'diecinueve': 19,
    'veinte': 20,
    'veintiuno': 21,
    'veintidos': 22,
    'veintitres': 23,
    'veinticuatro': 24,
    'veinticinco': 25,
    'veintiseis': 26,
    'veintisiete': 27,
    'veintiocho': 28,
    'veintinueve': 29,
    'treinta': 30,
    'cuarenta': 40,
    'cincuenta': 50,
    'sesenta': 60,
    'setenta': 70,
    'ochenta': 80,
    'noventa': 90,
    'cien': 100,
    'ciento': 100,
    'doscientos': 200,
    'trescientos': 300,
    'cuatrocientos': 400,
    'quinientos': 500,
    'seiscientos': 600,
    'setecientos': 700,
    'ochocientos': 800,
    'novecientos': 900
}


Magnitude = {
    'mil':          1000,
    'millon':       1000000,
    'millones':     1000000,
    'billon':       1000000000,
    'billones':     1000000000,
    'trillon':      1000000000000,
    'trillones':    1000000000000,
}

def text2num(s):
    a = re.split(r"[\s-]+", s.lower())
    n = 0
    g = 0
    lista = []
    for w in a:
        if w == 'y':
           continue
        x = Small.get(w, None)
        if x is not None:
            g += x
        else:
            x = Magnitude.get(w, None)
            if x is not None:
                n += g * x
                g = 0
            else:
                if n + g != 0:
                    lista.append(n+g)
                    n = 0
                    g = 0
                # si no encuentra la palabra en el diccionario
                lista.append(w)
                
                # raise NumberException("Unknown number: "+w)
    if n + g != 0:
        lista.append(n+g)
    return " ".join(str(x) for x in lista)

if __name__ == "__main__":
    print(text2num("quiero un carro del año Trescientos ochenta y cinco mil ochocientos setenta y dos"))