# Caro Negamax

> Bài tập nhóm — **đang trong quá trình hoàn thiện**.

Cờ Caro AI sử dụng thuật toán **Negamax kết hợp cắt tỉa Alpha-Beta**.
Mục tiêu của đề tài là tìm hiểu thuật toán trí tuệ nhân tạo trong game đối kháng 2 người.

## Tính năng hiện có

- Bàn cờ 19x19, thắng khi có 5 quân liên tiếp (ngang, dọc, 2 đường chéo).
- Chỉ sinh các nước ứng viên trong bán kính 2 quanh những quân đã đánh (giảm số node cần duyệt).
- **Hàm đánh giá theo mẫu hình (pattern)**: nhận diện 4 quân, 3 quân, thế bị chặn 1 đầu / 2 đầu, mẫu có khoảng trống.
- **Negamax + Alpha-Beta pruning**, có sắp xếp nước đi (move ordering) để tăng hiệu quả cắt tỉa.

## Trạng thái dự án

| Hạng mục | Trạng thái |
| --- | --- |
| Engine (sinh nước, luật thắng, undo) | Hoàn thành |
| Hàm đánh giá theo pattern | Hoàn thành (bản cơ bản) |
| Negamax + Alpha-Beta | Hoàn thành (bản cơ bản) |
| Giao diện pygame-ce | Đang phát triển |
| Kết nối AI với giao diện | Chưa bắt đầu |
| Kiểm thử tự động | Chưa bắt đầu |
| Báo cáo / slide | Chưa bắt đầu |

## Cấu trúc thư mục

```text
caro-negamax/
├── pyproject.toml
├── uv.lock
└── src/
    └── caro_negamax/
        ├── main.py          # điểm khởi chạy
        ├── constants.py     # hằng số, pattern, điểm số
        ├── engine/
        │   ├── utils.py     # tạo bàn cờ, kiểm tra thắng, sinh nước, đánh/undo
        │   ├── eval.py      # đo hướng, so khớp pattern, chấm điểm
        │   └── search.py    # negamax + alpha-beta
        └── gui/             # giao diện (đang phát triển)
```

## Cách AI hoạt động (tóm tắt)

1. `get_candidate_moves` — chỉ lấy các ô trống gần quân đã đánh, tránh duyệt toàn bộ 400 ô.
2. `order_moves` — sắp xếp nước theo điểm đánh giá giảm dần, giúp Alpha-Beta cắt nhánh sớm.
3. `negamax` — duyệt với độ sâu `depth`, dừng khi gặp thế thắng hoặc hết độ sâu.
4. `get_best_move` — trả về nước đi tốt nhất, điểm số và số node đã duyệt.

Ví dụ gọi engine trực tiếp:

```python
from caro_negamax.constants import BLACK
from caro_negamax.engine.search import get_best_move
from caro_negamax.engine.utils import create_board

board = create_board()
stones = []

move, score, nodes = get_best_move(board, stones, BLACK, depth=3)
print(move, score, nodes)
```

## Lộ trình

- [x] Engine: bàn cờ, kiểm tra thắng, sinh nước ứng viên, undo
- [x] Hàm đánh giá theo mẫu hình
- [x] Negamax + cắt tỉa Alpha-Beta
- [ ] Tối ưu thuật toán
- [ ] Giao diện đồ họa bằng pygame-ce
- [ ] Chế độ Người vs Máy
- [ ] Hiển thị điểm đánh giá và số node đã duyệt
- [ ] Kiểm thử và đo hiệu năng
- [ ] Báo cáo và slide thuyết trình

## Ghi chú

README này sẽ được cập nhật tiếp trong quá trình làm đồ án.

## Yêu cầu
- Python **3.14+**
- [uv](https://docs.astral.sh/uv/) để quản lý dependency

## Cài đặt nhanh để phát triển
1. Cài đặt uv theo hướng dẫn trên trang chủ
2. Clone repo và cài đặt dependency
```bash
git clone <link-repo>
cd caro-negamax
uv sync
```
