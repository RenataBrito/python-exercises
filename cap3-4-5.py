import math

def main():
    # read a number integer and print
    """num = float(input("Type a number: "))
    num_i = int(num)
    print("The number integer read is %s."% num_i)"""

    # read a number real and print
    """num = float(input("Type a number: "))
    print("The number real read is %s."% num)"""

    # peça ao usuario para digitar tres valor inteiros e imprima a soma deles
    """print("Digite 3 valores interos:")
    num1 = float(input())
    num2 = float(input())
    num3 = float(input())
    result = num1+num2+num3
    print("A soma dos valores é %s.\n" % result)"""

    # leia um numero real e imprima o quadrado desse nuemro
    """print("Digite um numero real e calcularemos seu quadrado.")
    num = float(input())
    result = num**2
    print(f'O quadrado do numero {num} é {result}.')"""

    # leia um numero real e imprima a quinta parte desse nuemro
    """print("Digite um numero real e calcularemos a sua quinta parte.")
    num = float(input())
    result = num/5
    print(f'A quinta parte do numero {num} é {result}.')"""

    # leia a temperatura em Celsius e mostre em Fahrenheit
    """print("Digite a temperatura em Celsius e mostraremos em Fahrenheit.")
    num = float(input())
    result = num*(9.0/5.0) + 32
    print(f'A temperatura {num} em Fahrenheit {result}.')"""

    # leia a temperatura em Fahrenheit e mostre em Celsius
    """print("Digite a temperatura em Fahrenheit e mostraremos em Celsius.")
    num = float(input())
    result = 5*(num-32)/9
    print(f'A temperatura {num} em Celsius {result}.')"""

    # leia a temperatura em Kelvin e mostre em Celsius
    """print("Digite a temperatura em Kelvin e mostraremos em Celsius.")
    num = float(input())
    result = num - 273.15
    print(f'A temperatura {num} em Celsius {result}.')"""

    # lê hora e minuto de inicio e duração mostrar quando acaba
    hora = int(input())
    minuto = int(input())
    segundo = int(input())
    duracao =int(input())
    dia = 0

    while duracao > 0:
        while (segundo <= 59) & (duracao >0):
            duracao -= 1
            segundo += 1
        if segundo == 60:
            if minuto <= 59:
                segundo = 0
                minuto += 1
            if minuto == 60:
                minuto = 0
                if hora < 12:
                    hora += 1
                else:
                    dia += 1
                    hora =0
        
    print(f"Vai termina em {dia} dias {hora} horas {minuto} minutos {segundo} segundos.")
        


if __name__ == '__main__':
    main()
    