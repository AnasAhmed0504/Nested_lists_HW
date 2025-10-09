

if __name__ == '__main__':
    rows, cols, matrix = read_matrix_strings()
    
    #for each column, get all words, compute their word length, get max of all 
    width_per_col = [max(len(str(value)) for value in col) for col in zip(*matrix)]

    #for each word in a row, just based on its column max width
    # then join all of them by '#'
    # logic--> for every row transform row then merge 
    matrix = ['#'.join([word.ljust(width_per_col[idx]) for idx, word in enumerate(row)]) for row in matrix]
    print('\n'.join(matrix))    #print rows in separated newline

