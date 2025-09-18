def checkmate(board_str):
    # แยกบรรทัด
    rows = board_str.splitlines()
    size = len(rows)

    # หาตำแหน่ง K
    king_x = -1
    king_y = -1
    for i in range(size):
        if "K" in rows[i]:
            king_x = i
            king_y = rows[i].index("K")
            break

    if king_x == -1:
        print("Fail")
        return

    # -------- Pawn --------
    if king_x + 1 < size:
        if king_y - 1 >= 0 and rows[king_x + 1][king_y - 1] == "P":
            print("Success")
            return
        if king_y + 1 < size and rows[king_x + 1][king_y + 1] == "P":
            print("Success")
            return

    # -------- Bishop / Queen --------
    steps = [(-1,-1), (-1,1), (1,-1), (1,1)]
    for dx, dy in steps:
        x = king_x
        y = king_y
        while True:
            x += dx
            y += dy
            if x < 0 or y < 0 or x >= size or y >= len(rows[x]):
                break
            if rows[x][y] != ".":
                if rows[x][y] in ["B", "Q"]:
                    print("Success")
                    return
                break

    # -------- Rook / Queen --------
    steps = [(-1,0), (1,0), (0,-1), (0,1)]
    for dx, dy in steps:
        x = king_x
        y = king_y
        while True:
            x += dx
            y += dy
            if x < 0 or y < 0 or x >= size or y >= len(rows[x]):
                break
            if rows[x][y] != ".":
                if rows[x][y] in ["R", "Q"]:
                    print("Success")
                    return
                break

    print("Fail")