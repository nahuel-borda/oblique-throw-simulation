import argparse
from decimal import Decimal
from numpy import roots
from math import radians, cos, sin
from visuals import display_throw
from projectile_motion import calculate_velocity, g

#SIMULATION_DURATION = 1

class TiroOblicuoSimulation():
    def __init__(self, height:int, speed:float, angle:int) -> None:
        self.height = height
        self.speed = speed
        self.angle = radians(angle)
        self.flight_time = self._flight_time()

    def _shift(self, t:int) -> tuple:
        return (
            self.speed * cos(self.angle) * t, # x(t)
            self.speed * sin(self.angle) * t - g/2 * t**2 + self.height  # y(t) 
        )

    def _speed(self, t:int) -> tuple:
        return calculate_velocity(t, self.speed, self.angle)
    
    def _max_reach(self):
        t1 = max(roots([-1*g*1/2, self.speed * sin(self.angle), self.height]))
        return self._shift(t1)

    def _flight_time(self):
        return max(roots([-1*g*1/2, self.speed * sin(self.angle), self.height]))

    def _max_height(self):
        t2 = max(roots([-1*g, self.speed * sin(self.angle)]))
        return self._shift(t2)

    def display(self):
        display_throw(
            self.height, 
            self.speed, 
            self.angle,
            self._max_reach(),
            self._flight_time(),
            self._max_height()
        )


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Get shift and/or speed data of an oblique shot simulation.')
    parser.add_argument('start_height', type=int, help='A starting height for the object.')
    parser.add_argument('shot_speed', type=float, help='A speed given in a numeric value, for the object to be shot at.')
    parser.add_argument('shot_angle', type=int, help='An angle given in degrees, for the object to be shot at.')
    parser.add_argument('display', type=int, help='A bool, a web-browser animation will display if set to true.')

    args = parser.parse_args()

    simulation = TiroOblicuoSimulation(
        height=args.start_height,
        speed=args.shot_speed,
        angle=args.shot_angle
    )

    if args.display:
        simulation.display()

    ts = range(0,round((simulation.flight_time+1)*100))
    vxs = [simulation._speed(t*0.01)[0] for t in ts]
    vys = [simulation._speed(t*0.01)[1] for t in ts]

    sxs = [simulation._shift(t*0.01)[0] for t in ts]
    sys = [simulation._shift(t*0.01)[1] for t in ts]

    import matplotlib.pyplot as plt

    plt.plot(ts,vys)
    plt.ylabel('velocidad en y')
    plt.savefig("graphs/y_velocity.png")
    plt.close()

    plt.plot(ts,vxs)
    plt.ylabel('velocidad en x')
    plt.savefig("graphs/x_velocity.png")
    plt.close()

    plt.plot(ts,sxs)
    plt.ylabel('desplazamiento en x')
    plt.savefig("graphs/x_shift.png")
    plt.close()
    
    plt.plot(ts,sys)
    plt.ylabel('desplazamiento en y')
    plt.savefig("graphs/y_shift.png")

    print(ts,vxs,vys,sxs,sys)