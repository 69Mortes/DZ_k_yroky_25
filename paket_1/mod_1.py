def kalk():
        summ = lambda a, b: a + b
        vuch = lambda a, b: a - b
        dell = lambda a, b: a / b
        pro = lambda a, b: a * b
        while True:
                a = int(input("ВВедите первое число:\n"))
                b = int(input("Введите второе число:\n"))
                c = input("Введите знак действия (-, +, /, *):\n"
                          "Если желаете закрыть программу введите 0\n")
                if c == "+":
                        print(summ(a, b))
                elif c == "-":
                        print(vuch(a, b))
                elif c == "/":
                        print(dell(a, b))
                elif c == "*":
                        print(pro(a, b))
                elif c == "0":
                        break