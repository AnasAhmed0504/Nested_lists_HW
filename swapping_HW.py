def read_matrix():
    rows = int(input('enter number of rows: '))
    assert rows > 0
    lst_of_lsts = [0] *rows
    
    for row in range(rows):
        lst_of_lsts[row] = list(map(int, input('enter: ').split()))
    return rows, len(lst_of_lsts[0]), lst_of_lsts

if __name__ == '__main__':
    rows, cols, matrix = read_matrix()
    c1, c2 = map(int, input('enter two columns to swap: ').split())

    for row in matrix:
        row[c1], row[c2] = row[c2], row[c1]
    
    print(matrix)