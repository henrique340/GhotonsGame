def line():
    print("-"*72)

def title(text):
    line()
    print(text.center(72))
    line()

def principalTitle(text):
    print('-='*36)
    print(text.center(72))
    print('-='*36)

def separateCode(num):
    hundred = num//100
    num = num - hundred*100
    decimal = num//10
    num = num - decimal*10
    unit = num
    return hundred, decimal, unit
