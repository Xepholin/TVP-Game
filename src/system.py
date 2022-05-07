from tkinter import *

class Pump(object):
    """A simple pump that allows tank to receive fuel"""

    def __init__(self, id, state = 1) -> None:
        '''
        Create a Pump object

                Parameters:
                        id (int) : A Integer
                        state (int) : A Integer, value = -1, 0 or 1 -> -1 = broken / 0 = stopped / 1 = worked
        '''
        if (state in [-1, 0, 1]):
            self.id = id
            self.state = state
        else:
            raise ValueError("Value of state should be -1, 0 or 1, got {}".format(state))
    def get_id(self):
        return self.id

    def get_state(self):
        return self.state

    def set_id(self, new_id):
        self.id = new_id
    
    def set_state(self, new_state):
        if (new_state in [-1, 0, 1]):
            self.state = new_state
        else:
            raise ValueError("Value of new state should be -1, 0 or 1, got {}".format(new_state))


class Tank(object):
    """A simple tank that stores fuel"""

    def __init__(self, canvas, id, first_pump, second_pump, quantityMax, color, state = 1) -> None:
        '''
        Create a Tank object

                Parameters:
                        canvas (Canvas) : A Canvas object
                        id (int) : A Integer
                        first_pump (Pump) : A Pump object
                        second_pump (Pump) : A Pump object
                        quantity (int) : A Integer, represents quantity of fuel in the tank
                        state (int) : A Integer, value = 0 or 1 -> 0 = empty / 1 = full
        '''
        if (isinstance(canvas, Canvas)):
            if (state in [0, 1]):
                if (quantityMax > 0):
                    if (isinstance(first_pump, Pump) and isinstance(second_pump, Pump)):
                        if (color in ["orange", "green", "yellow"]):
                            self.canvas = canvas
                            self.id = id
                            self.state = state
                            self.quantityMax = quantityMax
                            self.quantity = quantityMax
                            self.color = color
                            self.first_pump = first_pump
                            self.second_pump = second_pump
                        else:
                            raise ValueError("Color should be orange, green or yellow, got {}".format(color))
                    else:
                        raise TypeError("Type of pumps should be Pump, got {} and {}".format(type(first_pump), type(second_pump)))
                else:
                    raise ValueError("Value of quantity must be greater than 0")
            else:
                raise ValueError("Value of state should be 0 or 1, got {}".format(state))
        else:
            raise TypeError("Canvas should be Canvas, got {}".format(type(canvas)))

    def get_id(self):
        return self.id

    def get_first_pump(self):
        return self.first_pump

    def get_second_pump(self):
        return self.second_pump

    def get_state(self):
        return self.state

    def get_quantityMax(self):
        return self.quantityMax

    def get_quantity(self):
        return self.quantity

    def set_id(self, new_id):
        self.id = new_id

    def set_first_pump(self, new_pump):
        if (isinstance(new_pump, Pump)):
            self.first_pump = new_pump
        else:
            raise TypeError("Type of new pump should be Pump, got {}".format(type(new_pump)))

    def set_second_pump(self, new_pump):
        if (isinstance(new_pump, Pump)):
            self.second_pump = new_pump
        else:
            raise TypeError("Type of new pump should be Pump, got {}".format(type(new_pump)))

    def set_state(self, new_state):
        if (new_state in [0, 1]):
            self.state = new_state
        else:
            raise ValueError("Value of new state should be 0 or 1, got {}".format(new_state))

    def set_quantityMax(self, new_quantityMax):
        if (isinstance(new_quantityMax, int)):
            self.quantityMax = new_quantityMax
        else:
            raise TypeError("Type of new quantity max should be a integer, got {}".format(type(new_quantityMax)))
    
    def set_quantity(self, new_quantity):
        if (isinstance(new_quantity, int)):
            self.quantity = new_quantity
        else:
            raise TypeError("Type of new quantity should be a integer, got {}".format(type(new_quantity)))


class Valve(object):
    """A simple valve that used to open fuel access"""

    def __init__(self, id, state = 0) -> None:
        '''
        Create a Valve object

                Parameters:
                        id (int) : A Integer
                        state (int) : A Integer, value = 0 or 1 -> 0 = close / 1 = open
        '''

        if (state in [0, 1]):
            self.id = id
            self.state = state
        else:
            raise ValueError("Value of state should be 0 or 1, got {}".format(state))

    def get_id(self):
        return self.id

    def get_state(self):
        return self.state

    def set_id(self, new_id):
        self.id = new_id

    def set_state(self, new_state):
        if (new_state in [0, 1]):
            self.state = new_state
        else:
            raise ValueError("Value of new state should be 0 or 1, got {}".format(new_state))

class Player(object):
    """A player that controls pumps, tanks, valves"""

    def __init__(self, username, password, score = 0) -> None:
        '''
        Create a Player object
                Parameters:
                        username (str) : A string to name the player
                        password (str) : A string, required to find the player, double check
                        score (int) : A inetger
        '''

        if (isinstance(username, str)):
            if (isinstance(password, str)):
                self.user = username
                self.pwd = password
                self.score = score
            else:
                raise TypeError("password is not a string, got {}".format(type(password)))
        else:
            raise TypeError("username is not a string, got {}".format(type(username)))

class Simulation(object):
    '''An aircraft fuel system operating simulator'''

    def __init__(self, player, tank1, tank2, tank3, valveT12, valveT23, valve13, valve12, valve23) -> None:
        '''
        Create a Simulation object

                Parameters:
                        player (Player) : A Player object
                        tank1 (Tank) : A Tank object
                        tank2 (Tank) : A Tank object
                        tank3 (Tank) : A Tank object
                        valveT12 (Valve) : A Valve object
                        valveT23 (Valve) : A Valve object
                        valve13 (Valve) : A Valve object
                        valve12 (Valve) : A Valve object
                        valve23 (Valve) : A Valve object
        '''

        if (isinstance(player, Player)):
            if (isinstance(tank1, Tank) and isinstance(tank2, Tank) and isinstance(tank3, Tank)):
                if (isinstance(valveT12, Valve) and isinstance(valveT23, Valve) and isinstance(valve13, Valve) and isinstance(valve12, Valve) and isinstance(valve23, Valve)):
                    self.player = player
                    self.tank1 = tank1
                    self.tank2 = tank2
                    self.tank3 = tank3
                    self.valveT12 = valveT12
                    self.valveT23 = valveT23
                    self.valve13 = valve13
                    self.valve12 = valve12
                    self.valve23 = valve23
                else:
                    raise TypeError("Valves should be a Valve, got {}, {}, {}, {} and {}".format(type(valveT12), type(valveT23), type(valve13), type(valve12), type(valve23)))
            else:
                raise TypeError("Tanks should be a Tank, got {}, {} and {}".format(type(tank1), type(tank2), type(tank3)) )
        else:
            raise TypeError("Player should be a Player, got {}".format(type(player)))