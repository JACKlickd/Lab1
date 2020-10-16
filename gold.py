## Гавриленко Артём. РЕ-21. Комментарии кода.

## Функция getgold. Принимает 3 переменные а, b, e для расчёта золотого сечения.
def getgold(a, b, e):
    ## Переменная, которая обозначает количество неудачных попыток расчёта при а * х < 0.
    i = 0
    ## Если а * b < 0, то рачитать х по формуле.
    if a * b < 0:
        x = a + (b - a) * 0.382
        ## Цикл для случая того, что х не равен 0 и модуль b - a не меньше е.
        while True:
            ## Если x = 0, то вывести 0.
            if x == 0:
                return "Золотое сечение:", x
            ## Если х не равен 0, то умножить а на х.
            else:
                if a * x < 0:
                    ## Если а * х таки меньше 0, то изменить b
                    b = a + (b - a) * 0.618
                else:
                    ## Если а * х таки не меньше 0, то изменить а
                    a = a + (b - a) * 0.382
                ## Если модуль b - a меньше е, вывести результат (b+a)/2
                if abs(b - a) < e:
                    return "Золотое сечение:", (b+a)/2
                ## Иначе пойти по следующему кругу.
                else:
                    i += 1
                    print("Сечение", i)
                    x = a + (b - a) * 0.382
    ## Если а * b = 0, то проверить, равно ли а нулю. Если равно, вернуть, а, если нет, вернуть b.
    elif a * b == 0:
        if a == 0:
            return "Золотое сечение:", a
        else:
            return "Золотое сечение:", b
    ## Если a * b > 0, то функция не пересекает ось Ох на этом отрезке.
    else:
        return "Функция х = у при золотом сечении не пересекает ось Ох на отрезке [{};{}]".format(a, b)
        
## Функция del2. Принимает 3 переменные а, b, e для расчёта Деления на 2.
def del2(a, b, e):
    ## Переменная, которая обозначает количество неудачных попыток расчёта при а * х < 0.
    i = 0
    ## Если а * b < 0, то рачитать х по формуле.
    if a * b < 0:
        x = (a + b)/2
        ## Цикл для случая того, что х не равен 0 и b - a не меньше е.
        while True:
            ## Если x = 0, то вывести 0.
            if x == 0:
                return "Деление на 2:", x
            ## Если х не равен 0, то умножить а на х.
            else:
                if a * x < 0:
                    ## Если а * х таки меньше 0, то изменить b
                    b = x
                else:
                    ## Если а * х таки не меньше 0, то изменить а
                    a = x
                ## Если b - a меньше е, вывести результат (b+a)/2
                if b - a < e:
                    return "Деление на 2:", (b+a)/2
                ## Иначе пойти по следующему кругу.
                else:
                    i += 1
                    print("Деление",i)
                    x = (a + b)/2
    ## Если а * b = 0, то проверить, равно ли а нулю. Если равно, вернуть, а, если нет, вернуть b.
    elif a * b == 0:
        if a == 0:
            return "Деление на 2:", a
        else:
            return "Деление на 2:", b
    ## Если a * b > 0, то функция не пересекает ось Ох на этом отрезке.
    else:
        return "Функция х = у при делении на 2 не пересекает ось Ох на отрезке [{};{}]".format(a, b)

## Ввод данных а, b, e в список, благодаря split().
data = input('Введите значения a, b, e(Через пробел): ').split()

## Вывод возвращаемых значений функций getgold и del2, где ввод происходится со списка и перевод со строки во float(Число с плавающей точкой).
print(getgold(float(data[0]), float(data[1]), float(data[2])))
print(del2(float(data[0]), float(data[1]), float(data[2])))
