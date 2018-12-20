# The Three Musketeers Game

# In all methods,
#   A 'location' is a two-tuple of integers, each in the range 0 to 4.
#        The first integer is the row number, the second is the column number.
#   A 'direction' is one of the strings "up", "down", "left", or "right".
#   A 'board' is a list of 5 lists, each containing 5 strings: "M", "R", or "-".
#        "M" = Musketeer, "R" = Cardinal Richleau's man, "-" = empty.
#        Each list of 5 strings is a "row"
#   A 'player' is one of the strings "M" or "R" (or sometimes "-").
#
# For brevity, Cardinal Richleau's men are referred to as "enemy".
# 'pass' is a no-nothing Python statement. Replace it with actual code.
POSSIBLE_CHARACTERS = ["A", "B", "C", "D", "E"]
import random
def create_board():
    global board
    """Creates the initial Three Musketeers board and makes it globally
       available (That is, it doesn't have to be passed around as a
       parameter.) 'M' represents a Musketeer, 'R' represents one of
       Cardinal Richleau's men, and '-' denotes an empty space."""
    m = 'M'
    r = 'R'
    _ = '-'
    board = [ [r, r, r, r, m],
              [r, r, r, r, r],
              [r, r, m, r, r],
              [r, r, r, r, r],
              [m, r, r, r, r] ]

def set_board(new_board):
    """Replaces the global board with new_board."""
    global board
    board = new_board

def get_board():
    """Just returns the board. Possibly useful for unit tests."""
    return board

def string_to_location(s):
    """Given a two-character string (such as 'A5'), returns the designated
       location as a 2-tuple (such as (0, 4)).
       The function should raise ValueError exception if the input
       is outside of the correct range (between 'A' and 'E' for s[0] and
       between '1' and '5' for s[1]"""

    n = list(s)
    poss_char = ["A", "B", "C", "D", "E"]
    if int(n[1]) - 1 > 4 or int(n[1]) - 1 < 0:
        return ValueError

    else:
        return POSSIBLE_CHARACTERS.index(n[0]), int(n[1]) - 1

def location_to_string(location):
    """Returns the string representation of a location.
    Similarly to the previous function, this function should raise
    ValueError exception if the input is outside of the correct range
    """
    g = ["", ""]
    g[0] = POSSIBLE_CHARACTERS[location[0]]
    g[1] = location[1] + 1
    if int(g[1]) > 5 or int(g[1]) < 1:
        return ValueError
    else:
        return str(g[0]) + str(g[1])

def at(location):
    """Returns the contents of the board at the given location.
    You can assume that input will always be in correct range."""
    return board[location[0]][location[1]]

def all_locations():
    """Returns a list of all 25 locations on the board."""
    l = []
    for i in range(5):
        for j in range(5):
            l.append((i, j))
    return l

def all_locations_for_m():
    all_loc = all_locations()
    m = []
    for element in all_loc:
        if at(element) == "M":
            m.append(element)
    return m

def all_locations_for_r():
    all_loc = all_locations()
    r = []
    for element in all_loc:
        if at(element) == 'R':
            r.append(element)
    return r


def adjacent_location(location, direction):
    """Return the location next to the given one, in the given direction.
       Does not check if the location returned is legal on a 5x5 board.
       You can assume that input will always be in correct range."""
    (row, column) = location

    if direction == "left":
        column -= 1
    elif direction == "right":
        column += 1
    elif direction == "up":
        row -= 1
    elif direction == "down":
        row += 1
    return [row, column]


def is_legal_move_by_musketeer(location, direction):
    """Tests if the Musketeer at the location can move in the direction.
    You can assume that input will always be in correct range. Raises
    ValueError exception if at(location) is not 'M'"""

    (row, column) = location

    if at([row, column]) != 'M':
        return ValueError
    (row, column) = adjacent_location(location, direction)[0], adjacent_location(location, direction)[1]
    if is_within_board(location, direction) == False:
        return False
    if is_within_board(location, direction) == False:
        return False

    if at([row, column]) == '-' or at([row, column]) == 'M':
        return False
    elif at([row, column]) == 'R':
        return True
    else:
        return False



def is_legal_move_by_enemy(location, direction):
    """Tests if the enemy at the location can move in the direction.
    You can assume that input will always be in correct range. Raises
    ValueError exception if at(location) is not 'R'"""
    (row, column) = location


    if at([row, column]) != 'R':
        return ValueError
    if is_within_board(location, direction) == False:
        return False
    (row, column) = adjacent_location(location, direction)[0], adjacent_location(location, direction)[1]
    if is_within_board(location, direction) == False:
        return False

    if at([row, column]) == 'M' or at([row, column]) == 'R':
        return False
    elif at([row, column]) == '-':
        return True

    else:
        return False

