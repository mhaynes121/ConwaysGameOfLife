# This is our lifeform that will spawn, live, decay in a grid coordinate
class lifeform:
    def __init__(self, xpos:int=0, ypos:int=0, neighbors:int=0, alive:bool=False) -> None:
        self.xpos = xpos
        self.ypos = ypos
        self.neighbors = neighbors
        self.alive = alive
        self.generationsLived = 0

    # getr for alive status
    def isAlive(self) -> bool:
        return self.alive
    
    # the miracle of birth
    def beginLife(self) -> None:
        self.alive = True

    # kill off this lifeform
    def endLife(self) -> None:
        self.alive = False

    # display the appropriate ascii character depending on if this lifeform is living or not
    def printSelf(self, debugMode) -> None:
        # We call this each game loop so this can also be short circuited into a generation counter for each lifeform.
        self.generationsLived += 1

        if debugMode: # if debuging let's show the number of neighbors instead as that's more useful
            if self.alive:
                print(str(self.neighbors), end = '')
            else:
                print(u'\xb7', end = '') # u'\xb7'     #  0xFA -> MIDDLE DOT
        else:
            if self.alive:
                print(u'\u2593', end = '') # u'\u2593'   #  0xB2 -> DARK SHADE
            else:
                print(u'\xb7', end = '') # u'\xb7'     #  0xFA -> MIDDLE DOT

        # If we lived for 4 generations, aprox 80 year life span human years, we will die off due to old age.
        if self.generationsLived >= 4:
            self.endLife()
