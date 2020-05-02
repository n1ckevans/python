import random
class Pokemon:
 def __init__(self, name, move=[], health=100):
   self.name = name
   self.health = health
   self.move = move
 def dump(self):
   out = ""
   out += f"Name: {self.name} HP: {self.health}"
   for mv in self.move:
     out +="\n"
     out += mv.dump()
   return out
class Moves:
 def __init__(self, name, times_available, damage):
   self.name = name
   self.times_available = times_available
   self.damage = damage
 def dump(self):
   return f"\tMove: {self.name}     PP: {self.times_available}"
def setChar(char, allPokes):
 for i in range(len(allPokes[char["pokeId"]].move)):
   char["mvsRemain"][i] = allPokes[char["pokeId"]].move[i].times_available
 return char
def checkPP(attacker, mv_id):
 if attacker['mvsRemain'][mv_id] <= 0:
   return False
 return True
def attack(attacker, attacked, mv_id, allPokes):
 attacked["pokeHealth"] -= allPokes[attacker["pokeId"]].move[mv_id].damage
 attacker['mvsRemain'][mv_id] -= 1
def disHealth():
 print(f"P1 HP: {player['pokeHealth']}")
 print(f"CPU HP: {cpu['pokeHealth']}")
def playerMove():
 while True:
   print(f"Move 0: {allPokes[player['pokeId']].move[0].name}\t\tPP: {player['mvsRemain'][0]}")
   print(f"Move 1: {allPokes[player['pokeId']].move[1].name}\t\tPP: {player['mvsRemain'][1]}")
   print(f"Move 2: {allPokes[player['pokeId']].move[2].name}\t\tPP: {player['mvsRemain'][2]}")
   print(f"Move 3: {allPokes[player['pokeId']].move[3].name}\t\tPP: {player['mvsRemain'][3]}")
   print("Select your Move")
   selMove = input()
   if (not selMove.isdigit() or int(selMove) < 0 or int(selMove) > 3):
     print("Invalid move, Please input number between 0 and 3")
     continue
   if checkPP(player, int(selMove)) is True:
     break
   else:
     print("No more PP left")
 attack(player, cpu, int(selMove), allPokes)
 print(f"You select Move {allPokes[player['pokeId']].move[int(selMove)].name}")
def cpuMove():
 while True:
   selMove = random.randint(0, len(allPokes[cpu["pokeId"]].move) - 1)
   if selMove < 0 or selMove > 3:
     continue
   if checkPP(cpu, selMove) is True:
     break
 attack(cpu, player, selMove, allPokes)
 print(f"CPU select Move {allPokes[cpu['pokeId']].move[selMove].name}")

def initState(player, cpu):
 print("Welcome to Jon and Nick's Pokémon Game!")
 print("                            .::.")
 print("                             .;:**'               ")
 print("                              `                   ")
 print("  .:XHHHHk.              db.   .;;.     dH  MX    ")
 print("oMMMMMMMMMMM       ~MM  dMMP :MMMMMR   MMM  MR      ~MRMN")
 print("QMMMMMb  \"MMX       MMMMMMP !MX' :M~   MMM MMM  .oo. XMMM 'MMM")
 print("  `MMMM.  )M> :X!Hk. MMMM   XMM.o\"  .  MMMMMMM X?XMMM MMM>!MMP")
 print("   'MMMb.dM! XM M'?M MMMMMX.`MMMMMMMM~ MM MMM XM `\" MX MMXXMM")
 print("    ~MMMMM~ XMM. .XM XM`\"MMMb.~*?**~ .MMX M t MMbooMM XMMMMMP")
 print("     ?MMM>  YMMMMMM! MM   `?MMRb.    `\"\"\"   !L\"MMMMM XM IMMM")
 print("      MMMX   \"MMMM\"  MM       ~%:           !Mh.\"\"\" dMI IMMP")
 print("      'MMM.                                             IMX")
 print("       ~M!M                                             IMP")
 print("")
 print("Choose your Pokémon")
 for i in range(len(allPokes)):
   print(f"ID: {i} {allPokes[i].dump()}")
 print("Input your Pokémon ID:")
 while True:
   tmp = input()
   if (not tmp.isdigit() or int(tmp) < 0 or int(tmp) >= len(allPokes)):
     print("Invalid input, Please input number between 0 and 3")
   else:
     player["pokeId"] = int(tmp)
     break
 player = setChar(player, allPokes)
 print(f"You selected {allPokes[player['pokeId']].name}")
 cpu["pokeId"] = random.randint(0, len(allPokes) - 1)
 cpu = setChar(cpu, allPokes)
 print(f"CPU selected {allPokes[cpu['pokeId']].name}")
 mvNow = random.randint(0, 1)
 if mvNow == 0:
   print("You move first")
   return mvNow
 else:
   print("CPU moves first")
   return mvNow

def gameState(player, cpu, mvNow):
 while(player["pokeHealth"] > 0 and cpu["pokeHealth"] > 0):
   if mvNow == 0:
     playerMove()
     mvNow = 1
   else:
     cpuMove()
     mvNow = 0
   if (player["pokeHealth"] > 0 and cpu["pokeHealth"] > 0):
     disHealth()
 if player["pokeHealth"] <= 0:
   print("You Lose, better luck next time!")
 else:
    print("You Win!")

def endState(player, cpu):
 print("Press Enter to play again or any other key to exit")
 inStr = input()
 if inStr == "":
   player["pokeHealth"] = 100
   cpu["pokeHealth"] = 100
   return True
 return False

attack1 = Moves("Scratch", 20, 5)
attack2 = Moves("Tackle", 10, 10)
attack3 = Moves("Headbutt", 8, 12)
attack4 = Moves("Vine Whip", 5, 15)
attack5 = Moves("Ember", 5, 15)
attack6 = Moves("Water Gun", 5, 15)
attack7 = Moves("Thunder Shock", 5, 20)
bulbasaur = Pokemon("Bulbasaur", [attack1, attack2, attack3, attack4])
charmander = Pokemon("Charmander", [attack1, attack2, attack3, attack5])
squirtle = Pokemon("Squirtle", [attack1, attack2, attack3, attack6])
pikachu = Pokemon("Pikachu", [attack1, attack2, attack3, attack7])
allPokes = [bulbasaur, charmander, squirtle, pikachu]
player = {
 "pokeId": 0,
 "pokeHealth": 100,
 "mvsRemain": [0, 0, 0, 0]
}
cpu = {
 "pokeId": 0,
 "pokeHealth": 100,
 "mvsRemain": [0, 0, 0, 0]
}

mvNow = 0
state = True
while state:
  mvNow = initState(player, cpu)
  gameState(player, cpu, mvNow)
  state = endState(player, cpu)

print("Thank you for playing!")