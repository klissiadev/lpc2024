from random import randint

lancamentos = []
freq_lados = [0]*6

for _ in range(100):
    lancamentos.append(randint(1, 6))

for lado in lancamentos:
    match lado:
        case 1:
            freq_lados[0] += 1
        case 2:
            freq_lados[1] += 1
        case 3:
            freq_lados[2] += 1
        case 4:
            freq_lados[3] += 1
        case 5:
            freq_lados[4] += 1
        case 6:
            freq_lados[5] += 1

print("Vetor de lançamentos: \n", lancamentos)
print("\nFrequência de lados: ")

for i in range(6):
    print(f"Lado {i + 1} = {freq_lados[i]} vezes.")


