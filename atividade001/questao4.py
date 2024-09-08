algarismos = [
    "zero", "um", "dois", "três", "quatro",
    "cinco", "seis", "sete", "oito", "nove"
]

casa_de_10 = [
    "dez", "onze", "doze", "treze",
    "quatorze", "quinze", "dezesseis",
    "dezessete", "dezoito", "dezenove"
]

dezenas = [
    "vinte", "trinta", "quarenta", "cinquenta",
    "sessenta", "setenta", "oitenta", "noventa"
]

numero = int(input("Insira um número entre 0 e 99: "))

if numero < 0 or numero > 99:
    print("O número está fora do intervalo.")
elif numero / 10 < 1:
    print(f"O número por extenso é: {algarismos[numero].capitalize()}")
elif numero / 10 < 2:
    last_dig = numero - 10
    print(f"O número por extenso é: {casa_de_10[last_dig].capitalize()}")
else:
    first_dig = (numero // 10) - 2
    last_dig = numero % 10

    if last_dig == 0:
        print(f"O numero por extenso é: {dezenas[first_dig].capitalize()}")
    else:
        print(f"O numero por extenso é: {dezenas[first_dig].capitalize()} e {algarismos[last_dig]}")
