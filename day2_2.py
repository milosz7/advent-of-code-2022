opponent_moves = {
    "A": "rock",
    "B": "paper",
    "C": "scissors"
}

losing_score_if_opponent_played = {
    "paper": 1,
    "scissors": 2,
    "rock": 3,
}

draw_score_if_opponent_played = {
    "rock": 1,
    "paper": 2,
    "scissors": 3
}

winning_score_if_opponent_played = {
    "scissors": 1,
    "rock": 2,
    "paper": 3
}


def parse_data(data):
    return data.split(" ")


def result_duel(moves):
    points = 0
    opponent, player, *rest = moves
    opponent_move = opponent_moves.get(opponent)
    player_move = player
    match player_move:
        case "X":
            points += losing_score_if_opponent_played.get(opponent_move)
        case "Y":
            points += (draw_score_if_opponent_played.get(opponent_move) + 3)
        case "Z":
            points += (winning_score_if_opponent_played.get(opponent_move) + 6)
    return points


def calculate_score():
    score = 0
    file = open("day2.txt", "r")
    data = list(map(parse_data, file.read().splitlines()))
    for duel_data in data:
        score += result_duel(duel_data)
    print(score)


calculate_score()
