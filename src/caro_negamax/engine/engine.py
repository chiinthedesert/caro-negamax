from caro_negamax.constants import (
    BLACK,
    DIRECTIONS,
    EMPTY,
    MOVE_OFFSETS,
    SIZE,
    WHITE,
    WINNING_LENGTH,
    WINNING_SCORE,
)


def get_best_move(board, stone_list, player, depth):
    candidate_moves = get_candidate_moves(board, stone_list)

    if not candidate_moves:
        return None, None, 0

    candidate_moves = order_moves(board, candidate_moves, player)

    best_move = None
    best_score = float("-inf")
    nodes_searched = 0

    opponent = WHITE if player == BLACK else BLACK

    alpha = float("-inf")
    beta = float("inf")

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

    if depth == 0:
        return evaluate_board(board, stone_list, player), 1

    candidate_moves = get_candidate_moves(board, stone_list)
    if not candidate_moves:
        return 0, 1
    candidate_moves = order_moves(board, candidate_moves, player)

    best_score = float("-inf")
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


def order_moves(board, candidate_moves, player): ...


def evaluate_board(board, stone_list, player): ...


def create_board():
    return [[EMPTY] * SIZE for _ in range(SIZE)]


def check_win(board, last_move) -> bool:
    row, col = last_move
    player = board[row][col]

    for dr, dc in DIRECTIONS:
        count = 1

        # kiểm tra theo hướng dương
        r, c = row + dr, col + dc
        while 0 <= r < SIZE and 0 <= c < SIZE and board[r][c] == player:
            count += 1
            r += dr
            c += dc

        # kiểm tra theo hướng âm
        r, c = row - dr, col - dc
        while 0 <= r < SIZE and 0 <= c < SIZE and board[r][c] == player:
            count += 1
            r -= dr
            c -= dc

        if count >= WINNING_LENGTH:
            return True
    return False


def get_candidate_moves(board, stone_list) -> list[tuple[int, int]]:
    candidate_moves = set()
    if not stone_list:
        return [(SIZE // 2, SIZE // 2)]
    for row, col in stone_list:
        for dr, dc in MOVE_OFFSETS:
            r, c = row + dr, col + dc
            if 0 <= r < SIZE and 0 <= c < SIZE and board[r][c] == EMPTY:
                candidate_moves.add((r, c))
    return list(candidate_moves)


def make_move(board, stone_list, move, player):
    row, col = move
    if not (0 <= row < SIZE and 0 <= col < SIZE):
        raise ValueError("vị trí không hợp lệ")

    if board[row][col] != EMPTY:
        raise ValueError("vị trí đã có quân cờ")
    board[row][col] = player
    stone_list.append(move)


def undo_move(board, stone_list):
    row, col = stone_list.pop()
    board[row][col] = EMPTY