def is_legal_move(location, direction):
    """Tests whether it is legal to move the piece at the location
    in the given direction.
    You can assume that input will always be in correct range."""

    (row, column) = location
    if at(location) == 'M':

        if is_legal_move_by_musketeer(location, direction):
            return True
    if at(location) == 'R':
        if is_legal_move_by_enemy(location, direction):
            return True
    return False



def can_move_piece_at(location):
    """Tests whether the player at the location has at least one move available.
    You can assume that input will always be in correct range."""
    (row, column) = location
    z = []
    if is_legal_move(location, 'left'):
        Left = adjacent_location(location, 'left')
        z.append(Left)
    if is_legal_move(location, 'right'):
        Right = adjacent_location(location, 'right')
        z.append(Right)
    if is_legal_move(location, 'up'):
        Up = adjacent_location(location, 'up')
        z.append(Up)
    if is_legal_move(location, 'down'):
        Down = adjacent_location(location, 'down')
        z.append(Down)

    for element in z:

        if at(element) == '-'  and at(location) == 'R':
            return True

        elif at(element) == 'R'  and at(location) == 'M':
            return True


    return False


def has_some_legal_move_somewhere(who):
    """Tests whether a legal move exists for player "who" (which must
    be either 'M' or 'R'). Does not provide any information on where
    the legal move is.
    You can assume that input will always be in correct range."""
    L = all_locations()

    for location in L:
        if at(location) == who and can_move_piece_at(location):
            return True

def possible_moves_from(location):
    """Returns a list of directions ('left', etc.) in which it is legal
       for the player at location to move. If there is no player at
       location, returns the empty list, [].
       You can assume that input will always be in correct range."""
    possible_moves = []
    if is_legal_move(location, 'left'):
        possible_moves.append('left')
    if is_legal_move(location, 'right'):
        possible_moves.append('right')
    if is_legal_move(location, 'up'):
        possible_moves.append('up')
    if is_legal_move(location, 'down'):
        possible_moves.append('down')


    return possible_moves


def is_legal_location(location):
    """ Tests if the location is legal on a 5x5 board.
        You can assume that input will be a pair of integer numbers."""
    row, column = location
    if row < 0 or row > 4:
        return False
    elif column < 0 or column > 4:
        return False

    else:
        return True

def is_within_board(location, direction):
    """Tests if the move stays within the boundaries of the board.
    You can assume that input will always be in correct range."""

    (row, column) = location
    g = adjacent_location(location, direction)
    if g[0] < 0 or g[0] > 4:
        return False
    elif g[1] < 0 or g[1] > 4:
        return False
    else:
        return True

def all_possible_moves_for(player):
    """Returns every possible move for the player ('M' or 'R') as a list
       (location, direction) tuples.
       You can assume that input will always be in correct range."""
    L = all_locations()
    locations = []
    possible_moves = []
    for location in L:
        if at(location) == player:
            locations.append(location)


    for location in locations:
        if is_legal_move(location, 'left'):
            possible_moves.append((location, 'left'))
        if is_legal_move(location, 'right'):
            possible_moves.append((location, 'right'))
        if is_legal_move(location, 'up'):
            possible_moves.append((location, 'up'))
        if is_legal_move(location, 'down'):
            possible_moves.append((location, 'down'))

    return possible_moves

def make_move(location, direction):
    """Moves the piece in location in the indicated direction.
    Doesn't check if the move is legal. You can assume that input will always
    be in correct range."""

    curr_contents = at(location)
    adj_location = adjacent_location(location, direction)
    (row, column) = adj_location
    board[row][column] = curr_contents
    board[location[0]][location[1]] = '-'



def r_strategy():
    poss_moves = all_possible_moves_for('R')
    poss_moves_m = all_possible_moves_for('M')
    m_locs = all_locations_for_m()
    return random.choice(poss_moves)

