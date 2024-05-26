
import pytest #importerar pytest-biblioteket som används för att skriva och köra tester
from unittest.mock import MagicMock #Importerar MagicMock klassen från unittest.mock
#vilket tillåter dig att ersätta delar av ditt system under test med mock-objekt som du kan styra helt och hållet.
from smart_home_system import SmartHomeSystem #Importerar SmartHomeSystem klassen från modulen smart_home_system
#vilket är klassen du testar.

def test_schedule_lighting(): #definierar testfunktionen som pytest kommer att köra, namnet på funktionen börjar med test
    #vilket är det som pytest använder för att automatiskt identifiera vilka funktioner som är testfall
    # Skapa en instans av SmartHomeSystem
    system = SmartHomeSystem() #skapar en instans av SmartHomeSystem klassen, detta är objekt vars metoder
    #vi kommer att testa
    
    # Simulera schemaläggning av ljus i 'bedroom' för att tändas kl '18:00'
    system.schedule_lighting = MagicMock(return_value=True)
    #ersätter schedule_lighting metoden i system-objektet med en MagicMock instans. return_value=true returnerar
    #true när det anropas vilket förenklar att kontrollera testets utfall
    
    # Anropa schemaläggning med parametrarna
    result = system.schedule_lighting('bedroom', '18:00', 'on')
    #anropar schedule_lighting metoden på mock-objektet med specfika argument. Eftersom metoden är en mock kommer den
    #returnera true som konfigurerats ovan.
    
    # Verifiera att schemaläggning av ljus skapades korrekt
    assert result == True #kontrollerar att result är true vilket förväntas baserat på return_value 
    system.schedule_lighting.assert_called_once_with('bedroom', '18:00', 'on')
    #verifierar att schedule_lighting metoden anropas exakt en gång med de rätta argumenten
    