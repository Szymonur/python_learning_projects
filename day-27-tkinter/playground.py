def add(*args: int):
    result = 0
    for n in args:
        result += n
    # result = sum(result)
    return result


print(add(1, 2, 3, 4, 5, 6, 1, 3, 4))


def calculate(n, **kwargs):
    print(kwargs)
    # for key, value in kwargs.items():
    #     print(key, value)
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)


calculate(2, add=3, multiply=5)


class Car:

    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")
        self.color = kw.get("color")


my_car = Car(make="Nissan")
print(my_car.model)