#    for item in m_locs:
#        print(item)
#
#    for i in range(2):
#        print(m_locs[i][0])
"""
    LOOK FOR M POSITIONS THAT ARE EITHER IN THE SAME ROW OR COLUMN (BOOLEAN)

    IF TRUE
        LOOK FOR THE R THAT ARE AROUND THEM
        IF WHEN YOU MOVE THAT R THE AMOUNT OF POSSIBLE MOVES GETS LOWER FOR M
            MOVE TO THAT POSITION
        IF IT GETS BIGGER
            GO THROUGH THE NEXT ONE
        DO THE SAME FOR EACH POSITION UNTIL FINDING THE BEST
        IF SAME POSITIONS LOWER THE AMOUNT OF POSSIBLE M MOVES
            PICK THE ONE THAT WILL BE THE FURTHEST AWAY FROM THE MUSKETEERS
        IF ALL ELSE FAILS
            PICK RANDOMLY









     Strategies for R
     if who = R
     get all the possible moves for the opponent
     if majority of the musketeers is on one side, for example if
     m1 is at (0, 1), m2 is at (2, 4) and m3 is at (3, 3)
     look for moves for R that are exactly to the left of M
     to limit their choices and make them move right
     priority should be given to the one that is furthest from the rest
    ###
     if this is not possible, look for possible moves for r
     so he has an option to move to one side
     priority should again be given to the one furthest from the rest
     to bring them all closer to each other

     if the above is not possible
     r should try to move closer to the furthest one away from the rest
     to give him an option to move to the rest """







def check_for_m_positions():
    """
    This function returns true or false if there are two musketeers in the same row or column.
    It does not return the positions of these two musketeers
    """
    m_locs = all_locations_for_m()
    for i in range(2):
        if m_locs[0][i] == m_locs[1][i]:
            return True
        if m_locs[0][i] == m_locs[2][i]:
            return True
        if m_locs[1][i] == m_locs[2][i]:
            return True
    return False



def get_m_same_row():
    """
    This function returns all positions where two musketeers ar
    e
    in the same row or column.
    """
    m_locs = all_locations_for_m()
    positions = []
    for i in range(2):
        if m_locs[0][i] == m_locs[1][i]:
            positions.append([m_locs[0], m_locs[1]])
        if m_locs[0][i] == m_locs[2][i]:
            positions.append([m_locs[0], m_locs[2]])
        if m_locs[1][i] == m_locs[2][i]:
            positions.append([m_locs[1], m_locs[2]])

    return positions


def m_strategy():
    poss_moves = all_possible_moves_for('M')


    if check_for_m_positions():
        positions = get_m_same_row()
        print(positions)

        for item in positions:
            print(item)
            moves = possible_moves_from(item[0])
            """
            for each position in moves
            if there is musketeers already in that column or row
                go through the next one
                save positions that wont put the musketeer in the same r/c

            if there are few positions
                choose the one that will put the M furthest away from others
            if there are no saved positions
                choose the one that will put the M furthest away from others  
            """

    return random.choice(poss_moves)


    """
     RETURN TRUE IF TWO POSITIONS ARE THE SAME
     IF TRUE
         RETURN THE TWO POSITIONS
         IF THERE ARE MORE PAIRS
         SAVE THEM AND GO THROUGH THE FIRST PAIR

         LOOK FOR MOVES IN THE FIRST POSITIONS AND RETURN TRUE
         IF NO MOVES CARRY ON
         IF MOVES: LOOK WHAT WILL BE THE OUTCOME
            IF TWO POSITIONS WONT BE THE SAME AGAIN
            SAVE THAT POSITION

        DO THE SAME FOR THE SECOND POSITION

        PICK THE BEST POSITION
        IF IT WILL HAVE MORE MOVES THEN CHOOSE THAT POSITION

        IF THEY WILL HAVE THE SAME AMOUNT OF MOVES
            LOOK WHICH ONES WILL BE BETTER
            FOR EXAMPLE DONT INCLUDE THE SAME POSITIONS THAT ARE OCCUPIED BY OTHER MUSKETEER
            IF ALL ELSE FAILS
                CHOOSE RANDOMLY
    DO THE SAME FOR A DIFFERENT SET OF TWO POSITIONS
    AFTER SAVING ALL THE POSITIONS LOOK WHICH ONE WILL BE THE BEST
    (SAME AS ABOVE)
    MOVE IN THAT POSITION



    Strategies for M
    Stay as far away from each other as possible:
    goes through each position vertically and horizontally
    for example, if one of the Ms(M1) is in the same row as the other(M2),
    he should move away in the opposite direction that the third (M3) is
    to make sure that they are not close to each other.
    Who moves should be decided based on the position of the M
    For example if M1 is on (0, 0), M2 is on (0, 1) and m3 is on (1, 4)
    M4 should move down if possible, if not, M2 should move to the right
    if possible to move them away from each other

    If that's not possible, he should move only if his new position won't put him
    in the same row as the third (M3)
    Otherwise, someone else should move
    """


