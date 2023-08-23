from random import randint
from time import sleep  
from random import choice
game = {"00":" ","01":" ","02":" ","10":" ","11":" ","12":" ","20":" ","21":" ","22":" "}  

def reader(lists1):
    count = 0
    if lists1[0] == 'X' and len(lists1)==3 or lists1[0]=='O' and len(lists1)==3:
        FV = lists1[0]
        for v in lists1:
            if v == FV:
                if count<3:
                    count+=1
                    if count==3:return str(FV[0])

def vector(index):
    index = int(index)
    if index == 1:return str(index),str(index-1),str(index+1)
    elif index == 0:return str(index),str(index+1),str(index+2)
    elif index == 2:return str(index),str(index-1),str(index-2)

def diagCh():
    val,ch1,ch2=game["11"],[game["00"],game["22"]],[game["02"],game["20"]]
    if val!=" ":
        if ch1[0] == val and ch1[1] == val or ch2[0] == val and ch2[1] == val:
            return val

def check():
    try:
        t = diagCh()
        if t!=None:return t
    except:pass
    for i0 in game.keys():
        x = i0[1]
        y = i0[0]
        count = 0
        things = []
        for i1 in vector(y):
            for i2 in vector(x):
                if count <3:
                    count+=1
                    things.append(game.get(i1+i2))
                    if count==3 and reader(things)!=None:return reader(things)
                    elif count==3 and reader(things)==None:
                        things.clear()
                        count = 0
        for in1 in vector(x):
            for in2 in vector(y):
                count+=1
                things.append(game.get(in2+in1))
                if count==3 and reader(things)!=None:return reader(things)
                elif count==3 and reader(things)==None:
                    things.clear()
                    count = 0

def showGame():
        print("  _____")
        print("2|"+game["20"],game["21"],game["22"]+"|")
        print("1|"+game["10"],game["11"],game["12"]+"|")
        print("0|"+game["00"],game["01"],game["02"]+"|")
        print("  -----")
        print("  0 1 2")
        print(" ")

def insult():
    insults = [
    "Looks like the bot just outplayed you!",
    "I guess binary is more your opponent's language.",
    "Congratulations, you made the bot's day!",
    "Losing to a bot? It's like losing to a toaster.",
    "Don't worry, bots have been training for this moment.",
    "The bot just sent its regards... and a smirk emoji.",
    "Bot: 1, You: 0. Better luck next time!",
    "Well, at least you didn't lose to a vacuum cleaner.",
    "Roses are red, violets are blue, lost to a bot? Yep, that's true.",
    "Remember, the bot doesn't even need coffee to function.",
    "Losing to a bot is like getting beat by a calculator.",
    "The bot's victory dance is truly an algorithmic marvel.",
    "Losing to a bot means you're officially AI-approved.",
    "The bot told me to tell you it's 'feeling electric.'",
    "Losing to a bot builds character... or binary code.",
    "Don't stress, even Shakespeare lost to a typewriter once.",
    "Bot: Just doing its job. You: Well, you tried.",
    "They say the bot is training for the Olympics... in the digital realm.",
    "Losing to a bot? You just got schooled by algorithms.",
    "The bot said it's happy to be your virtual mentor.",
    "Your defeat is the bot's greatest achievement.",
    "Losing to a bot is just a glimpse of the future. Hello, AI overlords!",
    "Bot: Crushing dreams since its last update.",
    "At least bots don't gloat about their victories. Oh, wait..."]
    return choice(insults)
tile = None
enemyTile = None

def turnBased():
    amX = 0
    amO = 0
    for x in game.values():
        if x == 'X':amX+=1
        elif x == 'O':amO+=1
    return 'x' if amO>amX else 'o'

def getEmptyTile():
    for a, b in game.items():
        if b == " ":return a

def Place(place,tileType):
    game[place] = tileType.upper()

def moveEnemy():
    while True:
        cho = choice(list(game.keys()))
        if game[cho]==" ":
            return cho
        

mode = None

def inputError():
    print("TTT: Please input a VALID EMPTY tile position. example : %s" % (getEmptyTile()))
    sleep(1.5)
    showGame()

def isFull():
    for v in game.values():
        if v==" ":return False
    return True

print(" ")
print("Welcome to Tic Tac Toes : Command Prompt Edition, Made by armygogames on Github")
print(" ")
choosemode = input("Fight against? PLR/BOT :")  
if choosemode=="BOT":
    mode = 0
    tile = 'o' if randint(0,1)==0 else 'x'
    enemyTile = 'x' if tile=='o' else 'o'
    print("You vs BOT")
elif choosemode=="PLR":
    mode = 1
    tile = 'o' if randint(0,1)==0 else 'x'
    enemyTile = 'x' if tile=='o' else 'o'
    print("You vs Player 2")
else:
    print("Unknown input, choosing random modes...")
    sleep(.5)
    mode = randint(0,1)
    tile = 'o' if randint(0,1)==0 else 'x'
    enemyTile = 'x' if tile=='o' else 'o'
    print("You vs BOT") if mode == 0 else print("You vs Player 2")
showGame()

while True:
    if isFull()==True:
        print("Tie!")
        print(" ")
        break
    if mode == 1:
        tile = turnBased()
    a = input("Place %s at :" % (tile.upper()))
    if len(a)==2:
        if a in game and game[a] == " ":
            Place(a,tile)
            if mode == 1:
                tile = turnBased()
            winner = check()
            if winner!=None:
                showGame()
                if mode == 0:
                    print("Tile %s has won the game!" % (winner)) if winner == tile.upper() else print(insult())
                else:print("Tile %s has won the game!" % (winner))
                print(" ")
                sleep(2)
                break
            showGame()
            if mode == 0:
                if isFull()==True:
                    print("Tie!")
                    print(" ")
                    break
                print("Bot is moving...")
                sleep(1)
                Place(moveEnemy(),enemyTile)
                showGame()
            winner = check()
            if winner!=None:
                if mode == 0:
                    print("Tile %s has won the game!" % (winner)) if winner == tile.upper() else print(insult())
                else:print("Tile %s has won the game!" % (winner))
                print(" ")
                sleep(2)
                break
        else:inputError()
    elif a == "quit":break
    else:inputError()
