def calculadora():
    print('#'*20,'BEM VINDO A CALCULADORA EM PYTHON', "#"*20)

    print("Escolha uma operação para iniciar:")
    print('1-Somar', '2-Subtrair','3-Dividir','4-Multiplicar', '5-Sair')

    escolha=input("Opção: ") 
    while escolha not in('1','2','3','4','5'):
        print("Opção invalida")
        escolha=input("Escolha uma opção valida..")
        if escolha=='5':
            break
        
    num1=int(input("Escolha o Primeiro Numero: "))
    num2=int(input("Escolha o Segundo Numero: "))

    try:
        if escolha=='1':
            print('O resultado da soma é:', num1+num2)
        elif escolha=='2':
            print('O resultado da Subtração é:', num1-num2)
        elif escolha=='3':
            print('O resultado da divisão é:', num1%num2)
        elif escolha=='4':
            print('O resultado da multiplicação é:', num1*num2)
    except ZeroDivisionError:
        print("Não é possivel dividir o numero zero")
        
    novamente=input("Deseja realizar novo calculo? 1-Sim, 2- Não ")

    if novamente=='1':
        calculadora()
    else:
        pass
calculadora()
