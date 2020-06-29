import math
import re

algarismo_para_extenso = {
  0: "zero",
  1: "um",
  2: "dois",
  3: "três",
  4: "quatro",
  5: "cinco",
  6: "seis",
  7: "sete",
  8: "oito",
  9: "nove",
  10: "dez",
  11: "onze",
  12: "doze",
  13: "treze",
  14: "quatorze",
  15: "quinze",
  16: "dezesseis",
  17: "dezessete",
  18: "dezoito",
  19: "dezenove",
  20: "vinte",
  30: "trinta",
  40: "quarenta",
  50: "cinquenta",
  60: "sessenta",
  70: "setenta",
  80: "oitenta",
  90: "noventa",
  100: "cento",
  200: "duzentos",
  300: "trezentos",
  400: "quatrocentos",
  500: "quinhentos",
  600: "seiscentos",
  700: "setecentos",
  800: "oitocentos",
  900: "novecentos"
}


def obtem_extenso(algarismo):

    if algarismo == 0:
        return algarismo_para_extenso[algarismo]

    prefixo = "menos " if algarismo < 0 else ""
    modulo_algarismo = math.fabs(algarismo) # módulo do algarismo

    sufixos = [" mil ", ""]
    extenso = ""

    while modulo_algarismo != 0:
        sufixo = sufixos.pop()
        cento, extenso_parcial = traduz_cento(modulo_algarismo)
        modulo_algarismo = (modulo_algarismo - cento) / 1000

        if cento == 1 and sufixo != "":
            if extenso == "":
                extenso = sufixo.strip()
            else:
                extenso = sufixo.strip() + " e " + extenso
        else:
            if sufixo != "":
                extenso_parcial = extenso_parcial + sufixo
                if extenso == "":
                    extenso = extenso_parcial
                else:
                    extenso = extenso_parcial + "e " + extenso
            else:
                extenso = extenso_parcial + sufixo + extenso

    return (prefixo + extenso).strip()


def traduz_cento(modulo_algarismo):

    unidade = modulo_algarismo % 10
    dezena = (modulo_algarismo % 100) - unidade
    cento = modulo_algarismo % 1000
    centena = cento - dezena - unidade
    extenso = ""

    if centena != 0:
        if cento == 100:
            return cento, "cem"
        else:
            extenso += algarismo_para_extenso[centena]
    if dezena != 0:
        if centena != 0:
            extenso += " e "
        if dezena == 10:
            extenso += algarismo_para_extenso[dezena + unidade]
            return cento, extenso
        else:
            extenso += algarismo_para_extenso[dezena]
    if unidade != 0:
        if dezena != 0 or centena != 0:
            extenso += " e "
        extenso += algarismo_para_extenso[unidade]
    return cento, extenso


def valida_algarismo(algarismo):
    if re.match("^[-+]?[0-9]{1,5}$", algarismo) is None:
        return False
    return True


if __name__ == '__main__':
    print(obtem_extenso(119000))
