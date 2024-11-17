def add(*args):
    print(args[9])
    sum = 0
    for n in args:
        sum += n
    return sum


print(add(3, 5, 6, 8, 9, 9, 9, 9, 9, 9))


def calculate(n, **kwargs):
    print(kwargs)
    # for key, value in kwargs.items():
    #     print(key)
    #     print(kwargs)
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)


calculate(3, add=3, multiply=5)

class Car:
    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")
        self.color = kw.get("colour")
        self.seats = kw.get("seats")

my_car = Car(make="Nissan", model="skyline")
print(my_car.make)