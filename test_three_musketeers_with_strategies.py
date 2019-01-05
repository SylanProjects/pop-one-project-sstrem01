import pytest
from three_musketeers import *

left = 'left'
right = 'right'
up = 'up'
down = 'down'
directions = [left, right, up, down]
M = 'M'
R = 'R'
_ = '-'
poss_str = ['M', 'R', '-']

board1 =  [ [_, _, _, M, _],
            [_, _, R, M, _],
            [_, R, M, R, _],
            [_, R, _, _, _],
            [_, _, _, R, _] ]

board2 = [ [R, R, R, R, M],
          [R, R, R, R, R],
          [R, R, _, R, R],
          [R, M, R, _, R],
          [_, M, R, R, R] ]

board3 = [ [_, _, _, _, M],
          [_, _, M, _, M],
          [_, _, _, _, _],
          [R, _, _, _, R],
          [_, _, R, R, _] ]

board4 = [ [_, _, _, _, M],
          [_, _, M, _, M],
          [_, _, _, _, _],
          [_, _, _, _, _],
          [_, _, _, _, _] ]

board5 = [ [_, _, _, _, M],
          [_, _, M, _, _],
          [_, _, _, M, _],
          [R, _, _, _, R],
          [_, _, R, R, _] ]



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

    # Test if any of the items is not in the poss_str list which
    # stores the only possible strings that can be on the board.
    for i in range(4):
        for j in range(4):
            assert at((i, j)) in poss_str

    # Test the type
    for i in range(4):
        for j in range(4):
            obj = at((i, j))
            assert isinstance(obj, str)
    for i in range(4):
        for j in range(4):
            assert at((i, j)) == str(at((i, j)))



def test_set_board():
    set_board(board1)
    assert at((0,0)) == _
    assert at((1,2)) == R
    assert at((1,3)) == M
    # Test if any of the items is not in the poss_str list
    for i in range(4):
        for j in range(4):
            assert at((i, j)) in poss_str
    # Test the type
    for i in range(4):
        for j in range(4):
            obj = at((i, j))
            assert isinstance(obj, str)

    set_board(board2)
    assert at((4,0)) == _
    assert at((1,2)) == R
    assert at((4,1)) == M
    assert at((3,1)) == M
    assert at((0,4)) == M
    assert at((3,4)) == R
    # Test if any of the items is not in the poss_str list
    for i in range(4):
        for j in range(4):
            assert at((i, j)) in poss_str


def test_get_board():
    boards = [board1, board2, board3]
    for board in boards:
        set_board(board)
        assert board == get_board()

        # Test the type of the item at the given location
        for item in get_board():
            for i in range(4):
                assert item[i] == str(item[i])
                assert isinstance(item[i], str)

        # test if the item is in the possible strings
        for item in board:
            for i in range(4):
                assert item[i] in poss_str
        for item in get_board():
            for i in range(1):
                assert item[i] in poss_str


def test_string_to_location():
    # Raise a value error if the value is incorrect
    with pytest.raises(ValueError):
        string_to_location('X3')
    with pytest.raises(ValueError):
        string_to_location('F1')
    with pytest.raises(ValueError):
        string_to_location('G3')

    # Raise an error if string_to_location converts these
    # strings to anything but these tuples
    assert string_to_location('A1') == (0, 0)
    assert string_to_location('E2') == (4, 1)
    assert string_to_location('C4') == (2, 3)
    assert string_to_location('A4') == (0, 3)
    assert string_to_location('B3') == (1, 2)
    assert string_to_location('C1') == (2, 0)
    assert string_to_location('D4') == (3, 3)
    assert string_to_location('E5') == (4, 4)

    # Test the type of the output
    assert isinstance(string_to_location('E5'), tuple)
    assert isinstance(string_to_location('A1'), tuple)
    assert isinstance(string_to_location('E3'), tuple)
    assert isinstance(string_to_location('B4'), tuple)
    assert isinstance(string_to_location('B2'), tuple)
    assert isinstance(string_to_location('C5'), tuple)
    assert isinstance(string_to_location('C1'), tuple)




