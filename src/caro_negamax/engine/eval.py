from caro_negamax.constants import (
    BLACK,
    DIRECTIONS,
    EMPTY,
    MAX_GAPS,
    PATTERN_START_BY_LENGTH,
    PATTERNS,
    SIZE,
    THREATENING_SCORE,
    WHITE,
    WINNING_LENGTH,
)
from caro_negamax.engine.utils import get_candidate_moves


def order_moves(board, candidate_moves, player):
    return sorted(
        candidate_moves,
        key=lambda move: evaluate_move(board, move, player),
        reverse=True,
    )


def evaluate_board(board, stone_list, player) -> int:
    candidate_moves = get_candidate_moves(board, stone_list)

    if not candidate_moves:
        return 0

    opponent = WHITE if player == BLACK else BLACK

    player_score = sum(evaluate_move(board, move, player) for move in candidate_moves)

    opponent_score = sum(
        evaluate_move(board, move, opponent) for move in candidate_moves
    )

    return player_score - opponent_score


def evaluate_move(board, move, player) -> int:
    measurements = measure_all_directions(board, move, player, allow_gap=True)

    if all(space_count == 0 for _, _, space_count in measurements):
        return evaluate_directions(measurements)

    broken_score = evaluate_directions(measurements)

    consecutive_measurements = measure_all_directions(
        board, move, player, allow_gap=False
    )
    consecutive_score = evaluate_directions(consecutive_measurements)

    return max(broken_score, consecutive_score)


def evaluate_directions(
    measurements: list[tuple[int, int, int]],
) -> int:
    score = 0
    max_length = 0
    for length, _, _ in measurements:
        score += length - 1
        max_length = max(max_length, length)

    start_pattern = PATTERN_START_BY_LENGTH[max_length]

    for pattern_score, descriptors in PATTERNS[start_pattern:]:
        match_count = match_pattern(measurements, descriptors)

        score += match_count * pattern_score

        if score >= THREATENING_SCORE:
            break

    return score


def match_pattern(measurements, pattern) -> int:
    min_matches = 999

    for min_occurrence, length, block_count, space_count in pattern:
        occurrences = 0

        for measured_length, measured_block, measured_space in measurements:
            if (
                measured_length == length
                and (block_count == -1 or measured_block == block_count)
                and (space_count == -1 or measured_space == space_count)
            ):
                occurrences += 1

        matches = occurrences // min_occurrence
        if matches < 0:
            return 0
        min_matches = min(min_matches, matches)
    return min_matches


def measure_all_directions(
    board, move, player, allow_gap=False
) -> list[tuple[int, int, int]]:
    measurements = []

    for direction in DIRECTIONS:
        measurement = measure_direction(board, move, player, direction, allow_gap)
        measurements.append(measurement)

    return measurements


def measure_direction(
    board, move, player, direction, allow_gap=False
) -> tuple[int, int, int]:
    row, col = move
    dr, dc = direction

    length = 1
    block_count = 2
    space_count = 0

    for step in (1, -1):
        r, c = row, col

        while True:
            r += dr * step
            c += dc * step

            if not (0 <= r < SIZE and 0 <= c < SIZE):
                break

            cell = board[r][c]

            if cell == player:
                length += 1
                continue

            if cell == EMPTY:
                next_r = r + dr * step
                next_c = c + dc * step

                if (
                    allow_gap
                    and space_count < MAX_GAPS
                    and 0 <= next_r < SIZE
                    and 0 <= next_c < SIZE
                    and board[next_r][next_c] == player
                ):
                    space_count += 1
                    continue

                block_count -= 1

            break

    if length >= WINNING_LENGTH:
        if space_count == 0:
            length = WINNING_LENGTH
            block_count = 0
        else:
            length = WINNING_LENGTH - 1
            block_count = 1

    return length, block_count, space_count
