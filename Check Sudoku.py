def check_sudoku(l):
    for i in range(0,9):
        if len(set(l[i]))!=9:
            return False
        c=[j[i] for j in l]
        if len(set(c))!=9:
            return False
    for i in range(0,9,3):
        for j in range(0,9,3):
            b=l[i][j:j+3]
            b.extend(l[i+1][j:j+3])
            b.extend(l[i+2][j:j+3])
            if len(set(b))!=9:
                return False
    return True
l=[[1,2,3,6,7,8,9,4,5],
   [5,8,4,2,3,9,7,6,1],
   [9,6,7,1,4,5,3,2,8],
   [3,7,2,4,6,1,5,8,9],
   [6,9,1,5,8,3,2,7,4],
   [4,5,8,7,9,2,6,1,3],
   [8,3,6,9,2,4,1,5,7],
   [2,1,9,8,5,7,4,3,6],
   [7,4,5,3,1,6,8,9,2]]
if check_sudoku(l):
    print("Sudoku is solved correctly.")
else:
    print("Sudoku is not solved correctly.")