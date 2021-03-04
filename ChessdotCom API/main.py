from chessdotcom import get_leaderboards, get_player_stats
import pprint

printer = pprint.PrettyPrinter()

while True:
    print("1. Print the leaderboards")
    print("2. Get stats for a player")
    print("3. Get recent game details for a player")
    print("4. To exit the process")
    choice = input("Enter a choice number between 1 and 4 ")
    try:
        choice = int(choice)
    except Exception as e:
        print("Please enter a valid number choice")
    if choice == 1:
        print()
        print_leaderboards()
        print()
    elif choice == 2:
        print()
        username = input("Enter the username for the player you want to get the stats for: ")
        get_player_ratings(username)
        print()
    elif choice == 3:
        print()
        username = input("Enter the username for the player you want to get recent game details for: ")
        get_most_recent_game(username)
        print()
    elif choice == 4:
        break