#Calculadora Basica para Uso convencional
import os
class Calculadora:

    def __init__(self,a,b):
        self.a = a
        self.b = b

    def soma(self):
        return self.a + self.b
    
    def subtrair(self):
        return(self.a - self.b)
    
    def multiplicar(self):
        return(self.a * self.b)
    
    def dividir(self):
        return(self.a/self.b)
    

#Exemplo de aplicação
print("Olá")
choise = True
while choise == True:
    print("Escolha sua opção")
    print("1 - Somar\n2 - Subtrair\n3 - Multiplicar\n4 - Dividir")
    escolha = int(input(" Escolha:"))
    os.system("cls")
    if escolha == 1:
        print("Soma")
        number1 = int(input("Numero 1:"))
        number2 = int(input("Numero 2:"))
        escolha = Calculadora(number1,number2)
        print(escolha.soma())
    elif escolha == 2:
        print("Subtrair")
        number1 = int(input("Numero 1:"))
        number2 = int(input("Numero 2:"))
        escolha = Calculadora(number1,number2)
        print(escolha.subtrair())
    elif escolha == 3:
        print("Multiplciar")
        number1 = int(input("Numero 1:"))
        number2 = int(input("Numero 2:"))
        escolha = Calculadora(number1,number2)
        print(escolha.multiplicar())
    elif escolha == 4: 
        print("Dividir")
        number1 = int(input("Numero 1:"))
        number2 = int(input("Numero 2:"))
        escolha = Calculadora(number1,number2)
        print(escolha.dividir())
    else:
        print("ERRO")
    continuar = input("Deseja tentar novamente?\nS ou N\n").lower()
    if continuar == "s":
        os.system("cls")
    elif continuar == "n":
        choise = False
    else:
        os.system("cls")
        print("Resposta Invalida")