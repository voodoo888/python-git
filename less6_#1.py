import time


class TrafficLight:
    color = None

    def running(self):
        def choise_color(color, secunds):
            TrafficLight.color = color
            print(TrafficLight.color)
            time.sleep(secunds)

        while True:
            choise_color('red', 7)
            choise_color('yellow', 2)
            choise_color('green', 5)


a = TrafficLight()
a.running()
