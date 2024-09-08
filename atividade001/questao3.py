cpf = input("Informe o número de cpf, seguindo o formato xxx.xxx.xxx-xx: ")

if len(cpf) < 11 or len(cpf) > 14:
    print("Cpf inválido. Número de dígitos incorreto.")
elif cpf[3] != '.' or cpf[7] != '.' or cpf[11] != '-':
    print("Cpf inválido. Formatação incorreta.")
else:
    digitos = cpf.replace(".", "")
    digitos = digitos.replace("-", "")

    if not digitos.isnumeric():
        print("Cpf inválido. Dígitos inválidos.")
    else:
        dig_verif = 0

        for i in range(9):
            dig_verif += int(digitos[i])*(i + 1)

        if dig_verif % 11 != int(digitos[9]):
            print("Cpf inválido. Dígito verificador incorreto.")
        else:
            dig_verif = 0

            for i in range(10):
                dig_verif += int(digitos[i])*i

            if dig_verif % 11 != int(digitos[10]):
                print("Cpf inválido. Dígito verificador incorreto.")
            else:
                print("Cpf Válido.")
