def leiaInt():
    #Retorna se uma string é um inteiro ou não
    v = False
    while True:
        num = input("Digite um número:")
        if num.isnumeric() == True:
            print(f"Você digitou o número {num}")
            v = True
        else:
            print('\033[1;31mERRO! Digite um número inteiro válido\033[m')
        if v:
            break


leiaInt()
