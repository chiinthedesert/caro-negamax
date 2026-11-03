from caro_negamax.constants import (
    BLACK,
    INF,
    WHITE,
    WINNING_SCORE,
)
from caro_negamax.engine.eval import evaluate_board, order_moves
from caro_negamax.engine.utils import (
    check_win,
    get_candidate_moves,
    make_move,
    undo_move,
)


def get_best_move(board, stone_list, player, depth):
    candidate_moves = get_candidate_moves(board, stone_list)

    if not candidate_moves:
        return None, None, 0

    candidate_moves = order_moves(board, candidate_moves, player)

    best_move = None
    best_score = -INF
    nodes_searched = 0

    opponent = WHITE if player == BLACK else BLACK

    alpha = -INF
    beta = INF

    for move in candidate_moves:
        make_move(board, stone_list, move, player)

        score, nodes = negamax(board, stone_list, depth - 1, opponent, -beta, -alpha)

        undo_move(board, stone_list)

        score = -score
        nodes_searched += nodes

        if score > best_score:
            best_score = score
            best_move = move

        alpha = max(alpha, score)

    return best_move, best_score, nodes_searched


def negamax(board, stone_list, depth, player, alpha, beta):
    last_move = stone_list[-1]

    if check_win(board, last_move):
        return -WINNING_SCORE, 1

    if depth <= 0:
        return evaluate_board(board, stone_list, player), 1

    candidate_moves = get_candidate_moves(board, stone_list)
    if not candidate_moves:
        return 0, 1
    candidate_moves = order_moves(board, candidate_moves, player)

    best_score = -INF
    nodes_searched = 1
    opponent = WHITE if player == BLACK else BLACK

    for move in candidate_moves:
        make_move(board, stone_list, move, player)

        score, nodes = negamax(board, stone_list, depth - 1, opponent, -beta, -alpha)

        undo_move(board, stone_list)

        score = -score
        nodes_searched += nodes

        best_score = max(best_score, score)

        alpha = max(alpha, score)
        if alpha >= beta:
            break

    return best_score, nodes_searched
