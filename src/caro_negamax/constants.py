SIZE = 20

EMPTY = 0
BLACK = 1
WHITE = 2
WINNING_LENGTH = 5
WINNING_SCORE = 1000000

DIRECTIONS = (
    (0, 1),  # ngang
    (1, 0),  # dọc
    (1, 1),  # chéo xuống phải
    (1, -1),  # chéo xuống trái
)

CANDIDATE_RADIUS = 2
MOVE_OFFSETS = tuple(
    (dr, dc)
    for dr in range(-CANDIDATE_RADIUS, CANDIDATE_RADIUS + 1)
    for dc in range(-CANDIDATE_RADIUS, CANDIDATE_RADIUS + 1)
    if not (dr == 0 and dc == 0)
)
