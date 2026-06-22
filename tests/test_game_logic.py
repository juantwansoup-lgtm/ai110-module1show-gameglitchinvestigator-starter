from logic_utils import check_guess, new_game_state


def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    outcome, message = check_guess(50, 50)
    assert outcome == "Win"


def test_guess_too_high():
    # Guess above the secret -> outcome "Too High"
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"


def test_guess_too_low():
    # Guess below the secret -> outcome "Too Low"
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"


def test_too_high_hint_tells_player_to_go_lower():
    # Bug regression: when the guess is too high, the hint must tell the
    # player to go LOWER (the original code told them to go HIGHER).
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"
    assert "LOWER" in message
    assert "HIGHER" not in message


def test_too_low_hint_tells_player_to_go_higher():
    # Bug regression: when the guess is too low, the hint must tell the
    # player to go HIGHER (the original code told them to go LOWER).
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"
    assert "HIGHER" in message
    assert "LOWER" not in message


def test_new_game_starts_with_full_attempts():
    # Bug regression: starting a new game must reset attempts to 0 so the
    # player gets their full allotment of attempts again.
    state = new_game_state(secret=42)
    assert state["attempts"] == 0


def test_new_game_resets_status_to_playing():
    # Bug regression: the original New Game handler left "status" untouched,
    # so after a win/loss the game stayed over and a new game never started.
    state = new_game_state(secret=42)
    assert state["status"] == "playing"


def test_new_game_clears_history_and_score():
    # A fresh game must start from a clean slate, not carry over the
    # previous game's guesses or score.
    state = new_game_state(secret=42)
    assert state["history"] == []
    assert state["score"] == 0
    assert state["secret"] == 42