def test_location_to_string():
    create_board()

    # Raise an error if the value is not between A-E and 1-5
    with pytest.raises(ValueError):
        string_to_location('X3')
    with pytest.raises(ValueError):
        string_to_location('F1')
    with pytest.raises(ValueError):
        string_to_location('G3')

    assert location_to_string((0, 0)) == ('A1')
    assert location_to_string((1, 1)) == ('B2')
    assert location_to_string((4, 4)) == ('E5')

    # Test the type of the output
    for i in range(4):
        for j in range(4):
            assert isinstance(location_to_string((i, j)), str)

    assert isinstance(location_to_string((0, 0)), str)
    assert isinstance(location_to_string((3, 0)), str)


def test_at():
    create_board()
    assert at((1, 2)) == 'R'
    assert at((0, 4)) == M
    assert at((0, 0)) == R
    assert at((4, 2)) == 'R'
    assert at((4, 0)) == 'M'
    assert at((3, 0)) == R

    # Check the type of the output and make sure it is one
    # of the possible options

    for i in range(4):
        for j in range(4):
            assert isinstance(at((i, j)), str)
            assert at((i, j)) in poss_str


def test_all_locations():

    # Make sure that all_locations outputs exactly this list
    assert all_locations() == [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4),
                                (1, 0), (1, 1), (1, 2), (1, 3), (1, 4),
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

"""
The next few functions are very similar therefore the tests have been duplicated with
some changes made to them to fit the function.
"""

def test_is_legal_move_by_musketeer():
    set_board(board1)
    assert is_legal_move_by_musketeer((0, 3), 'left') == False
    assert is_legal_move_by_musketeer((0, 3), 'down') == False
    assert is_legal_move_by_musketeer((1, 3), 'left') == True
    assert is_legal_move_by_musketeer((1, 3), 'right') == False
    assert is_legal_move_by_musketeer((2, 2), 'down') == False

    set_board(board2)
    assert is_legal_move_by_musketeer((0, 4), 'left') == True
    assert is_legal_move_by_musketeer((0, 4), 'down') == True
    assert is_legal_move_by_musketeer((3, 1), 'left') == True
    assert is_legal_move_by_musketeer((3, 1), 'right') == True
    assert is_legal_move_by_musketeer((4, 1), 'up') == False

    set_board(board3)
    assert is_legal_move_by_musketeer((0, 4), 'left') == False
    assert is_legal_move_by_musketeer((0, 4), 'down') == False
    assert is_legal_move_by_musketeer((1, 2), 'left') == False
    assert is_legal_move_by_musketeer((1, 4), 'right') == False
    assert is_legal_move_by_musketeer((1, 4), 'up') == False



def test_is_legal_move_by_enemy():
    set_board(board1)
    assert is_legal_move_by_enemy((1, 2), 'left') == True
    assert is_legal_move_by_enemy((1, 2), 'right') == False
    assert is_legal_move_by_enemy((2, 1), 'left') == True
    assert is_legal_move_by_enemy((2, 3), 'right') == True
    assert is_legal_move_by_enemy((3, 1), 'up') == False
    assert is_legal_move_by_enemy((4, 3), 'down') == False

    set_board(board2)
    assert is_legal_move_by_enemy((1, 2), 'left') == False
    assert is_legal_move_by_enemy((1, 2), 'right') == False
    assert is_legal_move_by_enemy((2, 1), 'right') == True
    assert is_legal_move_by_enemy((2, 3), 'right') == False
    assert is_legal_move_by_enemy((3, 2), 'right') == True
    assert is_legal_move_by_enemy((4, 3), 'down') == False

    set_board(board3)
    assert is_legal_move_by_enemy((3, 4), 'left') == True
    assert is_legal_move_by_enemy((3, 4), 'right') == False
    assert is_legal_move_by_enemy((4, 2), 'right') == False
    assert is_legal_move_by_enemy((4, 2), 'up') == True
    assert is_legal_move_by_enemy((4, 3), 'right') == True
    assert is_legal_move_by_enemy((4, 3), 'left') == False

def test_is_legal_move():
    # Replace with tests
    set_board(board1)

    assert is_legal_move((0, 3), 'left') == False
    assert is_legal_move((0, 3), 'up') == False
    assert is_legal_move((1, 3), 'left') == True
    assert is_legal_move((1, 3), 'right') == False
    assert is_legal_move((4, 2), 'down') == False
    assert is_legal_move((2, 4), 'up') == False
    for i in range(4):
        for j in range(4):
            obj = is_legal_move((i, j), 'up')
            assert isinstance(obj, bool)


