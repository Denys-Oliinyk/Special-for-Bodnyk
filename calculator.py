while True:
    print ('Вітаю вас в калькуляторі')
    q1 = int (input('Введіть число один 1: '))
    q2 = int (input('Введіть число два 2: '))

    v = int (input('Яку операцію ви хочете виконати? \n 1 Додавання \n 2 Віднімання \n 3 Ділення \n 4 Множення \n'))

    if v == 1:
        r = q1 + q2
        p = 'додавання'
        t = p
    if v == 2:
        r = q1 - q2
        l = 'віднімання'
        t = l
    if v == 3:
        if q2 == 0: 
            print("ділити на 0 неможна")       
        r = float(q1 / q2)
        m = 'ділення'
        t = m
    if v == 4:
        r = q1 * q2
        n = 'множення'
        t = n
    print ('Результат ',t,' = ',r)
