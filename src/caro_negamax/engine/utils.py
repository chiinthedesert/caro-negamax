from caro_negamax.constants import (
    BLACK,
    DIRECTIONS,
    EMPTY,
    INF,
    MOVE_OFFSETS,
    SIZE,
    WHITE,
    WINNING_LENGTH,
    WINNING_SCORE,
)


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
