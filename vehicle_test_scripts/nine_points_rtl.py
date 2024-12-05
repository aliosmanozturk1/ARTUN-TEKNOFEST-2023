from dronekit import connect, VehicleMode, LocationGlobalRelative
from base_functions import *
import time

location1 = LocationGlobalRelative(39.48200490, 29.89861470, 20)
location2 = LocationGlobalRelative(39.48181130,	29.89837200, 20)
location3 = LocationGlobalRelative(39.48159600,	29.89867240, 20)
location4 = LocationGlobalRelative(39.48182790,	29.89894460, 20)
location5 = LocationGlobalRelative(39.48198730,	29.89866030, 20)
location6 = LocationGlobalRelative(39.48181240,	29.89844040, 20)
location7 = LocationGlobalRelative(39.48167470,	29.89866700, 20)
location8 = LocationGlobalRelative(39.48182380,	29.89883200, 20)
location9 = LocationGlobalRelative(39.48187760,	29.89864290, 20)

while True:
    if vehicle.mode == "GUIDED":
        time.sleep(2)
        arm_and_takeoff(20)
        time.sleep(1)

        advanced_goto(location1)
        advanced_goto(location2)
        advanced_goto(location3)
        advanced_goto(location4)
        advanced_goto(location5)
        advanced_goto(location6)
        advanced_goto(location7)
        advanced_goto(location8)
        advanced_goto(location9)

        time.sleep(3)
        vehicle.mode = "RTL"
        break

