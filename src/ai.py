import math

def get_available_moves(state_lines, boxes):
    possible = []

    for box in boxes.keys():
        edges = [
            (box[0], box[1]),
            (box[1], box[2]),
            (box[3], box[2]),
            (box[0], box[3])
        ]

        for e in edges:
            if e not in state_lines and (e[1], e[0]) not in state_lines:
                possible.append(e)

    return list(set(possible))


def score_state(state_lines, boxes):
    score = 0

    for b in boxes.keys():
        edges = [
            (b[0], b[1]),
            (b[1], b[2]),
            (b[3], b[2]),
            (b[0], b[3])
        ]

        if all(e in state_lines or (e[1], e[0]) in state_lines for e in edges):
            score += 1

    return score


def minimax(state_lines, boxes, depth, maximizing):
    if depth == 0:
        return score_state(state_lines, boxes), None

    available = get_available_moves(state_lines, boxes)

    if not available:
        return score_state(state_lines, boxes), None

    best_move = None

    if maximizing:
        max_eval = -math.inf

        for move in available:
            new_state = state_lines + [move]

            eval, _ = minimax(new_state, boxes, depth - 1, False)

            if eval > max_eval:
                max_eval = eval
                best_move = move

        return max_eval, best_move

    else:
        min_eval = math.inf

        for move in available:
            new_state = state_lines + [move]

            eval, _ = minimax(new_state, boxes, depth - 1, True)

            if eval < min_eval:
                min_eval = eval
                best_move = move

        return min_eval, best_move