from Models import Accelerometer, Gyroscope, GPSSubject, GPSObserver, User
from Emulator import current_acceleration, current_gyroscope, current_location
import time


acc = Accelerometer(current_acceleration())
gyro = Gyroscope(current_gyroscope())
gps_observer = GPSObserver('GPS')
acc.attach(gps_observer)
gyro.attach(gps_observer)


gps_subject = GPSSubject(current_location())
navdeep = User('Navdeep')
gps_subject.attach(navdeep)


theft_detection_control = True


while theft_detection_control and not gps_subject.get_state():

    # At first, the accelerometer and gyroscope will check for any change in state of bicycle
    while not acc.get_state() and not gyro.get_state():
        acc.check_for_movement(current_acceleration())
        if acc.get_state():
            acc.notify_observer()
            break
        
        gyro.check_for_orientation_change(current_gyroscope())
        if gyro.get_state():
            gyro.notify_observer()
            break

    # Now GPS will check whether the bicycle mmoves out of the safe distance
    for i in range(40):
        gps_subject.calculate_distance(current_location())

        if gps_subject.get_state():
            gps_subject.notify_observer()
            break
        else:
            time.sleep(3.0)
            continue

