
class Car:

    cars_dict = {}

    def __init__(self, type_car, rent_price):
        self.type_car = type_car
        self.rent_price = rent_price

    @classmethod
    def add_dict(cls, self):
        cls.cars_dict[self.type_car] = self.rent_price

    @classmethod
    def display_fares(cls):
        print('Cost per day')
        print('Hatchback    : $', cls.cars_dict['Hatchback'])
        print('Sedan        : $', cls.cars_dict['Sedan'])
        print('SUV          : $', cls.cars_dict['SUV'])

    @classmethod
    def calculateFare(cls, type_car, num_days):
        return cls.cars_dict[type_car] * num_days

def main():

    Car.add_dict(Car('Hatchback', 30))
    Car.add_dict(Car('Sedan', 50))
    Car.add_dict(Car('SUV', 100))
    car_list = list(Car.cars_dict.keys())

    while True:
        print('1: Show fares')
        print('2: Chose a car')
        print('3: Quit')
        user_choice = int(input())

        if user_choice == 1:
            Car.display_fares()
        elif user_choice == 2:
            type_car = input('Enter the type of car you want: ')
            while type_car not in car_list:
                type_car = input('Enter available car model: ')
            while True:
                num_days = input('Enter number of days: ')
                try: 
                    num_days = int(num_days)
                    break
                except ValueError:
                    print('Error, please type a correct number')
            fare = Car.calculateFare(type_car, num_days)
            print('Total =', fare)
        else:
            quit()

main()
