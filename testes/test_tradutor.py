import pytest
import tradutor

## Testes da função obtem_extenso

def test_zero():
    assert tradutor.obtem_extenso(0) == "zero"

def test_sinal_negativo():
    assert tradutor.obtem_extenso(-1) == "menos um"

def test_sinal_positivo():
    assert tradutor.obtem_extenso(+1) == "um"

def test_numero_positivo_sem_sinal():
    assert tradutor.obtem_extenso(94587) == "noventa e quatro mil e quinhentos e oitenta e sete"

def test_primeiro_milhar():
    assert tradutor.obtem_extenso(1000) == "mil"

def test_milhar_negativo():
    assert tradutor.obtem_extenso(-1042) == "menos mil e quarenta e dois"

def test_primeiro_milhar_maior_que_mil():
    assert tradutor.obtem_extenso(1001) == "mil e um"

def test_segundo_milhar():
    assert tradutor.obtem_extenso(2042) == "dois mil e quarenta e dois"

def test_unidade():
    assert tradutor.obtem_extenso(5) == "cinco"

def test_dezena():
    assert tradutor.obtem_extenso(23) == "vinte e três"
    assert tradutor.obtem_extenso(20) == "vinte"

def test_centena():
    assert tradutor.obtem_extenso(233) == "duzentos e trinta e três"
    assert tradutor.obtem_extenso(203) == "duzentos e três"

## Testes da função traduz_cento

def test_traducao_cento_zero():
    assert tradutor.traduz_cento(0) == (0, "")

def test_traducao_cento_sinal_positivo():
    assert tradutor.traduz_cento(+1) == (1, "um")

def test_traducao_cento_numero_positivo_sem_sinal():
    assert tradutor.traduz_cento(94587) == (587, "quinhentos e oitenta e sete")

def test_traducao_cento_primeiro_milhar():
    assert tradutor.traduz_cento(1000) == (0, "")

def test_traducao_cento_primeiro_milhar_maior_que_mil():
    assert tradutor.traduz_cento(1001) == (1, "um")

def test_traducao_cento_segundo_milhar():
    assert tradutor.traduz_cento(2042) == (42, "quarenta e dois")

def test_traducao_cento_unidade():
    assert tradutor.traduz_cento(5) == (5, "cinco")

def test_traducao_cento_dezena():
    assert tradutor.traduz_cento(23) == (23, "vinte e três")
    assert tradutor.traduz_cento(20) == (20, "vinte")

def test_traducao_cento_centena():
    assert tradutor.traduz_cento(233) == (233, "duzentos e trinta e três")
    assert tradutor.traduz_cento(203) == (203, "duzentos e três")

def test_dezenas_menores_que_vinte():
    assert tradutor.traduz_cento(11) == (11, "onze")
    assert tradutor.traduz_cento(12) == (12, "doze")
    assert tradutor.traduz_cento(13) == (13, "treze")
    assert tradutor.traduz_cento(14) == (14, "quatorze")
    assert tradutor.traduz_cento(15) == (15, "quinze")
    assert tradutor.traduz_cento(16) == (16, "dezesseis")
    assert tradutor.traduz_cento(17) == (17, "dezessete")
    assert tradutor.traduz_cento(18) == (18, "dezoito")
    assert tradutor.traduz_cento(19) == (19, "dezenove")

def test_centena_menor_que_duzentos():
    assert tradutor.traduz_cento(101) == (101, "cento e um")
    assert tradutor.traduz_cento(111) == (111, "cento e onze")
    assert tradutor.traduz_cento(121) == (121, "cento e vinte e um")


## Testes de validação

def test_milhao():
    assert tradutor.valida_algarismo("1000000") == False

def test_hexadecimal():
    assert tradutor.valida_algarismo("0xFF") == False

def test_sinal_positivo_duplicado():
    assert tradutor.valida_algarismo("++1") == False

def test_sinal_negativo_duplicado():
    assert tradutor.valida_algarismo("--1") == False

def test_sinal_duplicado_pos_neg():
    assert tradutor.valida_algarismo("+-1") == False

def test_sinal_sinal_duplicado_neg_pos():
    assert tradutor.valida_algarismo("-+1") == False

def test_so_sinal_positivo():
    assert tradutor.valida_algarismo("+") == False

def test_so_sinal_negativo():
    assert tradutor.valida_algarismo("-") == False

def test_sinal_neg_lugar_errado():
    assert tradutor.valida_algarismo("-13-") == False

def test_sinal_pos_lugar_errado():
    assert tradutor.valida_algarismo("+13+") == False

def test_caractere_especial_():
    assert tradutor.valida_algarismo("$%#") == False

def test_sinal_caractere_especial_():
    assert tradutor.valida_algarismo("$%#") == False

def test_numero_quebrado():
    assert tradutor.valida_algarismo("0.2") == False

def test_numero_quebrado_maior_que_um():
    assert tradutor.valida_algarismo("1.4") == False

def test_minimo_positivo():
    assert tradutor.valida_algarismo("+1") == True

def test_minimo_negativo():
    assert tradutor.valida_algarismo("-1") == True

def test_zero():
    assert tradutor.valida_algarismo("0") == True
    
def test_maximo_positivo():
    assert tradutor.valida_algarismo("+99999") == True

def test_maximo_negativo():
    assert tradutor.valida_algarismo("-99999") == True

def test_positivo_sem_sinal():
    assert tradutor.valida_algarismo("1933") == True
