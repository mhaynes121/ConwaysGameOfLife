# This is our lifeform that will spawn, live, decay in a grid coordinate
class lifeform:
    def __init__(self, xpos:int=0, ypos:int=0, neighbors:int=0, alive:bool=False) -> None:
        self.xpos = xpos
        self.ypos = ypos
        self.neighbors = neighbors
        self.alive = alive
        self.generationsLived = 0
        self.generationsDead = 2 # starts eligible for its first-ever birth

    # getr for alive status
    def isAlive(self) -> bool:
        return self.alive
    
    # the miracle of birth
    def beginLife(self) -> None:
        self.alive = True
        self.generationsLived = 0

    # kill off this lifeform
    def endLife(self) -> None:
        self.alive = False
        self.generationsDead = 0

    # called once per generation for a lifeform that survives into the next one;
    # dies of old age after living ~80 human-equivalent years (4 generations)
    def ageOneGeneration(self) -> None:
        self.generationsLived += 1
        if self.generationsLived >= 4:
            self.endLife()

    # called once per generation for a lifeform that remains dead; tracks how
    # long it's been dead so evolveLife() can enforce a rebirth cooldown
    def ageOneDeadGeneration(self) -> None:
        self.generationsDead += 1

    # display the appropriate ascii character depending on if this lifeform is living or not
    def printSelf(self, debugMode) -> None:
        if debugMode == 1: # if debuging is set to 1 let's show the number of neighbors instead as that's more useful
            if self.alive:
                print(str(self.neighbors), end = '')
            else:
                print(u'\xb7', end = '') # u'\xb7'     #  0xFA -> MIDDLE DOT
        elif debugMode == 2: # if it's set to 2 let's show the number of generations this LF has lived
            if self.alive:
                print(str(self.generationsLived), end = '')
            else:
                print(u'\xb7', end = '') # u'\xb7'     #  0xFA -> MIDDLE DOT
        else:
            if self.alive:
                print(u'\u2593', end = '') # u'\u2593'   #  0xB2 -> DARK SHADE
            else:
                print(u'\xb7', end = '') # u'\xb7'     #  0xFA -> MIDDLE DOT