def test_can_move_piece_at():
    # Replace with tests
    set_board(board1)
    assert can_move_piece_at((0, 3)) == False
    assert can_move_piece_at((1, 2)) == True
    assert can_move_piece_at((1, 3)) == True
    assert can_move_piece_at((4, 3)) == True
    assert can_move_piece_at((3, 1)) == True
    assert can_move_piece_at((3, 0)) == False
    assert can_move_piece_at((4, 1)) == False
    for i in range(4):
        for j in range(4):
            obj = can_move_piece_at((i, j))
            assert isinstance(obj, bool)
    with pytest.raises(IndexError):
        can_move_piece_at((34, 1)) == False
    with pytest.raises(IndexError):
        can_move_piece_at((34, 7)) == False
    with pytest.raises(IndexError):
        can_move_piece_at((52, 86)) == False
    with pytest.raises(IndexError):
        can_move_piece_at((6, 8)) == False

def test_has_some_legal_move_somewhere():

    set_board(board1)
    assert has_some_legal_move_somewhere('M') == True
    assert has_some_legal_move_somewhere('R') == True
    set_board(board2)
    assert has_some_legal_move_somewhere('M') == True
    assert has_some_legal_move_somewhere('R') == True
    set_board(board3)
    assert has_some_legal_move_somewhere('M') == False
    assert has_some_legal_move_somewhere('R') == True
    set_board(board4)
    assert has_some_legal_move_somewhere('M') == False
    assert has_some_legal_move_somewhere('R') == False


def test_possible_moves_from():

    # Lists need to be sorted to make sure they are exactly the same
    set_board(board1)
    assert possible_moves_from((0, 3)) == []
    assert possible_moves_from((1, 2)).sort() == ['up', 'left'].sort()
    assert possible_moves_from((2, 1)).sort() == ['up', 'left'].sort()
    assert possible_moves_from((3, 1)).sort() == ['right', 'left', 'down'].sort()
    assert possible_moves_from((4, 3)).sort() == ['up', 'left', 'right'].sort()
    assert possible_moves_from((2, 2)).sort() == ['up', 'down', 'left', 'right'].sort()


    set_board(board2)
    assert possible_moves_from((4, 1)).sort() == ['right'].sort()
    assert possible_moves_from((3, 1)).sort() == ['up', 'left', 'right'].sort()
    assert possible_moves_from((4, 4)).sort() == ['up', 'left'].sort()
    assert possible_moves_from((0, 2)).sort() == ['right', 'left', 'down'].sort()
    assert possible_moves_from((1, 2)).sort() == ['up', 'left', 'right'].sort()
    assert possible_moves_from((1, 3)).sort() == ['up', 'down', 'left', 'right'].sort()


    set_board(board3)
    assert possible_moves_from((4, 2)).sort() == ['up', 'left'].sort()
    assert possible_moves_from((4, 3)).sort() == ['up', 'right'].sort()
    assert possible_moves_from((3, 4)).sort() == ['up', 'left', 'down'].sort()
    for i in range(4):
        for j in range(4):
            for direction in (possible_moves_from((i, j))):
                assert direction in directions

def test_is_legal_location():
    assert is_legal_location((0, 0)) == True
    assert is_legal_location((-1, 0)) == False
    assert is_legal_location((3, 2)) == True
    assert is_legal_location((2, 4)) == True
    assert is_legal_location((1, 2)) == True
    assert is_legal_location((5, 3)) == False
    assert is_legal_location((7, 3)) == False
    assert is_legal_location((2, 8)) == False
    for i in range(4):
        for j in range(4):
            obj = is_legal_location((i, j))
            assert isinstance(obj, bool)


def test_is_within_board():

    assert is_within_board((0, 0), 'right') == True
    assert is_within_board((3, 2), 'down') == True
    assert is_within_board((2, 4), 'right') == False
    assert is_within_board((1, 2), 'left') == True
    assert is_within_board((-1, 0), 'up') == False
    assert is_within_board((5, 3), 'down') == False
    assert is_within_board((7, 3), 'right') == False
    assert is_within_board((2, 8), 'down') == False
    for i in range(4):
        for j in range(4):
            obj = is_within_board((i, j), 'down')
            assert isinstance(obj, bool)

