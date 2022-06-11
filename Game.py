import random

while True:
    user_option = input("Enter your choice (R, P, S): ")
    possible_options = ["R", "P", "S"]
    computer_option = random.choice(possible_options)
    print(f"\nPlayer {user_option} : Computer {computer_option}.\n")
    
    if user_option == computer_option:
        print("You got a tie!, restart game")
    elif user_option == "R":
        if computer_option == "S":
            print("Rock smashes scissor, Player win!")
        else:
            print("Paper covers rock, Computer wins")
    elif user_option == "S":
            if computer_option == "P":
                print("Scissor cuts paper, Player wins!")
            else:
                print("Rock smashes scissor, Computer wins!")
    elif user_option == "P":
        if computer_option == "R":
            print("Paper smashes rock, Player wins!")
        else:
            print("Scissor cuts paper, Computer wins!") 
    else:
        print("Error, wrong option")
        user_option = input("Enter your choice (R, P, S): ")    