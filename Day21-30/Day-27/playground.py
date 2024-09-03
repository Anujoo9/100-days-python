def add(*args):
    sum = 0
    for n in args:
        sum += n
    return sum

# print(add(12,3,4,5,6))

def calculate(n, **kwargs):
    print(kwargs)
    # for (key,value) in kwargs.items():
    #     print(key)
    # print(kwargs["add"])
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)



calculate(2,add =3, multiply =4)


class Car:

    def __init__(self,**kw) :
        # self.make = kw["make"]
        # self.model = kw["model"]
        self.model = kw.get("model") # get if we don't pass then by default it's NULL, but in above mandatory to pass 
        self.make = kw.get("make")
        self.color = kw.get("color")
        self.seats = kw.get("seats")



my_car = Car(make = "Nissan", model = "GT-R")

print(my_car.model)