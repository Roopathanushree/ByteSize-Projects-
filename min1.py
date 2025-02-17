import random # to generate random no
#Simulates rolling a six-sided die and returns the result.
#usage of the function  to store the value of the dice
def roll(): #defining roll 
    min_value = 1
    max_value = 6
    roll = random.randint(min_value, max_value) #using randint to store value of randint(a,b)

    return roll

value=roll()
print(value)#printing the random no
#while to ask the user to give the no of players in the given range 
#Gets the number of players from the user, ensuring it's between 2 and 4.
while True:
    players = input("Enter the number of players (2 - 4): ")
    if players.isdigit():
        players = int(players) 
        if 2 <= players <= 4:
            break #to break from the infinte while loop
        else:
            print("Must be between 2 - 4 players.") 
    else:
        print("Invalid, try again.")#if the noubers r not in intrger and any other formayt other than the given condition  then it will execute the else part  which is try again

max_score = 50
player_scores = [0 for _ in range(players)] #tho store the no of players value in range 
#main game loop.runs till the loop meets the hightes score 
while max(player_scores) < max_score:
    for player_idx in range(players):#loop itrative throught each player
        print("\nPlayer number", player_idx + 1, "turn has just started!")
        print("Your total score is:", player_scores[player_idx], "\n")
        current_score = 0

        while True: #Inner loop for a player's turn: continues until the player decides to stop or rolls a 1
            should_roll = input("Would you like to roll (y)? ")
            if should_roll.lower() != "y":# If the player doesn't want to roll, exit the inner loop
                break  # End the player's turn

            value = roll()
            if value == 1:# If the player rolls a 1 the value message will be printed
                print("You rolled a 1! Turn done!")
                current_score = 0
                break
            else: # If the player rolls anything other than a 1 Add the rolled value to the current turn's score
                current_score += value
                print("You rolled a:", value)

            print("Your score is:", current_score)

        player_scores[player_idx] += current_score
        print("Your total score is:", player_scores[player_idx])

max_score = max(player_scores)# Find the highest score achieved in the game (might be over max_score)
winning_idx = player_scores.index(max_score)
print("Player number", winning_idx + 1,
      "is the winner with a score of:", max_score)