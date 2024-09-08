from random import randint

caminho = input("Informe o diretório do arquivo: ")

with open(caminho, "r") as arquivo:
    palavras = arquivo.readlines()

indice_aleatorio = randint(0, len(palavras) - 1)
palavra_aleatoria = palavras[indice_aleatorio].strip("\n").upper()
palavra_escondida = ["_"]*len(palavra_aleatoria)


def montando_palavra(nova_letra, indice):
    global palavra_escondida
    nova_palavra = ''

    for j in range(len(palavra_escondida)):
        if j == indice:
            nova_palavra += nova_letra + ' '
            palavra_escondida[j] = nova_letra
        else:
            nova_palavra += palavra_escondida[j] + ' '

    return nova_palavra


palavra = montando_palavra("", -1)

print(f"Jogo da Forca!\nDescubra a palavra:\n")
print(f"     {palavra}\nVocê terá 6 tentativas...\n")

erros = 1

while erros < 7:
    letra = input("Digite uma letra: ").upper()

    possui = False

    for i in range(len(palavra_aleatoria)):
        if letra == palavra_aleatoria[i]:
            palavra = montando_palavra(letra, i)
            possui = True

    if possui:
        print(f"A palavra é:   {palavra}\n")
        if palavra.find("_") == -1:
            print("----- Parabéns!! -----")
            break
    elif erros != 6:
        print(f"-> Você errrou pela {erros}° vez. Tente de novo!\n")
        erros += 1
    else:
        print(f"\nVocê perdeu. A palavra era {palavra_aleatoria}.")
        erros += 1
