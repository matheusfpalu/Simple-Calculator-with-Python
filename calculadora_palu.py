import cmath
opera��o = 6
continua = "A"


def soma(x,y):
    "Soma dois n�meros"
    return x+y

def subtra��o(x,y):
    "Subtrai dois n�meros"
    return x-y

def multiplica��o(x,y):
    "Multiplica dois n�meros"
    return x*y

def divis�o(x,y):
    "Divide dois n�meros"
    return x/y

def ra�z(x):
    "Ra�z quadrada de um n�mero"
    return cmath.sqrt(x)

while(opera��o!=0):
    while(opera��o<0 or opera��o>5):
        opera��o = int(input("Digite a opera��o que voc� deseja\n0 - Sair \n1 - Soma\n2 - Subtra��o\n3 - Multiplica��o\n4 - Divis�o\n5 - Ra�z Quadrada\n\n"))
        
    if opera��o == 0:
        break
        
    elif opera��o == 1:
        print("\nOpera��o escolhida: Soma\n")
        y = complex(input("Digite o primeiro valor que deseja somar\n"))
        w = complex(input("Digite o segundo valor que deseja somar\n"))
        valor = soma(y,w)
        
    elif opera��o == 2:
        print("\nOpera��o escolhida: Subtra��o\n")
        y = complex(input("Digite o primeiro valor\n"))
        w = complex(input("Digite o valor que ser� subtraido\n"))
        valor = subtra��o(y,w)
        
    elif opera��o == 3:
        print("\nOpera��o escolhida: Multiplica��o\n")
        y = complex(input("Digite o primeiro valor da multiplica��o\n"))
        w = complex(input("Digite o segundo valor da multiplica��o\n"))
        valor = multiplica��o(y,w)

    elif opera��o == 4:
        print("\nOpera��o escolhida: Divis�o\n")
        y = complex(input("Digite o valor do numerador\n"))
        w = complex(input("Digite o valor do denominador\n"))
        valor = divis�o(y,w)
            
    elif opera��o == 5:
        print("\nOpera��o escolhida: Ra�z Quadrada\n")
        y = complex(input("Digite o valor que deseja tirar a ra�z quadrada\n"))
        valor = ra�z(y)
        
    if valor.imag == 0:
        print("\nO resultado �: %.4f\n" % valor.real)
    else:
        print("\nO resultado �:\n",valor)
        
    continua = input("\nDeseja rodar novamente? (S/N)\n")

    if continua.upper() == "N":
            opera��o = 0
    
    elif continua.upper() == "S":
            opera��o = 6
    
    else:
        print("Opera��o inv�lida! A calculadora foi finalizada.")
        opera��o = 0
        
