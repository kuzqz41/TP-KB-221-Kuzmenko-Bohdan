import random
def get_str(promt:str):
    while 1:
        x = str(input(promt))
        if (x != "stone" and  x != "scissor" and x != "paper" and x != "exit"):
            print ("Wrong")
        else:
            return x
def rand_str():
    return random.choice(["stone", "scissor", "paper"])
def answ(a,b):
    if (a == "stone" and b == "scissor") or (a == "paper" and b == "stone") or (a == "scissor" and b == "paper"):
        return "You win"
    elif a == b:
        return "Draw"
    else:
        return "Random wins"
while 1:
    choice = get_str('Choise stone, scissor or paper (exit to leave): ')
    if choice == "exit":
        break
    rand_choice = rand_str()
    print ("Random choice - ", rand_choice)
    print (answ(choice, rand_choice))