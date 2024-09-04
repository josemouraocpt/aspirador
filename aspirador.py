import time

class Aspirador:
    def __init__(self, start_position, environment):
        self.position = start_position
        self.environment = environment
        self.battery = 10
        self.battery_cicles = 1

    def clean(self):
        x,y = self.position
        print("Aspirando...")
        time.sleep(1)
        self.environment[x][y] = 0
        return self.position
            
    def move_next(self):
        self.battery = self.battery - 1
        x,y = self.position
        self.position = (x, y + 1)
        time.sleep(1)
        print("Movendo para próxima posição: ", self.position)
        if self.environment[x][y+1] == 1:
            self.clean()
        return self.position
    
    def move_previous(self):
        self.battery = self.battery - 1
        x,y = self.position
        self.position = (x, y - 1)
        time.sleep(1)
        print("Movendo para posição anterior: ", self.position)
        if self.environment[x][y-1] == 1:
            self.clean()
        return self.position
    
    def next_line(self):
        self.battery = self.battery - 1
        x,y = self.position
        self.position = (x + 1, y)
        time.sleep(1)
        print("Movendo para próxima linha: ", self.position)
        if self.environment[x+1][y] == 1:
            self.clean()
        return self.position
    
    def previous_line(self):
        self.battery = self.battery - 1
        x,y = self.position
        self.position = (x - 1, y)
        time.sleep(1)
        print("Movendo para linha anterior: ", self.position)
        if self.environment[x-1][y] == 1:
            self.clean()
        return self.position

    def start(self):
        done = False
        count = 0

        #Mapeando todas as posições sujas
        dirty_places = []
        for i in range(0, len(self.environment)):
            for j in range(0, len(self.environment[i])):
                if self.environment[i][j] == 1:
                    dirty_places.append((i,j))
        while not done:
            x1, y1 = dirty_places[count]
            x2, y2 = self.position

            last_dirty_spot = dirty_places[len(dirty_places) - 1]

            if self.environment[x1][y1] == 0:
                if count + 1 <= len(dirty_places):
                    x1, y1 = dirty_places[count + 1]
            
            if self.battery == 0:
                print("A bateria chegou ao fim")
                print("Voltando para posição inicial...")
                x2, y2 = (0, 0)
                self.position = (0, 0)
                self.battery = 10
                self.battery_cicles = self.battery_cicles + 1
                time.sleep(2)
                print("Iniciando novamente o ciclo...")
                time.sleep(1)

            if y2 < y1 and y2 + 1 < len(self.environment[x2]) and self.environment[x2][y2 + 1] != -1:
                self.move_next()

            elif x1 > x2 and x2 + 1 < len(self.environment) and self.environment[x2 + 1][y2] != -1:
                self.next_line()

            elif x1 > x2 and self.environment[x2][y2 + 1] == 0:
                self.move_next()
                
            elif x2 == x1 and y2 > y1 and y2 - 1 > 0 and self.environment[x2][y2 - 1] != -1:
                self.move_previous()

            elif y1 < y2 and x2 == x1:
                if -1 not in self.environment[x2 - 1]:
                    self.previous_line()
                    for i in range(y1, y2):
                        self.move_previous()
            else:
                count = count + 1
            if count == len(dirty_places) - 1:
                print("Sala limpa :)")
                done = True

            
            
            

if __name__ == "__main__":
    sala = [
    [0,  1,  0,  0, -1],
    [0, -1,  1,  0,  0],
    [0,  0,  0,  1,  0],
    [1, -1,  0,  0,  0],
    [0,  0,  1,  0,  0]
    ]

    sala2 = [
    [0,  1,  0,  0, 0, 1],
    [0, -1,  1,  0,  0, 1],
    [0,  0,  0,  1,  0, 1],
    [1, -1,  0,  0,  0, 1],
    [0,  0,  1,  1,  0, 1],
    [1,  0,  0,  1,  0, 0]
    ]

    agente = Aspirador((0,0), sala2)

    for linha in sala2:
        print(linha)
    
    print("\n")

    agente.start()

    print(agente.environment)
    print("Movimentos restantes: ", agente.battery)
    print("Ciclos de baterias necessários para limpar a sala: ", agente.battery_cicles)