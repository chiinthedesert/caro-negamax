SIZE = 19

EMPTY = 0
BLACK = 1
WHITE = 2
WINNING_LENGTH = 5
WINNING_SCORE = 10**6
INF = 10**9

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

# số khoảng trống tối đa giữa các quân cờ cùng màu để được tính là một formation
MAX_GAPS = 1

# các mẫu hình (pattern) và điểm số tương ứng
PATTERNS = (
    (10000, ((1, 5, 0, 0),)),
    (700, ((1, 4, 0, 0),)),
    (700, ((2, 4, 1, 0),)),
    (700, ((2, 4, -1, 1),)),
    (700, ((1, 4, 1, 0), (1, 4, -1, 1))),
    (500, ((1, 4, 1, 0), (1, 3, 0, -1))),
    (500, ((1, 4, -1, 1), (1, 3, 0, -1))),
    (300, ((2, 3, 0, -1),)),
    (50, ((3, 2, 0, -1),)),
    (20, ((1, 3, 0, -1),)),
    (9, ((1, 2, 0, -1),)),
)
PATTERN_START_BY_LENGTH = (
    11,
    11,
    10,
    7,
    1,
    0,
)

THREATENING_SCORE = 300
