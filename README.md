# magic_square

# Magic Square Generator (Python)

This project generates a 3×3 magic square using randomised
permutations and constraint-based rejection.

## Rules
- Uses numbers 1–9 exactly once
- All rows, columns, and diagonals sum to 15

## Approach
- Random shuffle
- Reject invalid rows, columns, diagonals
- Tracks failed patterns to reduce repetition

## Run
```bash
python main.py
