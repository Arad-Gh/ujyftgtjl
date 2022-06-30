import random
print("How do you wanna play the game?")
ba_ki = input("with another player = player 2 or with computer=computer : ")
tedad = int(input ("How many times you want to play ?"))
entkhab = ["rock", "paper", "scissors"]
if ba_ki == "computer": 
    emtiaz_computer=0
    emtiaz_player=0
    while tedad != 0 :
        computer = random.choice(entkhab)
        player = input("select [rock or paper or scissors]=")
        print (f"player choice = {player} / computer choice = {computer}")
        if player == computer:
            print ("draw")
        if player == "rock"and computer == "scissors":
                print ("player win")
                emtiaz_player=emtiaz_player+1
        if player == "rock" and computer =="paper":
                print ("computer win")
                emtiaz_computer=emtiaz_computer+1
        if player == "paper" and computer == "rock":
                print("player win")
                emtiaz_player=emtiaz_player+1
        if player == "paper"and computer == "scissors":
                print ("computer win")
                emtiaz_computer=emtiaz_computer+1
        if player == "scissors"and computer == "paper":
                print ("player win")
                emtiaz_player=emtiaz_player+1
        if player == "scissors" and computer == "rock":
                print ("computer win")  
                emtiaz_computer=emtiaz_computer+1
        tedad = tedad - 1
        print("emtiaz_computer = " , emtiaz_computer, "/","emtiaz_player = ",emtiaz_player)  
        print("----------------------------------------------------------------------------") 
        if tedad==0:
            if emtiaz_computer>emtiaz_player:
                print("!!!computer win!!!")
            if emtiaz_computer<emtiaz_player:
                print("!!!player win!!!")
            if emtiaz_computer == emtiaz_player:
                print("!!!Draw!!!")
if ba_ki ==  "player 2":
    emtiaz_player1=0
    emtiaz_player2=0
    while tedad != 0:
        player_1 = input("select [rock or paper or scissors]=")
        player_2 = input ("select [rock or paper or scissors]=")
        print (f"player 1 choice {player_1}, player 2 choice {player_2}")
        if player_1 == player_2:
            print ("draw")
        if player_1 == "rock"and player_2 == "paper":
            print("player 2 win")
            emtiaz_player2=emtiaz_player2+1
        if player_1 == "rock"and player_2 == "scissors":
            print ("player 1 win")
            player_1=player_1+1
        if player_1 == "scissors"and player_2 == "rock":
            print ("player 2 win")
            emtiaz_player2=emtiaz_player2+1
        if player_1 == "scissors" and player_2 == "paper":
            print ("player 1 win")
            emtiaz_player1=emtiaz_player1+1
        if player_1 == "paper"and player_2 == "scissors":
            print ("player 2 win")
            emtiaz_player2=emtiaz_player2+1
        if player_1 == "paper"and player_2 == "rock":
            print ("player 1 win")
            emtiaz_player1=emtiaz_player1+1
        tedad = tedad - 1    
        print("emtiaz_player1 = " ,emtiaz_player1, "/","emtiaz_player2 = ",emtiaz_player2) 
        print("----------------------------------------------------------------------------") 
        if tedad==0:
            if emtiaz_player2>emtiaz_player1:
                print("!!!player2 win!!!")
            if emtiaz_player2<emtiaz_player1:
                print("!!!player1 win!!!")
            if emtiaz_player2==emtiaz_player1:
                print("!!!Draw!!!")