## Гавриленко Артём. РЕ-21. Комментарии кода.

## Импортирован модуль time для работы со временем.
import time

## Функция f(x), шо возвращает результат функции.
def f(x):
    return x**3 + 15 - 8

## Функция getgold. Принимает 3 переменные а, b, e для расчёта золотого сечения.
def getgold(a, b, e):
    global g
    ## Переменная, которая обозначает количество неудачных попыток расчёта при f(а) * f(х) < 0.
    g = 0
    ## Если f(а) * f(b) < 0, то рачитать х по формуле.
    if f(a) * f(b) < 0:
        x = a + (b - a) * 0.382
        ## Цикл для случая того, что х не равен 0 и модуль b - a не меньше е.
        while True:
            ## Если f(x) = 0, то вывести 0.
            if f(x) == 0:
                return "Золотое сечение:", x
            ## Если f(х) не равен 0, то умножить а на х.
            else:
                if f(a) * f(x) < 0:
                    ## Если f(а) * f(х) таки меньше 0, то изменить b
                    b = a + (b - a) * 0.618
                else:
                    ## Если f(а) * f(х) таки не меньше 0, то изменить а
                    a = a + (b - a) * 0.382
                ## Если модуль b - a меньше е, вывести результат (b+a)/2
                if abs(b - a) < e:
                    return "Золотое сечение:", (b+a)/2
                ## Иначе пойти по следующему кругу.
                else:
                    g += 1
                    print("Сечение", g)
                    x = a + (b - a) * 0.382
    ## Если f(а) * f(b) = 0, то проверить, равно ли f(а) нулю. Если равно, вернуть, а, если нет, вернуть b.
    elif f(a) * f(b) == 0:
        if f(a) == 0:
            return "Золотое сечение:", a
        else:
            return "Золотое сечение:", b
    ## Если f(a) * f(b) > 0, то функция не пересекает ось Ох на этом отрезке.
    else:
        return "Функция y = x^2 при золотом сечении не пересекает ось Ох на отрезке [{};{}]".format(a, b)
        
## Функция del2. Принимает 3 переменные а, b, e для расчёта Деления на 2.
def del2(a, b, e):
    global d
    ## Переменная, которая обозначает количество неудачных попыток расчёта при а * х < 0.
    d = 0
    ## Если f(а) * f(b) < 0, то рачитать х по формуле.
    if f(a) * f(b) < 0:
        x = (a + b)/2
        ## Цикл для случая того, что х не равен 0 и b - a не меньше е.
        while True:
            ## Если f(x) = 0, то вывести 0.
            if f(x) == 0:
                return "Деление на 2:", x
            ## Если х не равен 0, то умножить а на х.
            else:
                if f(a) * f(x) < 0:
                    ## Если f(а) * f(х) таки меньше 0, то изменить b
                    b = x
                else:
                    ## Если f(а) * f(х) таки не меньше 0, то изменить а
                    a = x
                ## Если b - a меньше е, вывести результат (b+a)/2
                if b - a < e:
                    return "Деление на 2:", (b+a)/2
                ## Иначе пойти по следующему кругу.
                else:
                    d += 1
                    print("Деление",d)
                    x = (a + b)/2
    ## Если f(а) * f(b) = 0, то проверить, равно ли а нулю. Если равно, вернуть, а, если нет, вернуть b.
    elif f(a) * f(b) == 0:
        if f(a) == 0:
            return "Деление на 2:", a
        else:
            return "Деление на 2:", b
    ## Если f(a) * f(b) > 0, то функция не пересекает ось Ох на этом отрезке.
    else:
        return "Функция y = x^2 при делении на 2 не пересекает ось Ох на отрезке [{};{}]".format(a, b)

## Ввод данных а, b, e в список, благодаря split().
data = input('Введите значения a, b, e(Через пробел): ').split()
print('\n')

## Переменная для расчёта начала работы метода "Золотого сечения".
start = time.time()
## Вывод возвращаемых значений функций getgold и del2, где ввод происходится со списка и перевод со строки во float(Число с плавающей точкой).
print(getgold(float(data[0]), float(data[1]), float(data[2])))
## Переменная для расчёта времени работы функции (Сколько секунд с начала времени сейчас - секунды с начала времени начала работы метода).
goldt = time.time() - start
print(goldt, 'сек. заняло золотое сечение.\n\n')
## Переменная для расчёта начала работы метода "Деления на 2".
start = time.time()
print(del2(float(data[0]), float(data[1]), float(data[2])))
## Переменная для расчёта времени работы функции (Сколько секунд с начала времени сейчас - секунды с начала времени начала работы метода).
del2t = time.time() - start
print(del2t, 'сек. заняло деление на 2.\n\n')

## Сравнение того, сколько кругов заняли обе функции и вывод результата(  СКОРОСТЬ ВЫПОЛНЕНИЯ??????  ).
if d < g:
    print("Метод \"Деления на 2\" закончил с выполнением задачи на", g - d, "итераций быстрее метода \"Золотого Сечения\".\n\n")
elif d == g:
    print("Метод \"Деления на 2\" равен по скорости методу \"Золотого Сечения\".\n\n")
else:
    print("Метод \"Золотого Сечения\" закончил с выполнением задачи на", d - g, "итераций быстрее метода \"Деления на 2\".\n\n")

## Сравнение того, сколько времени в секундах заняли обе функции и вывод результата(  СКОРОСТЬ ВЫПОЛНЕНИЯ??????  ).
if del2t < goldt:
    print("Метод \"Деления на 2\" на", goldt - del2t, "секунд быстрее метода \"Золотого Сечения\".\n\n")
elif del2t == goldt:
    print("Метод \"Деления на 2\" равен по скорости методу \"Золотого Сечения\".\n\n")
else:
    print("Метод \"Золотого Сечения\" на", del2t - goldt, "секунд быстрее метода \"Деления на 2\".\n\n")

