## GitHub Actions & Yatzy Game Implementation

This folder contains the Python implementation of a simplified Yatzy game and a GitHub Actions workflow for automatic testing.

### Files:

- `yatzy.py`: the Yatzy class which has:
  - 5 dice (each individually lockable)
  - A roll method (rolls only unlocked dice)
  - Scoring methods: ones, twos, threes, fours, fives, sixes, one pair, tw pairs, three alike, four alike, small, large, full house, chance, yatzy

- `test_yatzy.py`: unit tests for all the scoring methods to ensure if everything works

- `.github/workflows/python-app.yml`: a GitHub Actions workflow file that:
  - runs automated tests whenever code is pushed
  - uses `pytest` to test the class and its methods

### Explanation:

This folder shows how continuous integration can be done using GitHub Actions. Once the Yatzy class and tests were written, a CI pipeline was set up using GitHub's built-in actions to ensure code quality.
