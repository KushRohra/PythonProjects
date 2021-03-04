from chessdotcom import get_leaderboards, get_player_stats, get_player_game_archives
import pprint
import requests

printer = pprint.PrettyPrinter()


def print_leaderboards():
    data = get_leaderboards().json
    categories = data.keys()

    for category in categories:
        print("Category : ", category)
        for index, entry in enumerate(data[category]):
            print(f'Rank: {index + 1} | Username: {entry["username"]} | Rating: {entry["score"]}')


def get_player_ratings(username):
    try:
        data = get_player_stats(username)
    except Exception as e:
        print("Please enter a valid username")
        return
    data = data.json()
    categories = ['chess_blitz', 'chess_bullet', 'chess_rapid', 0]
    for category in categories:
        if category in list(data.keys()):
            categories[-1] = 1
            print("Category : ", category)
            print(f'Current Rating: {data[category]["last"]["rating"]}')
            print(f'Best Rating: {data[category]["best"]["rating"]}')
            print(f'Games won: {data[category]["record"]["win"]}')
            print(f'Games lost: {data[category]["record"]["loss"]}')
            print(f'Games draw: {data[category]["record"]["draw"]}')
            print()
    if categories[-1] == 0:
        print("No existing data for such a username. Please check and enter the username carefully")


def get_most_recent_game(username):
    try:
        data = get_player_game_archives(username)
    except Exception as e:
        print("Please enter a valid username")
        return
    data = data.json
    if len(data['archives']) == 0:
        print("No details for player with such username")
        return
    url = data['archives'][-1]
    games = requests.get(url).json()
    game = games['games'][-1]
    blackPlayer, whitePlayer = game['black'], game['white']
    print("Black Player Details: ")
    print("Username: " + blackPlayer['username'] + " | Rating: " + str(blackPlayer['rating']) + " | Result: " + blackPlayer['result'])
    print("White Player Details: ")
    print("Username: " + whitePlayer['username'] + " | Rating: " + str(whitePlayer['rating']) + " | Result: " + whitePlayer['result'])


def main():
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


if __name__ == "__main__":
    main()
