from Gothans.Classes.Map import *
from Gothans.Classes.Engine import *
from Gothans.Functions import *

principalTitle("Gothons Game")
a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()