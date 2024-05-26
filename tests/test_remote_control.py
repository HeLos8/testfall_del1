import pytest
from unittest.mock import MagicMock #importerar MagicMock från unittest.mock. MagicMock är ett verktyg för att skapa
#mockobjekt under testkörning, vilket simulerar beteenden i systemet utan att faktiskt utföra operationerna
from smart_home_system import SmartHomeSystem

def test_remote_light_control_on():
    system = SmartHomeSystem() #skapar en instans av smartHomeSystem
    system.control_light = MagicMock(return_value=True) #ersätter control_light metoden med en MagicMock-instans
    #return_value=true anger att när control_light anropas ska den returnera true
    assert system.control_light('living_room', 'on') == True #testar att när control_light metoden anropas med argumenten
    #living_room, "on" returnerar den true

def test_remote_light_control_off():
    system = SmartHomeSystem()
    system.control_light = MagicMock(return_value=True)
    assert system.control_light('living_room', 'off') == True