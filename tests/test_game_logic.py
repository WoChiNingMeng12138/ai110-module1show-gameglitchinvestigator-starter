import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from logic_utils import check_guess


# --- outcome correctness ---

def test_winning_guess():
    outcome, _ = check_guess(50, 50)
    assert outcome == "Win"

def test_guess_too_high():
    outcome, _ = check_guess(60, 50)
    assert outcome == "Too High"

def test_guess_too_low():
    outcome, _ = check_guess(40, 50)
    assert outcome == "Too Low"


# --- message content ---

def test_win_message():
    _, message = check_guess(50, 50)
    assert "Correct" in message

def test_too_high_message():
    _, message = check_guess(60, 50)
    assert "LOWER" in message

def test_too_low_message():
    _, message = check_guess(40, 50)
    assert "HIGHER" in message


# --- boundary values ---

def test_guess_one_above_secret():
    outcome, _ = check_guess(51, 50)
    assert outcome == "Too High"

def test_guess_one_below_secret():
    outcome, _ = check_guess(49, 50)
    assert outcome == "Too Low"

def test_secret_at_range_minimum():
    outcome, _ = check_guess(1, 1)
    assert outcome == "Win"

def test_secret_at_range_maximum():
    outcome, _ = check_guess(200, 200)
    assert outcome == "Win"

def test_guess_below_range_minimum():
    # Guessing 0 when secret is 1 — still Too Low, not a crash
    outcome, _ = check_guess(0, 1)
    assert outcome == "Too Low"

def test_guess_above_range_maximum():
    # Guessing beyond max — still Too High
    outcome, _ = check_guess(201, 200)
    assert outcome == "Too High"


# --- return type ---

def test_returns_tuple_of_two():
    result = check_guess(50, 50)
    assert isinstance(result, tuple)
    assert len(result) == 2

def test_outcome_is_string():
    outcome, _ = check_guess(50, 50)
    assert isinstance(outcome, str)

def test_message_is_string():
    _, message = check_guess(50, 50)
    assert isinstance(message, str)
