def reading_matrix():
    rows = int(input())
    lst_of_lsts = [0]*rows
    for i in range(rows):
        lst_of_lsts[i] = list(map(int, input().split()))
    return rows, len(lst_of_lsts[0]), lst_of_lsts

if __name__ == '__main__':
    rows, cols, matrix = reading_matrix()
    matrix = [row for row in matrix if row]
        # if row is same as if len(row) > 0
    print(matrix)