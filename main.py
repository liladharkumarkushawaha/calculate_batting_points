# main.py
import cricket_scoring

players = [
    {'name': 'Virat Kohli', 'role': 'bat', 'runs': 112, '4': 10, '6': 0, 'balls': 119, 'field': 0},
    {'name': 'du Plessis', 'role': 'bat', 'runs': 120, '4': 11, '6': 2, 'balls': 112, 'field': 0},
    {'name': 'Bhuvneshwar Kumar', 'role': 'bowl', 'wkts': 1, 'overs': 10, 'runs': 71, 'field': 1},
    {'name': 'Yuzvendra Chahal', 'role': 'bowl', 'wkts': 2, 'overs': 10, 'runs': 45, 'field': 0},
    {'name': 'Kuldeep Yadav', 'role': 'bowl', 'wkts': 3, 'overs': 10, 'runs': 34, 'field': 0}
]

print("Player Performance:")

for player in players:
    if player['role'] == 'bat':
        player['batscore'] = cricket_scoring.calculate_batting_points(player)
        print(f"{player['name']} (Batting Score): {player['batscore']}")
    elif player['role'] == 'bowl':
        player['bowlscore'] = cricket_scoring.calculate_bowling_points(player)
        print(f"{player['name']} (Bowling Score): {player['bowlscore']}")

# Determine the 'Man of the Match' based on total points
man_of_the_match = max(players, key=lambda x: x.get('batscore', 0) + x.get('bowlscore', 0))

print("\nMan of the Match:")
print(man_of_the_match['name'])
