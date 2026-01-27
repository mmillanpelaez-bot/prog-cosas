

def suma (a, b):
    return  a+b
adicion = suma

def saudo():
    print('Hey there!')
benvida = saudo

def execute(f, p1, p2):
    return f(p1, p2)

def multiplica(y):
    def producto(x):
        return x * y
    return  producto

if __name__ == '__main__':
    # print(adicion(1,2))
    print(execute(suma,2,2))

    benvida()

    double = multiplica(2)
    print(double)
    print(double(5))