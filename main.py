import random
health = 100

print("Welcome to ZombAvians: Aerial Infection 🧟")

# Initialise the play variable
play = True

# Main game loop
while play:
    # Prompt the user to input whether they want to play
    user_input = input("Do you want to play? (yes/no): ")

    # Check if the user wants to continue playing
    if user_input.lower() != "yes":
        # If the user doesn't want to continue, set play to False to exit the loop
        play = False
    else:
        # If the user wants to play, proceed with the game
        print("🎮 Congratulations! You have chosen to play. Let's have some fun!")

    # Continue with Wave 1
        wave_one = input("🧟‍♂️ Did you eliminate all the zombies? (yes/no): ")
        if wave_one.lower() == "yes":
            print("🌟 You survived Wave 1!")
        else:
            print("💀 If you meet your demise, fear not! Simply press run again and embark on another attempt!")

        print("🌊 Wave 2 will commence now!")
    
    # Continue with Wave 2
    wave_two = input("🧟‍♂️ Mob of zombies looking at the sky. Do you fight or flee? ")
    if wave_two.lower() == "fight":
        print("💪 If you decided to fight, good! You won the fight for the wave! ")
    else:
        print("🏞️ If you decided to flee, too bad. You fell down a mountain and succumbed to your death. ")

    print("🌊 Wave 3 will now commance! ")

    # Continue with Wave 3
    wave_three = input("🧟‍♂️ You see a mini boss and a mob of zombies. What do you do, fight or run away? ")
    if wave_three.lower() == "fight":
        print("👊 Looks like you made it through to Wave 4! ")
    elif wave_three.lower() == "run away":
        print("🏃‍♂️ Well, you ran away, so you failed. Back to the beginning you go! ") 
    else:
        print("🔄 Back to the start")

    print("🌊 Wave 4 will now commance! ")

    # Continue with Wave 4
    wave_four = input("🔊 You hear a horrific sound coming from the distance. Do you go and investigate, and fight, or run away? (fight/run): ")
    if wave_four.lower() == "fight":
        print("💥 Looks like you won against the wave, but were you injured?")
    # Simulate random health changes
        health_change = random.randint(-20, 10)
        player_health = 100
        player_health += health_change
        print(f"🩹 Your health has {'increased' if health_change > 0 else 'decreased'} by {abs(health_change)} points.")
        print(f"💖 Current Health: {player_health}%")
    elif wave_four.lower() == "run":
        print("🏃‍♂️ Well, you ran away, so you avoided potential injuries. Smart move!")
    else:
        print("Looks like you didnt fight or run need to choose one")
    
    print("🌊 Wave 5 will now commance! ")
        
    # Continue with Wave 5
    wave_five = input("🔍 As you explore further, you notice a dark alley on your right and a mysterious door on your left. "
                  "Which path will you take? (alley/door): ")
    if wave_five.lower() == "alley":
        print("🌃 You venture into the dark alley, finding it eerily quiet. What awaits you in the shadows?")
    elif wave_five.lower() == "door":
        print("🚪 You decide to open the mysterious door. Cautiously stepping inside, you discover a hidden room.")

    print("🌊 Wave 6 will now commance! ")

    # Continue with Wave 6
    wave_six = input("🚶‍♂️ Moving forward, you encounter a survivor who seems distressed. "
                     "They offer you a health potion. Do you accept? (yes/no): ")
    if wave_six.lower() == "yes":
        health_potion = random.randint(10, 30)
        player_health += health_potion
        print(f"🧪 You accept the health potion and feel rejuvenated! Health +{health_potion}")
        print(f"💖 Current Health: {player_health}%")
    else:
        print("🙅‍♂️ You decide not to take the health potion. The survivor nods understandingly.")

        print("🌊 Wave 7 will now commance! ")

    # Continue with Wave 7
        wave_seven = input("🧟 You find yourself in a tight spot with only two options:\n"
                   "Fight a mini boss and a horde of zombies or jump across the bridge. What's your choice? (fight/jump): ")
    if wave_seven.lower() == "fight":
        print("💪 You valiantly face the mini boss and the horde, emerging victorious! Onto the next challenge.")
        
    print("🌊Wave 8 will now commance! ")

    # Continue with Wave 8
    wave_eight = input("🧟‍♂️ Now you're in a pickle. Instead of taking a chance with the bridge, you march on ahead. "
                   "Unexpectedly, a large horde of infected stands in your way. Do you fight or find another way around? (fight/around): ")
    if wave_eight.lower() == "fight":
        print("💥 You bravely face the horde, demonstrating exceptional combat skills. On to the next challenge!")
    else:
        print("🚶‍♂️ You opt for a more strategic approach, finding a sneaky path around the horde. Clever move!")
    
    print("🌊 Wave 9 will now commance! ")

    # Continue with Wave 9
    wave_nine = input("🔦 After crushing the mini boss beneath your boot, you find yourself in a dimly lit room. "
                  "On your left, you notice a dial on the wall to adjust the room's brightness. "
                  "On the right, you spot a door, slightly ajar. What will you do? (adjust brightness/open door): ")
    if wave_nine.lower() == "adjust brightness":
        print("🌟 You adjust the brightness and reveal a hidden passage! Onwards to the next challenge!")
    elif wave_nine.lower() == "open door":
        print("🚪 You cautiously open the door, revealing a new area. The adventure continues!")

    print("🌊 Wave 10 will now commance! ")

    # Continue with Wave 10
    wave_ten = input("🤔 Now that you've left the room, you find yourself pondering what exactly it was you avoided. "
                 "In an instant, the door EXPLODES off its hinges, spewing splintering pieces of wood everywhere "
                 "across the room, causing you some minor injuries. What's your next move? (continue exploring/retreat): ")
    if wave_ten.lower() == "continue exploring":
        print("🚀 Undeterred by the door incident, you press forward into the unknown. What lies ahead?")
    else:
        print("🛑 You decide to retreat temporarily, regrouping and assessing your injuries. Safety first!")

# End of the game...
print("Thanks for playing ZombAvians: Aerial Infection! 🎮🧟‍♂️")