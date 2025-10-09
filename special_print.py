def read_matrix():
    rows = int(input())
    assert rows > 0
    lst_of_lsts = [0]*rows

    for row in range(rows):
        lst_of_lsts = list(map(int,input().split()))
        return rows, len(lst_of_lsts), lst_of_lsts
    


if __name__ == '__main__':
    rows, cols, matrix = read_matrix()
    
    last_row = sum(matrix[-1])
    last_col = sum([row[-1] for row in matrix])
    right_diag = sum([row(-(idx+1))] for idx, row in enumerate(matrix))
    left_diag = sum([row[idx] for idx, row in enumerate(matrix)])

    print(last_row, last_col)
    print(right_diag, left_diag)