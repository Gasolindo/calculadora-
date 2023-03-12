
from calculo import *

#neste arquivo eu criei o menu e executo o programa

print('#' * 20)
print('Digite 1 para soma')
print('Digite 2 para subtrair')
print('Digite 3 para multiplcar')
print('Digite 4 para dividir')
print('#' * 20)

while True:
 menu = input('Qual a operação que voce deseja realizar: \n ')

 if menu == '1':
    a = int(input('Informe o primeiro número: '))
    b = int(input('Informe o segundo número: '))
    print('A resposta para a sua opreção é:')
    print(soma(a,b))
    
 elif menu == '2':
    a = int(input('Informe o primeiro número: '))
    b = int(input('Informe o segundo número: '))
    print(subtracao(a,b))
    
 elif menu == '3':
    a = int(input('Informe o primeiro número: '))
    b = int(input('Informe o segundo número: '))
    print(multiplicar(a,b))

 elif menu == '4':
    a = int(input('Informe o primeiro número: '))
    b = int(input('Informe o segundo número: '))
    print(div(a,b))

 stop=str(input("Deseja continuar? S/N \n")).upper()
 if stop == "N":
    print("Finalizado!\n   🐌🤝🐓")
    break