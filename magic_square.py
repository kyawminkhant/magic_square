"""
Magic Square Generator (3x3)

Generates a 3x3 magic square using randomised permutations and
constraint-based rejection. A valid magic square satisfies:
- Uses numbers 1–9 exactly once
- All rows, columns, and diagonals sum to 15

This implementation is brute-force and intended for learning purposes.
"""

import random


total=15
maxAttempts=100_000


def rows_valid(square):
    return all(sum(square[i:i+3])==total for i in range(0, 9, 3))


def columns_valid(square):
    return all(sum(square[i::3])==total for i in range(3))


def diagonals_valid(square):
    return (
        square[0]+square[4]+square[8]==total and
        square[2]+square[4]+square[6]==total
    )


def main():
    generated_lists=[]
    dumb_rows=[]
    dumb_columns=[]
    dumb_diagonals=[]

    count=0

    while True:
        count+=1
        if count>maxAttempts:
            raise RuntimeError("Search space exhausted")

        square=[1, 2, 3, 4, 5, 6, 7, 8, 9]

        # Generate a unique permutation
        while True:
            random.shuffle(square)

            temp_diagonal=[
                square[0], square[2], square[4],
                square[6], square[8]
            ]

            if square in generated_lists:
                continue
            elif (
                square[0:3] in dumb_rows or
                square[3:6] in dumb_rows or
                square[6:9] in dumb_rows
            ):
                continue
            elif (
                square[0:7:3] in dumb_columns or
                square[1:8:3] in dumb_columns or
                square[2:9:3] in dumb_columns
            ):
                continue
            elif temp_diagonal in dumb_diagonals:
                continue
            else:
                generated_lists.append(square.copy())
                break

        # Check rows
        if not rows_valid(square):
            for i in range(0, 9, 3):
                if sum(square[i:i+3])!=total:
                    dumb_rows.append(square[i:i+3].copy())
            continue

        # Check columns
        if not columns_valid(square):
            for i in range(3):
                column=square[i::3]
                if sum(column)!=total:
                    dumb_columns.append(column.copy())
            continue

        # Check diagonals
        if not diagonals_valid(square):
            dumb_diagonals.append(temp_diagonal.copy())
            continue

        # Valid magic square found
        break

    # Output result
    print("Magic Square:\n")
    print(square[0:3])
    print(square[3:6])
    print(square[6:9])
    print(f"\nAttempts: {count}")


if __name__ == "__main__":
    main()