def read_matrix(lst_of_lsts):
    rows = int(input())
    assert rows > 0
    lst_of_lsts = [0]*rows

    for row in range(rows):
        lst_of_lsts[row] = list(map(int,input().split()))
        return rows, len(lst_of_lsts[0]), lst_of_lsts


def is_within_grid(r,c, rows, cols):
    return 0 <= r < rows and 0 <= c < cols


def get_neighbours(i, j, rows, cols, cnt=8):
    #   d, r, up, l, dr, dl, upr, upl
    di=[1, 0, -1, 0, 1, 1, -1, -1]
    dj=[0, 1, 0, -1, 1, -1, 1, -1]

    return [ (r,c) for idx in range(cnt)
            if is_within_grid(r:=i+di[idx], c:=j+dj[idx], rows, cols)]


if __name__ == '__main__':
    rows, cols, matrix = read_matrix()

    if rows == cols == 1:
        print(0, 0)
        exit(0)

    for r in range(rows):
        for c in range(cols):
            positions = get_neighbours(r, c, rows, cols)
            mx = max(matrix[i][j] for i, j in positions)
            if matrix[r][c] > mx:   #if the current cell value is greater than the max of all the neighbours
                print(r, c)         #then you are a mountain
                