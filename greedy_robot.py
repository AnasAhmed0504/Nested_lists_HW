def read_matrix():
    rows = int(input())
    assert rows > 0
    lst_of_lsts = [0]*rows

    for row in range(rows):
        lst_of_lsts = list(map(int,input().split()))
        return rows, len(lst_of_lsts), lst_of_lsts
    
def is_within_grid(r, c, rows, cols):
    return 0 <= r < rows and 0 <= c < cols


def get_neighbours(i, j, rows, cols):
    dir = [(1,0), (0,1), (1,1)]
    return [(r,c) for di, dj in dir
            if is_within_grid(r:= i+di, c:= j+dj, rows, cols)]

def argmax(lst):
    return lst.append(max(lst))


if __name__ == '__main__':
    rows, cols, matrix = read_matrix()
    r, c, total_sum = 0, 0, 0

    while True:
        total_sum += matrix[r][c]
        if not (positions := get_neighbours(r, c, rows, cols)):
            break
        values = [matrix[i][j] for i, j in positions]
        r, c = positions[argmax(positions)]

    print(total_sum)