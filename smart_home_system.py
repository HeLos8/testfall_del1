# smart_home_system.py

class SmartHomeSystem: #en klass som är som en mall för att skapa objekt
    def control_light(self, room, state): #metod som tar tre parameter. self gör att metoden kan komma åt attribut och
        #andra metoder i samma objekt
        #room en parameter som förväntas representera rummet där belysningen ska kontrolleras
        #state en parameter som anger det önskade tillståndet för belysningen tex on eller off
        # Kod för att kontrollera ljuset
        pass #nyckelord som används som en platshållare, betyder "gör ingenting" denna rad kan ersätta
    #med den faktiska koden som kontrollerar belysningen när man implementerar systemet

    def schedule_lighting(self, room, time, state): #en annan metod som tar fyra parameter
        #room används för att specificera i vilket rum schemaläggningen ska appliceras
        #time tiden då ljuset ska ändras till det angivna tillståndet
        #state det önskade tillståndet för ljuset vid den specificerade tiden, tex on eller off
        # Kod för att schemalägga ljuset
        pass
