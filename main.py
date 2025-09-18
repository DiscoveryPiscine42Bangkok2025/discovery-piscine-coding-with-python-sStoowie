from checkmate import checkmate

def main():
    print("Example 1:")
    board1 = """\
R...
.K..
..P.
....\
"""
    checkmate(board1)

    print("Example 2:")
    board2 = """\
..
.K\
"""
    checkmate(board2)

if __name__ == "__main__":
    main()