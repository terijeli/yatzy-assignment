## GitHub Actions & Yatzy Game Implementation

This folder contains the Python implementation of a simplified Yatzy game and a GitHub Actions workflow for automatic testing.

### Files:

- `yatzy.py`: The Yatzy class which includes:
  - 5 dice (each individually lockable)
  - A roll method that rolls only unlocked dice
  - Scoring methods: Ones, Twos, Threes, Fours, Fives, Sixes, OnePair, TwoPairs, ThreeAlike, FourAlike, Small, Large, FullHouse, Chance, Yatzy

- `test_yatzy.py`: Unit tests for all the scoring methods to ensure functionality.

- `.github/workflows/python-app.yml`: A GitHub Actions workflow file that:
  - Runs automated tests whenever code is pushed
  - Uses `pytest` to test the class and its methods

### Explanation:

This folder demonstrates how continuous integration is achieved using GitHub Actions. Once the Yatzy class and its tests were written, a CI pipeline was created using GitHub's built-in actions to ensure code quality. Every push triggers a test run.

### Screenshots:

- GitHub Actions page showing successful test run
- Test outputs in terminal
- Code snippets from `yatzy.py` and `test_yatzy.py`
