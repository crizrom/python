class Car:

    def __init__(self,make,model,year,color, pais):
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        self.pais = pais

    def drive(self):
        print("This "+self.model+" is driving")

    def stop(self):
        print("This "+self.model+" is stopped")


car_1 = Car("Chevy","Corvette",2021,"green", "Pala d'Oro")
car_2 = Car("Ford","Ferrari",2022,"red", "plaza")

print(car_2.make)
print(car_2.model)
print(car_2.year)
print(car_1.color)
setattr(car_1, "make", "Porsche")
print(car_1.make)
print(car_1.pais)
print(car_2.pais)
print(" ")


car_1.drive()
car_2.stop()