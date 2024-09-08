texto = input("Insira uma palavra ou uma frase: ")

sem_espaco = texto.replace(" ", "").lower()

# validação
palindromo = True

for i in range(len(sem_espaco)):
    if sem_espaco[i] != sem_espaco[(len(sem_espaco) - 1) - i]:
        palindromo = False

if palindromo:
    print(f"{texto.capitalize()} é um palíndromo.")
else:
    print(f"{texto.capitalize()} não é um palíndromo.")
