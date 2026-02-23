import random

player_health = 100
enemy_health = 100
defending = False

print("🎮 Welcome to the RPG Battle Game!!!")
print("You are fighting a dangerous enemy.\n")

while player_health > 0 and enemy_health > 0:
    print(f"\nPlayer Health: {player_health}")
    print(f"Enemy Health: {enemy_health}")

    print("\nChoose your action:")
    print("1. Attack")
    print("2. Defend")
    print("3. Heal")

    choice = input("Enter your choice (1/2/3): ")

    # Player's turn
    if choice == "1":
        damage = random.randint(10, 30)
        enemy_health -= damage
        print(f"You attack the enemy for {damage} damage!")

    elif choice == "2":
        defending = True
        print("You brace yourself! Enemy attack will be reduced.")

    elif choice == "3":
        heal = random.randint(10, 25)
        player_health = min(100, player_health + heal)
        print(f"You heal yourself for {heal} health!")

    else:
        print("Invalid choice! You lose your turn.")

    # Check if enemy is defeated
    if enemy_health <= 0:
        print("\n🎉 You defeated the enemy! Victory is yours!")
        break

    # Enemy's turn
    enemy_damage = random.randint(10, 35)

    if defending:
        enemy_damage //= 2
        defending = False
        print("Your defense reduces the damage!")

    player_health -= enemy_damage
    print(f"Enemy attacks you for {enemy_damage} damage!")

    # Check if player is defeated
    if player_health <= 0:
        print("\n💀 You have been defeated. Game Over.")
        break
