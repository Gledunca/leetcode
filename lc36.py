class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen = set()
        for i in range(len(board)):
            for j in range(len(board[0])):
                num = board[i][j]
                if num == ".":
                    continue
                if f"{num} row {i}" not in seen:
                    seen.add(f"{num} row {i}")
                else:
                    return False
                if f"{num} col {j}" not in seen:
                    seen.add(f"{num} col {j}")
                else:
                    return False
                if f"{num} box {(i // 3, j // 3)}" not in seen:
                    seen.add(f"{num} box {(i // 3, j // 3)}")
                else:
                    return False
        return True