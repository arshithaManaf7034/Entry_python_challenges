import random

choices = ["rock", "paper", "scissors"]

level = 1

print("🎮 Welcome to Rock Paper Scissors Game!")

while True:
    print(f"\n🔥 Level {level} Started!")
    player_score = 0
    computer_score = 0

    for round_no in range(1, 6):
        print(f"\n--- Round {round_no}/5 ---")
        print("Choose: rock / paper / scissors")
        print("Type 'exit' to quit the game")

        player_choice = input("Your choice: ").lower()

        if player_choice == "exit":
            print("\n👋 You exited the game. Thanks for playing!")
            exit()

        if player_choice not in choices:
            print("❌ Invalid choice! Round skipped.")
            continue

        computer_choice = random.choice(choices)
        print(f"Computer chose: {computer_choice}")

        if player_choice == computer_choice:
            print("🤝 It's a tie!")

        elif (
            (player_choice == "rock" and computer_choice == "scissors") or
            (player_choice == "paper" and computer_choice == "rock") or
            (player_choice == "scissors" and computer_choice == "paper")
        ):
            print("🎉 You win this round!")
            player_score += 1

        else:
            print("💻 Computer wins this round!")
            computer_score += 1

        print(f"Current Score → You: {player_score} | Computer: {computer_score}")

    # End of level
    print("\n🏁 Level Result:")
    print(f"Final Score → You: {player_score} | Computer: {computer_score}")

    if player_score > computer_score:
        print("🏆 You win this level!")
    elif computer_score > player_score:
        print("😞 Computer wins this level!")
    else:
        print("⚖️ This level is a draw!")

    # Continue or Exit
    next_action = input("\nDo you want to continue to next level? (yes/exit): ").lower()

    if next_action != "yes":
        print("\n👋 Game ended. Thanks for playing!")
        break

    level += 1