def choose_computer_move(who):
    """The computer chooses a move for a Musketeer (who = 'M') or an
       enemy (who = 'R') and returns it as the tuple (location, direction),
       where a location is a (row, column) tuple as usual.
       You can assume that input will always be in correct range."""
    #if check_for_m_positions():


    if who == 'R':
        return r_strategy()
    else:
        return m_strategy()



def is_enemy_win():
    """Returns True if all 3 Musketeers are in the same row or column."""
    m = all_locations_for_m()
    if m[0][0] == m[1][0]:
        if m[1][0] == m[2][0]:
            return True
    elif m[0][1] == m[1][1]:
        if m[1][1] == m[2][1]:
            return True
    else:
        return False


#---------- Communicating with the user ----------
#----you do not need to modify code below unless you find a bug
#----a bug in it before you move to stage 3

def print_board():
    print("    1  2  3  4  5")
    print("  ---------------")
    ch = "A"
    for i in range(0, 5):
        print(ch, "|", end = " ")
        for j in range(0, 5):
            print(board[i][j] + " ", end = " ")
        print()
        ch = chr(ord(ch) + 1)
    print()

def print_instructions():
    print()
    print("""To make a move, enter the location of the piece you want to move,
and the direction you want it to move. Locations are indicated as a
letter (A, B, C, D, or E) followed by an integer (1, 2, 3, 4, or 5).
Directions are indicated as left, right, up, or down (or simply L, R,
U, or D). For example, to move the Musketeer from the top right-hand
corner to the row below, enter 'A5 left' (without quotes).
For convenience in typing, you may use lowercase letters.""")
    print()

def choose_users_side():
    """Returns 'M' if user is playing Musketeers, 'R' otherwise."""
    user = ""
    while user != 'M' and user != 'R':
        answer = input("Would you like to play Musketeer (M) or enemy (R)? ")
        answer = answer.strip()
        if answer != "":
            user = answer.upper()[0]
    return user

def get_users_move():
    """Gets a legal move from the user, and returns it as a
       (location, direction) tuple."""
    directions = {'L':'left', 'R':'right', 'U':'up', 'D':'down'}
    move = input("Your move? ").upper().replace(' ', '')
    if (len(move) >= 3
            and move[0] in 'ABCDE'
            and move[1] in '12345'
            and move[2] in 'LRUD'):
        location = string_to_location(move[0:2])
        direction = directions[move[2]]
        if is_legal_move(location, direction):
            return (location, direction)
    print("Illegal move--'" + move + "'")
    return get_users_move()

def move_musketeer(users_side):
    """Gets the Musketeer's move (from either the user or the computer)
       and makes it."""
    if users_side == 'M':
        (location, direction) = get_users_move()
        if at(location) == 'M':
            if is_legal_move(location, direction):
                make_move(location, direction)
                describe_move("Musketeer", location, direction)
        else:
            print("You can't move there!")
            return move_musketeer(users_side)
    else: # Computer plays Musketeer
        (location, direction) = choose_computer_move('M')
        make_move(location, direction)
        describe_move("Musketeer", location, direction)

def move_enemy(users_side):
    """Gets the enemy's move (from either the user or the computer)
       and makes it."""
    if users_side == 'R':
        (location, direction) = get_users_move()
        if at(location) == 'R':
            if is_legal_move(location, direction):
                make_move(location, direction)
                describe_move("Enemy", location, direction)
        else:
            print("You can't move there!")
            return move_enemy(users_side)
    else: # Computer plays enemy
        (location, direction) = choose_computer_move('R')
        make_move(location, direction)
        describe_move("Enemy", location, direction)
        return board

def describe_move(who, location, direction):
    """Prints a sentence describing the given move."""
    new_location = adjacent_location(location, direction)
    print(who, 'moves', direction, 'from',\
          location_to_string(location), 'to',\
          location_to_string(new_location) + ".\n")

def start():
    """Plays the Three Musketeers Game."""
    users_side = choose_users_side()
    board = create_board()
    print_instructions()
    print_board()
    while True:
        if has_some_legal_move_somewhere('M'):
            board = move_musketeer(users_side)
            print_board()
            if is_enemy_win():
                print("Cardinal Richleau's men win!")
                break
        else:
            print("The Musketeers win!")
            break
        if has_some_legal_move_somewhere('R'):
            board = move_enemy(users_side)
            print_board()
        else:
            print("The Musketeers win!")
            break
