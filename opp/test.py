class Car:

    def __init__(self,make,model,year,color):
        self.make = make
        self.model = model
        self.year = year
        self.color = color

    def drive(self):
        print("This "+self.model+" is driving")

    def stop(self):
        print("This "+self.model+" is stopped")


car_1 = Car("Chevy","Corvette",2021,"green")
car_2 = Car("Ford","Ferrari",2022,"red")

print(car_2.make)
print(car_2.model)
print(car_2.year)
print(car_1.color)
print(" ")


car_1.drive()
car_2.stop()