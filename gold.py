## Гавриленко Артём. РЕ-21. Комментарии кода.

## Функция getgold. Принимает 3 переменные а, b, e для расчёта золотого сечения.
def getgold(a, b, e):
    ## Идут расчёты по формулам:
    ## -------------------------
    Y = 0.618*a + 0.382*b
    Z = 0.382*a + 0.618*b
    A = Y
    B = Z
    ## -------------------------
    ## Переменная, которая обозначает количество попыток неудачных расчётов.
    i = 0
    ## Цикл, который здесь находится на случай неудачной(ых) попытки(ок) расчётов.
    while True:
        ## Условие, если А > B.
        if A > B:
            a = Y
            ## Если изменённая переменная а в разнице b - a < e, то высчитывается и возвращается х.
            if b - a < e:
                x = (a + B)/2
                return x
            else:
                ## Переменная i увеличивается на 1, то-есть произошла неудачная попытка расчёта.
                i += 1
                print(i)
                ## Изменения переменных для дальнейших расчётов.
                ## ---------------------------------------
                Z = Y
                B = A
                Z = 0.382 * a + 0.618 * b
                B = Z
                ## ---------------------------------------
        ## Условие, если A < B.
        else:
            b = Z
            ## Если изменённая переменная а в разнице b - a < e, то высчитывается и возвращается х.
            if b - a < e:
                x = (a + B)/2
                return x
            else:
                ## Переменная i увеличивается на 1, то-есть произошла неудачная попытка расчёта.
                i += 1
                print(i)
                ## Изменения переменных для дальнейших расчётов.
                ## ---------------------------------------
                Z = Y
                B = A
                Y = 0.618 * a + 0.382 * b
                A = Y
                ## ---------------------------------------

## Ввод данных а, b, e в список, благодаря split().
data = input('Введите значения a, b, e(Через пробел): ').split()

## Вывод возвращаемых значений функции getgold, где ввод происходится со списка и перевод со строки во float(Число с плавающей точкой).
print(getgold(float(data[0]), float(data[1]), float(data[2])))
