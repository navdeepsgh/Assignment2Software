import geopy
from geopy.distance import geodesic


# Abstract Subject Class
class Subject:
    def attach(self, observer):
        pass
    
    def detach(self, observer):
        pass
    
    def notify_observer(self):
        pass


# Abstract Observer Class
class Observer:
    def update(self, message):
        pass


# Concrete Subject class of Accelerometer
class Accelerometer(Subject):

    # movement_detected variable denotes the state of the Accelerometer Subject
    def __init__(self, reference_reading):
        self.observers = []
        self.movement_detected = False
        self.reference_acceleration = reference_reading
    
    def attach(self, observer):
        self.observers.append(observer)
    
    def detach(self, observer):
        self.observers.remove(observer)
    
    def notify_observer(self):
        for observer in self.observers:
            observer.update("Accelerometer Detected the Movement")
    
    def check_for_movement(self, current_reading):
        difference_limit = abs((self.reference_acceleration - current_reading))
        if difference_limit > 0.5:
            self.movement_detected = True
    
    def get_state(self):
        return self.movement_detected
    

# Concrete Subject class of Gyroscope
class Gyroscope(Subject):

    # orientation_changed variable denotes the state of the Gyroscope Subject
    def __init__(self, reference_reading):
        self.observers = []
        self.orientation_changed = False
        self.reference_reading = reference_reading
    
    def attach(self, observer):
        self.observers.append(observer)
    
    def detach(self, observer):
        self.observers.remove(observer)
    
    def notify_observer(self):
        for observer in self.observers:
            observer.update("Gyroscope Detected change in the Orientation")
    
    def check_for_orientation_change(self, current_reading):
        ref_x, ref_y, ref_z = self.reference_reading
        current_x, current_y, current_z = current_reading
        #print(ref_x, ref_y, ref_z)
        #print(current_x, current_y, current_z)
        if abs((ref_x - current_x))>0.07 or abs((ref_y - current_y))>0.07 or abs((ref_z - current_z))>0.07:
            self.orientation_changed = True
    
    def get_state(self):
        return self.orientation_changed


# Concrete Subject class of GPS
class GPSSubject(Subject):
    
    # distance_exceeded variable denotes the state of the GPS Subject
    def __init__(self, reference_location):
        self.observers=[]
        self.distance_exceeded = False
        self.reference_location=reference_location
    
    def attach(self, observer):
        self.observers.append(observer)
    
    def detach(self, observer):
        self.observers.remove(observer)
    
    def notify_observer(self):
        for observer in self.observers:
            observer.update("Suspicious Activity is Observed, Bicycle is moving out of Safe Distance")
    
    def calculate_distance(self, current_location):
        distance = geodesic(self.reference_location, current_location).m
        print(distance)
        if distance > 11.0:
            self.distance_exceeded = True
    
    def get_state(self):
        return self.distance_exceeded


# Concrete Observer class of GPS
class GPSObserver(Observer):
    def __init__(self, name):
        self.name=name
    
    def update(self, message):
        print(f'{self.name} got message {message}')


# Concrete Observer class of User
class User(Observer):
    def __init__(self, name):
        self.name=name
    
    def update(self, message):
        print(f'{self.name} got message {message}')