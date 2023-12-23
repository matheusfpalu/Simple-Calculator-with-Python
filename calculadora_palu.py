import cmath
operação = 6
continua = "A"


def soma(x,y):
    "Soma dois números"
    return x+y

def subtração(x,y):
    "Subtrai dois números"
    return x-y

def multiplicação(x,y):
    "Multiplica dois números"
    return x*y

def divisão(x,y):
    "Divide dois números"
    return x/y

def raíz(x):
    "Raíz quadrada de um número"
    return cmath.sqrt(x)

while(operação!=0):
    while(operação<0 or operação>5):
        operação = int(input("Digite a operação que você deseja\n0 - Sair \n1 - Soma\n2 - Subtração\n3 - Multiplicação\n4 - Divisão\n5 - Raíz Quadrada\n\n"))
        
    if operação == 0:
        break
        
    elif operação == 1:
        print("\nOperação escolhida: Soma\n")
        y = complex(input("Digite o primeiro valor que deseja somar\n"))
        w = complex(input("Digite o segundo valor que deseja somar\n"))
        valor = soma(y,w)
        
    elif operação == 2:
        print("\nOperação escolhida: Subtração\n")
        y = complex(input("Digite o primeiro valor\n"))
        w = complex(input("Digite o valor que será subtraido\n"))
        valor = subtração(y,w)
        
    elif operação == 3:
        print("\nOperação escolhida: Multiplicação\n")
        y = complex(input("Digite o primeiro valor da multiplicação\n"))
        w = complex(input("Digite o segundo valor da multiplicação\n"))
        valor = multiplicação(y,w)

    elif operação == 4:
        print("\nOperação escolhida: Divisão\n")
        y = complex(input("Digite o valor do numerador\n"))
        w = complex(input("Digite o valor do denominador\n"))
        valor = divisão(y,w)
            
    elif operação == 5:
        print("\nOperação escolhida: Raíz Quadrada\n")
        y = complex(input("Digite o valor que deseja tirar a raíz quadrada\n"))
        valor = raíz(y)
        
    if valor.imag == 0:
        print("\nO resultado é: %.4f\n" % valor.real)
    else:
        print("\nO resultado é:\n",valor)
        
    continua = input("\nDeseja rodar novamente? (S/N)\n")

    if continua.upper() == "N":
            operação = 0
    
    elif continua.upper() == "S":
            operação = 6
    
    else:
        print("Operação inválida! A calculadora foi finalizada.")
        operação = 0
        
