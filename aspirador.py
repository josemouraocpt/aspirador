import time

class Aspirador:
    def __init__(self, start_position, dirty, obstacle, environment):
        self.position = start_position
        self.is_dirty = dirty
        self.have_obstacle = obstacle
        self.environment = environment

    def clean(self):
        x,y = self.position
        print("Aspirando...")
        time.sleep(1)
        self.environment[x][y] = 0
        return self.position
            
    def move_next(self):
        x,y = self.position
        self.position = (x, y + 1)
        print("Movendo para próxima posição: ", self.position)
        if self.environment[x][y+1] == 1:
            self.clean()
        return self.position
    
    def move_previous(self):
        x,y = self.position
        self.position = (x, y - 1)
        print("Movendo para posição anterior: ", self.position)
        return self.position
    
    def next_line(self):
        x,y = self.position
        self.position = (x + 1, y)
        print("Movendo para próxima linha: ", self.position)
        if self.environment[x+1][y] == 1:
            self.clean()
        return self.position
    
    def previous_line(self):
        x,y = self.position
        self.position = (x - 1, y)
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
            if 1 in self.environment[i]:
                dirty_places.append((i, self.environment[i].index(1)))
        print(dirty_places)

        while not done:
            x1, y1 = dirty_places[count]
            x2, y2 = self.position
            if y2 < y1 and y2 + 1 < len(self.environment[x2]) and self.environment[x2][y2 + 1] != -1:
                self.move_next()
            elif x1 > x2 and x2 + 1 < len(self.environment) and self.environment[x2 + 1][y2] != -1:
                self.next_line()
            elif x1 > x2 and self.environment[x2][y2 + 1] == 0:
                self.move_next()
            elif y1 < y2 and x2 == x1:
                if -1 not in self.environment[x2 - 1]:
                    self.previous_line()
                    for i in range(y1, y2):
                        self.move_previous()
            else:
                count = count + 1
            if count == 5:
                done = True

            
            
            

if __name__ == "__main__":
    sala = [
    [0,  1,  0,  0, -1],
    [0, -1,  1,  0,  0],
    [0,  0,  0,  1,  0],
    [1, -1,  0,  0,  0],
    [0,  0,  1,  0,  0]
    ]

    agente = Aspirador((0,0), False, True, sala)

    for linha in sala:
        print(linha)
    
    print("\n")

    # for linha in sala:
    #     for coluna in linha:
    #         agente.can_move(coluna)

    # print("\n")

    

    agente.start()

    print(agente.environment)