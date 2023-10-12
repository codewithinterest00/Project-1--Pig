import random


def roll():
    min_value=1
    max_value=6
    roll=random.randint(min_value,max_value)
    return roll
    
value=roll()
# print(value)


while True:
    players=input("Enter the numbers of players(2-4): ")
    if players.isdigit():
        players=int(players)
        if 2<=players<=4:
            break
        else:
            print("Must be between 2-4")
    else:
        print("Invalid, Try again")

print(players)


max_score=50
players_score=[0 for _  in range(players) ]

while max(players_score)<max_score:
    for player_index in range(players):
        print("\nPlayer number: ",player_index+1,"has just strated!\n")
        print("Your total score is ",players_score[player_index ])
        current_score=0
        while True:
            should_roll=input("Do you want to roll(Y)? ")
            if should_roll.lower()!="y":
                break
            value=roll()
            if value==1:
                print("You rolled 1! turn done!")
                current_score=0
                break
            else:
                current_score+=value
                print("You rolled :",value)

        players_score[player_index]+=current_score
        print("Your total score is :",players_score[player_index])


max_score=max(players_score)
winning_index=players_score.index(max_score)
print("player number ",winning_index+1,"is the winner")