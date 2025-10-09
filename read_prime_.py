def read_matrix():
    rows = int(input())
    assert rows > 0
    lst_of_lsts = [0]*rows

    for row in range(rows):
        lst_of_lsts = list(map(int,input().split()))
        return rows, len(lst_of_lsts), lst_of_lsts
    
def is_prime(num):
    if num <= 1:
        return 0
    for i in range(2, num):
        if num % i == 0:
            return 0

    return 1    


    
if __name__ == '__main__':
    rows, cols, matrix = read_matrix()

    # replace each value with 1 if prime zero , otherwise
    #then with each query, we don't have to keep computing the slow prime
    is_prime_matrix = [[is_prime[value] for value in row] for row in matrix]

    q  = int(input())

    while q>0:
        total_primes = 0
        sr, sc, nr, nc = map(int, input().split)
        #iterate on rows: slice the range and sum it
        for r in range(sr, sr +nr):
            total_primes += sum(is_prime_matrix[r][sc:sc + nc])
        print(total_primes)
        q -= 1