import datetime


class Day:
    def __init__(self, min_temp: float, max_temp: float, humidity: float, date: datetime):
        self.min_temp = min_temp
        self.max_temp = max_temp
        self.humidity = humidity
        self.date = date

    def __str__(self):
        return (f"{self.date} \nminimum tempeture: {self.min_temp} \nmaximum tempeture: " +
                f"{self.max_temp} \nhumidity: {self.humidity}")
