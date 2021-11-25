n1 = int(input("Informe o primeiro número: "))
n2 = int(input("Informe o primeiro número: "))
soma = n1 + n2
resto = soma / 2

if resto == 0:
    print("O valor {} é par".format(soma))
else:
    print("O valor {} é impar".format(soma))