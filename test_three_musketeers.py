import pytest
from three_musketeers import *

left = 'left'
right = 'right'
up = 'up'
down = 'down'
M = 'M'
R = 'R'
_ = '-'

board1 =  [ [_, _, _, M, _],
            [_, _, R, M, _],
            [_, R, M, R, _],
            [_, R, _, _, _],
            [_, _, _, R, _] ]

def test_create_board():
    create_board()
    assert at((0,0)) == R
    assert at((0,4)) == M
    #eventually add at least two more test cases

def test_set_board():
    set_board(board1)
    assert at((0,0)) == _
    assert at((1,2)) == R
    assert at((1,3)) == M
    #eventually add some board2 and at least 3 tests with it

def test_get_board():
    set_board(board1)
    assert board1 == get_board()
    #eventually add at least one more test with another board

def test_string_to_location():
    with pytest.raises(ValueError):
        string_to_location('X3')
    with pytest.raises(ValueError):
        string_to_location('F1')
    with pytest.raises(ValueError):
        string_to_location('A6')
    assert string_to_location('A1') == (0, 0)
    assert string_to_location('E2') == (4, 1)
    assert string_to_location('C4') == (2, 3)
    #eventually add at least one more exception test and two more
    #test with correct inputs

def test_location_to_string():
    # Replace with tests
    with pytest.raises(ValueError):
        location_to_string((6, 0))
    with pytest.raises(ValueError):
        location_to_string((2, 5))
    assert location_to_string((0, 0)) == ('A1')
    assert location_to_string((1, 1)) == ('B2')
    assert location_to_string((4, 4)) == ('D5')

def test_at():
    # Replace with tests
    assert at((1, 2)) == 'R'
    assert at((1, 3)) == M

def test_all_locations():
    # Replace with tests
    assert all_locations() == [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4),
                                (1, 0), (1, 1), (1, 2), (1, 3), (1, 4)
                                (2, 0), (2, 1), (2, 2), (2, 3), (2, 4),
                                (3, 0), (3, 1), (3, 2), (3, 3), (3, 4),
                                (4, 0), (4, 1), (4, 2), (4, 3), (4, 4)]

def test_adjacent_location():
    # Replace with tests

def test_is_legal_move_by_musketeer():
    # Replace with tests

def test_is_legal_move_by_enemy():
    # Replace with tests

def test_is_legal_move():
    # Replace with tests

def test_can_move_piece_at():
    # Replace with tests

def test_has_some_legal_move_somewhere():
    set_board(board1)
    assert has_some_legal_move_somewhere('M') == True
    assert has_some_legal_move_somewhere('R') == True
    # Eventually put at least three additional tests here
    # with at least one additional board

def test_possible_moves_from():
    # Replace with tests

def test_is_legal_location():
    # Replace with tests

def test_is_within_board():
    # Replace with tests

def test_all_possible_moves_for():
    # Replace with tests

def test_make_move():
    # Replace with tests

def test_choose_computer_move():
    # Replace with tests; should work for both 'M' and 'R'

def test_is_enemy_win():
    # Replace with tests
