class BMW:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def start(self):
        print("Starting the car")

    def stop(self):
        print("Stopping the car")


class ThreeSeries(BMW):  # Inherit class BMW
    def __init__(self, cruisControlEnabled, make, model, year):
        # BMW.__init__(self, make, model, year)  # Invoking parent class constructor
        super().__init__(make, model, year)  # Simpler way of invoking parent class constructor using super()
        self.cruiseControlEnabled = cruisControlEnabled

    def start(self):  # Overriding methods
        print('Starting 3 series using push start')


class FiveSeries(BMW):  # Inherit class BMW
    def __init__(self, parkingAssistEnabled, make, model, year):
        BMW.__init__(self, make, model, year)  # Invoking parent class constructor
        self.parkingAssistEnabled = parkingAssistEnabled

    def start(self):
        super().start()  # Invoking parent class method whithin child class
        print('Starting 5 series using remote start')


threeseries = ThreeSeries(True, "BMW", "3series", "2021")

print(threeseries.cruiseControlEnabled)
print(threeseries.make)
print(threeseries.model)
print(threeseries.year)
print(threeseries.start())
print(threeseries.stop())
