import pytest
from three_musketeers import *

left = 'left'
right = 'right'
up = 'up'
down = 'down'
M = 'M'
R = 'R'
_ = '-'
poss_str = ['M', 'R', '-']

board1 =  [ [_, _, _, M, _],
            [_, _, R, M, _],
            [_, R, M, R, _],
            [_, R, _, _, _],
            [_, _, _, R, _] ]




def test_create_board():
    create_board()
    assert at((0,0)) == R
    assert at((0,4)) == M
    assert at((0,1)) == R
    assert at((0,2)) == R
    assert at((1,1)) == R
    assert at((2,1)) == R
    assert at((3,1)) == R
    assert at((4,1)) == R
    assert at((0,1)) == str(at((0,1)))
    for i in range(4):
        for j in range(4):
            assert at((i, j)) == str(at((i, j)))
    for i in range(4):
        for j in range(4):
            assert at((i, j)) in poss_str
    
    
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
    for item in get_board():
        for i in range(4):
            assert item[i] == str(item[i])
            
    for item in board1:
        for i in range(4):
            assert item[i] in poss_str
            
    for item in get_board():
        for i in range(4):
            assert item[i] in poss_str
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

    with pytest.raises(ValueError):
        location_to_string((6, 0))
    with pytest.raises(ValueError):
        location_to_string((2, 5))
    assert location_to_string((0, 0)) == ('A1')
    assert location_to_string((1, 1)) == ('B2')
    assert location_to_string((4, 4)) == ('D5')

def test_at():

    assert at((1, 2)) == 'R'
    assert at((0, 4)) == M
    with pytest.raises(ValueError):
        at((1,2)) == int(at((1,2)))
        
    with pytest.raises(ValueError):
        at((1,2)) == int(at((4,2)))
    

def test_all_locations():

    assert all_locations() == [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4),
                                (1, 0), (1, 1), (1, 2), (1, 3), (1, 4)
                                (2, 0), (2, 1), (2, 2), (2, 3), (2, 4),
                                (3, 0), (3, 1), (3, 2), (3, 3), (3, 4),
                                (4, 0), (4, 1), (4, 2), (4, 3), (4, 4)]


def test_adjacent_location():
    with pytest.raises(ValueError):
        for i in range(5):
            adjacent_location((0, i), 'right') != [0, i + 1]
    with pytest.raises(ValueError):
        for i in range(5):
            adjacent_location((i, 0), 'down') != [i + 1, 0]




def test_is_legal_move_by_musketeer():
    set_board(board1)
    assert is_legal_move_by_musketeer((0, 3), 'left') == False
    assert is_legal_move_by_musketeer((0, 3), 'down') == False
    assert is_legal_move_by_musketeer((1, 3), 'left') == True
    assert is_legal_move_by_musketeer((1, 3), 'right') == False
    assert is_legal_move_by_musketeer((2, 2), 'down') == False
    assert is_legal_move_by_musketeer((2, 2), 'down') == True

def test_is_legal_move_by_enemy():
    set_board(board1)
    assert is_legal_move_by_enemy((1, 2), 'left') == True
    assert is_legal_move_by_enemy((1, 2), 'right') == False
    assert is_legal_move_by_enemy((2, 1), 'left') == True
    assert is_legal_move_by_enemy((2, 3), 'right') == True
    assert is_legal_move_by_enemy((3, 1), 'up') == False
    assert is_legal_move_by_enemy((4, 3), 'down') == False

def test_is_legal_move():
    # Replace with tests
    set_board(board1)
   # with pytest.raises(ValueError):
   #     is_legal_move((2, 5), 'right')
   # with pytest.raises(ValueError):
   #     is_legal_move((6, 5), 'up')
    assert is_legal_move((0, 3), 'left') == False
    assert is_legal_move((0, 3), 'up') == False
    assert is_legal_move((1, 3), 'left') == True
    assert is_legal_move((1, 3), 'right') == False
    assert is_legal_move((4, 2), 'down') == False
    assert is_legal_move((2, 4), 'up') == False
    for i in range(4):
        for j in range(4):
            assert(type(is_legal_move((0, 0), 'left')), bool)

def test_can_move_piece_at():
    # Replace with tests
    set_board(board1)
    assert can_move_piece_at((0, 3)) == False
    assert can_move_piece_at((1, 2)) == False
    assert can_move_piece_at((1, 3)) == True
    assert can_move_piece_at((4, 3)) == False
    assert can_move_piece_at((3, 1)) == False

def test_has_some_legal_move_somewhere():
    set_board(board1)
    assert has_some_legal_move_somewhere('M') == True
    assert has_some_legal_move_somewhere('R') == True
    # Eventually put at least three additional tests here
    # with at least one additional board

def test_possible_moves_from():

    set_board(board1)
    assert possible_moves_from((0, 3)) == []
    assert possible_moves_from((1, 2)) == ['up', 'left']
    assert possible_moves_from((2, 1)) == ['up', 'left']
    assert possible_moves_from((3, 1)) == ['right', 'left', 'down']
    assert possible_moves_from((4, 3)) == ['up', 'left', 'right']
    assert possible_moves_from((2, 2)) == ['up', 'down', 'left', 'right']

def test_is_legal_location():
    assert is_legal_location((0, 0)) == True
    assert is_legal_location((-1, 0)) == False
    assert is_legal_location((3, 2)) == True
    assert is_legal_location((2, 4)) == True
    assert is_legal_location((1, 2)) == True
    assert is_legal_location((5, 3)) == False
    assert is_legal_location((7, 3)) == False
    assert is_legal_location((2, 8)) == False


def test_is_within_board():

    assert is_within_board((0, 0)) == True
    assert is_within_board((3, 2)) == True
    assert is_within_board((2, 4)) == True
    assert is_within_board((1, 2)) == True
    assert is_within_board((-1, 0)) == False
    assert is_within_board((5, 3)) == False
    assert is_within_board((7, 3)) == False
    assert is_within_board((2, 8)) == False

def test_all_possible_moves_for():

    set_board(board1)
    assert all_possible_moves_for('M') == ([(1, 2), 'left'], [(2, 3), 'down'], [(2, 3), 'right'],
    [(2, 1), 'left'], [(1, 2), 'up'],)

    assert all_possible_moves_for('R') == ([(0, 2), 'up'], [(1, 1), 'left'], [(1, 1), 'up'],
    [(2, 0), 'left'], [(2, 4), 'right'], [(3, 0), 'left'], [(3, 2), 'right'], [(3, 3), 'up'],
    [(3, 3), 'down'], [(4, 1), 'down'], [(4, 2), 'left'], [(4, 4), 'right'],)

def test_make_move():
    # Replace with tests
    assert make_move(location, direction) # TODO


def test_choose_computer_move():
    # Replace with tests; should work for both 'M' and 'R'
    with pytest.raises(ValueError):
        assert choose_computer_move('M') not in all_possible_moves_for('M')
    with pytest.raises(ValueError):
        assert choose_computer_move('M') not in all_possible_moves_for('M')
    assert choose_computer_move('M') in all_possible_moves_for('M')
    assert choose_computer_move('R') in all_possible_moves_for('R')

def test_is_enemy_win():
    # Replace with tests
    assert is_enemy_win() == True or is_enemy_win() == False
