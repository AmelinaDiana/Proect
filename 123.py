comand = input("Введите команду: ").lower()

while comand != "выход":
    if comand == "анекдот":
        print ('Работа программиста и шамана имеет много общего — оба бормочут непонятные слова, совершают непонятные действия и не могут объяснить, как оно работает.')
        
    elif comand == "стишок":
        print ('С «прогами» у программиста')
        print ('Безупречно, точно, чисто.')
        print ('Он на то и программист,')
        print('Как талантливый артист.')
        
    elif comand == "калькулятор":
        command = input('Введите знак(+,-,*,/): ')
        while command!="выход":
            if command == "+":
                num1 = int(input('Введите число: '))
                num2 = int(input('Введите второе число: '))
                print(num1+num2)
            elif command == "-":
                num1 = int(input('Введите число: '))
                num2 = int(input('Введите второе число: '))
                print(num1-num2)
            elif command == "*":
                num1 = int(input('Введите число: '))
                num2 = int(input('Введите второе число: '))
                print(num1*num2)
            elif command == "/":
                num1 = int(input('Введите число: '))
                num2 = int(input('Введите второе число: '))
                print(num1/num2)
            command = input('Введите команду: ')
        print("Калькулятор выключен")
            
    
    comand = input("Введите команду: ").lower()
print("Чат-бот закончил.")