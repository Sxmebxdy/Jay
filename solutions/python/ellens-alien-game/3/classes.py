"""Solution to Ellen's Alien Game exercise."""


class Alien:
    total_aliens_created = 0
    """Create an Alien object with location x_coordinate and y_coordinate.

    Attributes
    ----------
    (class)total_aliens_created: int
    x_coordinate: int - Position on the x-axis.
    y_coordinate: int - Position on the y-axis.
    health: int - Number of health points.

    Methods
    -------
    hit(): Decrement Alien health by one point.
    is_alive(): Return a boolean for if Alien is alive (if health is > 0).
    teleport(new_x_coordinate, new_y_coordinate): Move Alien object to new coordinates.
    collision_detection(other): Implementation TBD.
    """
    
    def __init__(self, x_coordinate, y_coordinate, health = 3,):
        Alien.total_aliens_created += 1
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate
        self.health = 3
    
    def hit(self):
        self.health -= 1
    
    def is_alive(self):
        if self.health <= 0:
            return False
        return True

    def teleport(self, new_x, new_y):
        self.x_coordinate = new_x
        self.y_coordinate = new_y

    def collision_detection(self,other_object):
        pass

    def total_aliens_create(self):
        return Alien.total_aliens_created
        
#TODO:  create the new_aliens_collection() function below to call your Alien class with a list of coordinates.
def new_aliens_collection(liste):
    l = list()
    for item in liste:
        new_al = Alien(item[0], item[1])
        l.append(new_al)
    return l
    
