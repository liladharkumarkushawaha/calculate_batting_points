# cricket_scoring.py

def calculate_batting_points(player):
    runs = player['runs']
    fours = player['4']
    sixes = player['6']
    balls_faced = player['balls']
    strike_rate = (runs / balls_faced) * 100

    batting_points = runs // 2
    if runs >= 50:
        batting_points += 5
    if runs >= 100:
        batting_points += 10
    if 80 <= strike_rate <= 100:
        batting_points += 2
    elif strike_rate > 100:
        batting_points += 4
    batting_points += (fours * 1) + (sixes * 2)

    return batting_points

def calculate_bowling_points(player):
    wickets = player['wkts']
    overs_bowled = player['overs']
    runs_given = player['runs']

    economy_rate = runs_given / overs_bowled

    bowling_points = (wickets * 10)
    if wickets >= 3:
        bowling_points += 5
    if wickets >= 5:
        bowling_points += 10
    if 3.5 <= economy_rate <= 4.5:
        bowling_points += 4
    elif 2 <= economy_rate < 3.5:
        bowling_points += 7
    elif economy_rate < 2:
        bowling_points += 10

    return bowling_points
