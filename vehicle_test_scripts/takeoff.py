from dronekit import connect, VehicleMode, LocationGlobalRelative
from base_functions import *
import time

while True:
    if vehicle.mode == "GUIDED":
        time.sleep(2)
        arm_and_takeoff(10)
        time.sleep(10)
        vehicle.mode = "LAND"
        break



