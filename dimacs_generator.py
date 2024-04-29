import argparse

def queens(n):
    rows = horizontal(n) + vertical(n) + diagonal(n)
    with open(f"queens_{n}.cnf", "w") as f:
        f.write(f"p cnf {n*n} {len(rows)}\n")
        for row in rows:
            f.write(" ".join(map(str, row)) + " 0\n")


def horizontal(n):
    result = []
    for i in range(n):
        next_row = [i*n + j for j in range(1, n+1)]
        result.append(next_row)

        for a in range(len(next_row)):
            for b in range(a+1, len(next_row)):
                result.append([-next_row[a], -next_row[b]])

    return result

def vertical(n):
    result = []
    for i in range(1, n+1):
        next_row = [i + j * n for j in range(0, n)]
        result.append(next_row)

        for a in range(len(next_row)):
            for b in range(a + 1, len(next_row)):
                result.append([-next_row[a], -next_row[b]])

    return result

def diagonal(n):
    result = []
    for i in range(1, pow(n, 2) + 1):
        if i % n == 0:
            continue
        for j in range(i + n + 1, pow(n, 2) + 1, n+1):
            result.append([-i, -j])

    for i in range(2, pow(n, 2)):
        if i % n == 1:
            continue
        for j in range(i + n - 1, pow(n, 2) + 1, n-1):
            result.append([-i, -j])
            if j % n == 1:
                break

    return result

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
            prog='DIMACS generator',
            description='Generates a DIMACS file for the n-queens problem'
        )
        
    parser.add_argument('amount', type=int, help='the amount of queens placed on the board')
    args = parser.parse_args()
    queens(args.amount)
