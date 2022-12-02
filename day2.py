opponent_moves = {
    "A": "rock",
    "B": "paper",
    "C": "scissors"
}

player_moves = {
    "X": "rock",
    "Y": "paper",
    "Z": "scissors"
}


def parse_data(data):
    return data.split(" ")


def result_duel(moves):
    points = 0
    opponent, player, *rest = moves
    points += list(player_moves).index(player) + 1
    opponent_move = opponent_moves.get(opponent)
    player_move = player_moves.get(player)
    match player_move, opponent_move:
        case "rock", "scissors":
            points += 6
        case "paper", "rock":
            points += 6
        case "scissors", "paper":
            points += 6
    if player_move == opponent_move:
        points += 3
    return points


def calculate_score():
    score = 0
    file = open("day2.txt", "r")
    data = list(map(parse_data, file.read().splitlines()))
    for duel_data in data:
        score += result_duel(duel_data)
    print(score)


calculate_score()