def test_all_possible_moves_for():
    # The lists need to be sorted to make sure they are exactly the same

    set_board(board1)
    assert all_possible_moves_for('M').sort() == [((1, 3), 'down'), ((1, 3), 'left'),
    ((2, 2), 'left'), ((2, 2), 'right'), ((2, 2), 'up')].sort()
    assert all_possible_moves_for('R').sort() == [((1, 2), 'left'), ((1, 2), 'up'), ((2, 1), 'left'),
    ((2, 1), 'up'), ((2, 3), 'right'), ((2, 3), 'down'), ((3, 1), 'left'), ((3, 1), 'right'),
    ((3, 1), 'down'), ((4, 3), 'left'), ((4, 3), 'right'), ((4, 3), 'up')].sort()

    set_board(board3)
    assert all_possible_moves_for('M') == []
    assert all_possible_moves_for('R').sort() == [((3, 0), 'right'), ((3, 0), 'up'), ((3, 0), 'down'),
    ((3, 4), 'left'), ((3, 4), 'up'), ((3, 4), 'down'), ((4, 2), 'left'),
    ((4, 2), 'up'), ((4, 3), 'right'), ((4, 3), 'up')].sort()


def test_choose_computer_move():
    with pytest.raises(ValueError):
        assert choose_computer_move('M') not in all_possible_moves_for('M')
    with pytest.raises(ValueError):
        assert choose_computer_move('M') not in all_possible_moves_for('M')
    assert choose_computer_move('M') in all_possible_moves_for('M')
    assert choose_computer_move('R') in all_possible_moves_for('R')

def test_is_enemy_win():
    # Replace with tests
    assert is_enemy_win() == True or is_enemy_win() == False


def test_check_sides():
    # Make sure that the output is the same as manually written one.
    set_board(board1)
    assert check_sides().sort() == [('up', 2, (2, 2)), ('right', 2, (2, 2)),
    ('left', 1, (1, 3)), ('down', 0, (0, 3))].sort()
    # Test the type
    for item in check_sides():
        assert isinstance(item, tuple)
    set_board(board2)
    assert check_sides().sort() == [('right', 1, (4, 1)),
    ('down', 0, (0, 4)), ('up', 0, (4, 1)), ('left', 0, (0, 4))].sort()
    for item in check_sides():
        assert isinstance(item, tuple)

    set_board(board3)
    assert check_sides().sort() == [('up', 3, (1, 4)),
    ('right', 2, (1, 2)), ('down', 0, (0, 4)), ('left', 0, (1, 4))].sort()
    for item in check_sides():
        assert isinstance(item, tuple)

def test_m_same_direction():
    set_board(board1)

    assert m_same_direction('right', (2, 3)) == True
    assert m_same_direction('down', (2, 3)) == True
    assert m_same_direction('left', (4, 0)) == False
    set_board(board2)
    assert m_same_direction('down', (2, 3)) == False
    assert m_same_direction('down', (3, 2)) == True
    assert m_same_direction('down', (3, 0)) == True
    for i in range(4):
        for j in range(4):
            assert isinstance(m_same_direction('down', (i, j)), bool)

def test_check_if_touching_m():
    set_board(board1)
    assert check_if_touching_m((0, 1)) == False
    assert check_if_touching_m((1, 2)) == True
    assert check_if_touching_m((4, 3)) == False
    assert check_if_touching_m((2, 1)) == True
    assert check_if_touching_m((2, 3)) == True
    assert check_if_touching_m((3, 1)) == False
    # Test the type
    for i in range(4):
        for j in range(4):
            assert isinstance(check_if_touching_m((i, j)), bool)
    set_board(board3)
    assert check_if_touching_m((1, 2)) == False
    assert check_if_touching_m((3, 0)) == False
    assert check_if_touching_m((4, 2)) == False
    assert check_if_touching_m((4, 3)) == False
    assert check_if_touching_m((3, 4)) == False

def test_check_m_direction():
    # Lists need to be sorted so they are exactly the same
    # Tests if the function outputs correct results and returns
    # an error if it doesn't
    set_board(board1)
    assert check_m_direction((1, 2)).sort() == ['up', 'left'].sort()
    assert check_m_direction((2, 3)).sort() == ['down', 'right'].sort()
    assert check_m_direction((2, 1)).sort() == ['left'].sort()
    set_board(board2)
    assert check_m_direction((2, 1)).sort() == ['up'].sort()
    assert check_m_direction((3, 0)).sort() == ['left'].sort()
    assert check_m_direction((1, 4)).sort() == ['down'].sort()

