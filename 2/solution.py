with open("input.txt", "r") as input_file:
    input = input_file.read().rstrip()

data = [round.split(" ") for round in input.split("\n")]

loses_to = {
    "rock": "scissors",
    "paper": "rock",
    "scissors": "paper",
}

wins_against = {}
wins_against.update([reversed(mapping) for mapping in loses_to.items()])

shape_score = {
    "rock": 1,
    "paper": 2,
    "scissors": 3,
}


def part1(data):
    letter_shape = {
        "A": "rock",
        "B": "paper",
        "C": "scissors",
        "X": "rock",
        "Y": "paper",
        "Z": "scissors",
    }

    data = [(letter_shape[round[0]], letter_shape[round[1]]) for round in data]

    score = 0
    for round in data:
        them = round[0]
        you = round[1]

        score += shape_score[you]
        if you == them:
            score += 3
        elif them == loses_to[you]:
            score += 6
    return score


def part2(data):
    letter_shape = {
        "A": "rock",
        "B": "paper",
        "C": "scissors",
    }

    outcome_code = {
        "X": "lose",
        "Y": "draw",
        "Z": "win",
    }

    data = [(letter_shape[round[0]], outcome_code[round[1]]) for round in data]

    outcome_points = {
        "lose": 0,
        "draw": 3,
        "win": 6,
    }

    score = 0
    for round in data:
        score += outcome_points[round[1]]
        if round[1] == "draw":
            score += shape_score[round[0]]
        elif round[1] == "lose":
            score += shape_score[loses_to[round[0]]]
        else:
            score += shape_score[wins_against[round[0]]]
    return score


print("Part 1:", part1(data))
print("Part 2:", part2(data))