def test_high_priority_direction():
    set_board(board1)
    assert high_priority_direction(('right', 2, (3, 2)), ((2, 1), 'down')) == True
    assert high_priority_direction(('right', 2, (3, 2)), ((2, 1), 'down')) == True

def test_r_strategy():
    # This tests m_strategy and r_strategy
    boards = [board1, board2]
    for board in boards:
        set_board(board)
        moves = all_possible_moves_for('M') + all_possible_moves_for('R')
        assert r_strategy() in moves
        assert m_strategy() in moves

def test_check_for_m_positions():
    # Test if the function outputs correct results
    set_board(board1)
    assert check_for_m_positions() == True
    set_board(board2)
    assert check_for_m_positions() == True
    set_board(board3)
    assert check_for_m_positions() == True
    set_board(board5)
    assert check_for_m_positions() == False
    # Test the type
    assert isinstance(check_for_m_positions(), bool)

def test_get_m_same_row():
    set_board(board1)
    assert get_m_same_row().sort() == [[(0, 3), (1, 3)]].sort()
    # Test the type
    assert isinstance(get_m_same_row(), list)

    set_board(board2)
    assert get_m_same_row().sort() == [[(3, 1), (4, 1)]].sort()
    assert isinstance(get_m_same_row(), list)

    set_board(board3)
    assert get_m_same_row().sort() == [[(1, 2), (1, 4)], [(0, 4), (1, 4)]].sort()
    assert isinstance(get_m_same_row(), list)

    set_board(board5)
    assert get_m_same_row().sort() == [].sort()
    assert isinstance(get_m_same_row(), list)


def test_not_in_same_rc():
    """
    The rest of the function are very similar therefore the similar tests
    have been used, however they have been slightly changed to fit the functions.
    """
    set_board(board1)
    assert not_in_same_rc((2, 2), (2, 3)) == False
    assert not_in_same_rc((2, 2), (2, 1)) == True
    assert not_in_same_rc((1, 3), (1, 2)) == True
    set_board(board2)
    assert not_in_same_rc((3, 1), (3, 0)) == True
    assert not_in_same_rc((3, 1), (3, 2)) == True
    assert not_in_same_rc((0, 4), (0, 3)) == True

def test_other_m_not_in_same_rc():
    set_board(board1)
    assert other_m_not_in_same_rc((2, 2), (2, 3)) == False
    assert other_m_not_in_same_rc((2, 2), (2, 1)) == True
    assert other_m_not_in_same_rc((1, 3), (1, 2)) == False
    set_board(board2)
    assert other_m_not_in_same_rc((3, 1), (3, 0)) == True
    assert other_m_not_in_same_rc((3, 1), (3, 2)) == True
    assert other_m_not_in_same_rc((0, 4), (0, 3)) == True

def test_move_away():
    set_board(board1)
    assert other_m_not_in_same_rc((2, 2), (2, 3)) == False
    assert isinstance(other_m_not_in_same_rc((2, 2), (2, 3)), bool)
    assert other_m_not_in_same_rc((2, 2), (2, 1)) == True
    assert isinstance(other_m_not_in_same_rc((2, 2), (2, 1)), bool)
    assert other_m_not_in_same_rc((1, 3), (1, 2)) == False
    set_board(board2)
    assert other_m_not_in_same_rc((3, 1), (3, 0)) == True
    assert other_m_not_in_same_rc((3, 1), (3, 2)) == True
    assert isinstance(other_m_not_in_same_rc((3, 1), (3, 2)), bool)
    assert other_m_not_in_same_rc((0, 4), (0, 3)) == True
    assert isinstance(other_m_not_in_same_rc((0, 4), (0, 3)), bool)

def test_choose_best_move():
    set_board(board1)
    positions1 = [((0, 4), 'left'), ((0, 4), 'down'),
    ((1, 2), 'left'), ((1, 2), 'right'), ((1, 2), 'up'),
    ((1, 2), 'down'), ((4, 0), 'right'), ((4, 0), 'up')]
    assert choose_best_move(positions1) == ((1, 2), 'down')

    """
    m_strategy function has been tested in the test_r_strategy function since they
    are almost exactly the same.
    """
