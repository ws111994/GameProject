"""
Your name: Shuang Wu
Your student number: A01275027

All of your code must go in this file.
"""


import random
import itertools

EXP_TO_LEVEL = [15, 25, 2000]
MAX_HP_LEVEL = [5, 15, 30]
MAX_DMG_LEVEL = [4, 6, 8]
SPECIAL_BOOST_HP = 2
SPECIAL_BOOST_EXP = 5
FOO_HP_LEVEL = [10, 18, 26]
FOO_DMG_LEVEL = [1, 2, 3]
ITEM_DAMAGE = 15
COMBAT_EXP = [2, 4, 10]
RICH_CLASS = ['Rich Boi', 'Lottery Winner', 'Elon Musk']
SMART_CLASS = ['GPA 4.0 Boi', 'Theoretical Physicist', 'Neil deGrasse Tyson']
SPORT_CLASS = ['Basketball Team Leader', 'NBA Rookie', 'LeBron James']
GAMER_CLASS = ['CST Student', 'Indie Game Developer', 'Naoki Yoshida']
RICH_CLASS_SKILL = 'Shopping Spree'
SMART_CLASS_SKILL = 'Reciting Pi'
SPORT_CLASS_SKILL = 'Dunking Rampage'
GAMER_CLASS_SKILL = 'Showing off a SUD'
BOSS_HP = 50
BOSS_DAMAGE = 6
ROWS = 25
COLUMNS = 25
RANDOM_ROOM = ['Top of Vancouver Revolving Restaurant', 'Starbucks', 'Nordstrom', 'DT street', 'DT street',
               'DT street', 'DT street', 'DT street', 'DT street', 'DT street', 'DT street']
CLASS_LIST = ['Rich Man', 'Smart Man', 'Sports Man', 'Gamer']
POSSIBLE_BOSS = [['Griana Arande', RICH_CLASS], ['Germione Hranger', SMART_CLASS],
                 ['Saylor Twift', SPORT_CLASS], ['Lifa Tockhart', GAMER_CLASS]]
POSSIBLE_GIRLS = [['Gold digging girl', RICH_CLASS], ['Librarian girl', SMART_CLASS],
                  ['Cheerleader', SPORT_CLASS], ['Gamer girl', GAMER_CLASS]]
POSSIBLE_ACTION = ['Charm', 'Skill', 'Item', 'Flee']
ITEM_LIST = ['LV limited edition handbag']


def make_board(rows: int, columns: int) -> dict:
    """
    Generate a dictionary with room coordinates as keys, room description as value.

    :param rows: an integer
    :param columns: an integer
    :precondition: rows and columns must be positive integers equal to or greater than two
    :postcondition: generate a dictionary that contains rows * columns number of keys.
    :postcondition: generate a dictionary that has tuple (indicating coordinates) as key, and a string describing
    the key as value for each key value pair.
    :postcondition: rows and columns remain unchanged after executing the function
    :return: a dictionary with tuple of coordinates as keys and string description as values

    # test for number of keys in dictionary equals to input_1 * input_2
    >>> map_rows = 2
    >>> map_columns = 2
    >>> new_board = make_board(map_rows, map_columns)
    >>> all_keys = new_board.keys()
    >>> len(all_keys) == map_rows * map_columns
    True

    # test for correct type of output
    >>> type(new_board) == dict
    True

    """
    board = {(row, column): RANDOM_ROOM[random.randint(0, len(RANDOM_ROOM) - 1)] for row in range(rows)
             for column in range(columns)}
    return board


def make_map(rows: int, columns: int) -> list:
    """
    Generate a map as a 2d list.

    :param rows: an integer
    :param columns: an integer
    :precon: rows and columns must be greater than zero
    :postcon: generate a 2d list
    :postcondition: rows and columns remain unchanged after executing the function
    :return: map is a list

    >>> make_map(2, 2)
    [['|_|', '|_|'], ['|_|', '|_|']]
    """
    return [["|_|" for _ in range(rows)] for _ in range(columns)]


def mark_special_on_map(character: dict, board: dict, original_map: list) -> None:
    """
    Mark special locations, character location, and boss location on map.

    :param character: a dictionary
    :param board: a dictionary
    :param original_map: a list
    :precon: board must have tuple coordinates as keys and strings within RANDOM_ROOM as values
    :precon: character must have X and Y coordinates as key value pairs
    :precon: original_map must be a 2d list of strings
    :postcon: overwrite correct elements with special locations, character, and boss in original_map
    :postcon: character and board remain unchanged after execution the function


    >>> new_board = {(0, 0): "Starbucks", (0, 1): "DT street", (1, 0): "Starbucks", (1, 1): "Starbucks" }
    >>> new_character = {'X-coordinate': 0, 'Y-coordinate': 0}
    >>> new_map = [['|_|', '|_|'], ['|_|', '|_|']]
    >>> mark_special_on_map(new_character, new_board, new_map)
    >>> new_map
    [['|U|', '|^|'], ['|_|', '|B|']]

    """
    # overwrite special rooms onto map
    for key, value in board.items():
        if value == RANDOM_ROOM[0]:
            original_map[key[1]][key[0]] = '|+|'
        if value == RANDOM_ROOM[1]:
            original_map[key[1]][key[0]] = '|^|'
        if value == RANDOM_ROOM[2]:
            original_map[key[1]][key[0]] = '|!|'

    # overwrite boss location onto map
    original_map[-1][-1] = '|B|'

    # overwrite current character location onto map
    original_map[character['Y-coordinate']][character['X-coordinate']] = '|U|'


def print_map(original_map: list) -> None:
    """
    Print a joined 2d list.

    :param original_map: a list
    :precon: original_map must be a 2d list of strings
    :postcon: join provided 2d list into one string and print it


    >>> new_map = [['|U|', '|^|'], ['|_|', '|B|']]
    >>> print_map(new_map)
    |U||^|
    |_||B|
    """
    print('\n'.join(map(''.join, original_map)))


def choose_class() -> str:
    """
    Return user's choice of class as a string.

    The function will repeatedly prompt user to enter a valid input if user input is not within "1", "2", "3", or "4".

    :postcon: return user's choice of class as a string
    :return: user's choice of class as a string
    """

    valid_input = False
    char_class = None

    # if user does not enter valid input, keep looping
    while not valid_input:

        # print available options
        for _, boy in enumerate(CLASS_LIST, 1):
            print(_, boy)
        char_class = input('Please choose a boy you want to be (1-4): ')
        valid_choices = ['1', '2', '3', '4']
        if char_class not in valid_choices:
            print('Please choose a valid option between 1-4')
        else:
            valid_input = True

    # retrieve corresponding class name from global constant using user input as an index
    return CLASS_LIST[int(char_class) - 1]


def choose_name() -> str:
    """
    Return user's input for character name

    :postcon: return user's input for character name as a string
    :return: character name is a string
    """
    user_input = ''
    while user_input.strip() == '':
        user_input = input('Please enter your name (cannot be empty):')
    return user_input.strip()


def make_character(class_name: str, char_name: str) -> dict:
    """
    Create a dictionary representing initial status of a new character for each class.

    create a dictionary including 'X-coordinate", "Y-coordinate", "Current HP", "Max HP", "level", "level", "exp",
    "damage", "item" as keys with default values for all classes, "class", "skill" keys with class specific values for
    different classes, "name" key with user input as value.

    :param class_name: a string
    :param char_name: a string
    :precon: class_name must be elements inside global constant CLASS_LIST
    :postcon: return a correct character dictionary according to user's class choice and character name
    :postcon: class_name and char_name remain unchanged after executing the function
    :return: representation of new character created is a dictionary

    >>> class_name_new = 'Gamer'
    >>> char_name_new = 'Harry Potter'
    >>> new_character = make_character(class_name_new, char_name_new)
    >>> new_character['name']
    'Harry Potter'
    >>> new_character['class']
    'CST Student'
    >>> new_character['skill']
    'Showing off a SUD'


    """
    if class_name == CLASS_LIST[0]:
        character = {'X-coordinate': 0,
                     'Y-coordinate': 0,
                     'Max HP': MAX_HP_LEVEL[0],
                     'Current HP': MAX_HP_LEVEL[0],
                     'name': char_name,
                     'level': 1,
                     'exp': 0,
                     'class': RICH_CLASS[0],
                     'skill': RICH_CLASS_SKILL,
                     'damage': MAX_DMG_LEVEL[0],
                     'item': None}
    elif class_name == CLASS_LIST[1]:
        character = {'X-coordinate': 0,
                     'Y-coordinate': 0,
                     'Max HP': MAX_HP_LEVEL[0],
                     'Current HP': MAX_HP_LEVEL[0],
                     'name': char_name,
                     'level': 1,
                     'exp': 0,
                     'class': SMART_CLASS[0],
                     'skill': SMART_CLASS_SKILL,
                     'damage': MAX_DMG_LEVEL[0],
                     'item': None}
    elif class_name == CLASS_LIST[2]:
        character = {'X-coordinate': 0,
                     'Y-coordinate': 0,
                     'Max HP': MAX_HP_LEVEL[0],
                     'Current HP': MAX_HP_LEVEL[0],
                     'name': char_name,
                     'level': 1,
                     'exp': 0,
                     'class': SPORT_CLASS[0],
                     'skill': SPORT_CLASS_SKILL,
                     'damage': MAX_DMG_LEVEL[0],
                     'item': None}
    else:
        character = {'X-coordinate': 0,
                     'Y-coordinate': 0,
                     'Max HP': MAX_HP_LEVEL[0],
                     'Current HP': MAX_HP_LEVEL[0],
                     'name': char_name,
                     'level': 1,
                     'exp': 0,
                     'class': GAMER_CLASS[0],
                     'skill': GAMER_CLASS_SKILL,
                     'damage': MAX_DMG_LEVEL[0],
                     'item': None}
    return character


def generate_boss() -> dict:
    """
    Create a dictionary representing the boss.

    :postcon: Return a boss dictionary with name and type value randomly chosen from global constant POSSIBLE_BOSS
    :return: representation of boss is a dictionary
    """
    result_boss = POSSIBLE_BOSS[random.randint(0, len(POSSIBLE_BOSS) - 1)]
    return {'name': result_boss[0],
            'Current HP': BOSS_HP,
            'Max HP': BOSS_HP,
            'damage': BOSS_DAMAGE,
            'type': result_boss[1],
            'boss': True}


def introduction(character: dict, boss: dict) -> None:
    """
    Print introduction message.

    :param character: a dictionary
    :param boss: a dictionary
    :precon: character must have name as one of the keys
    :precon: boss must have name as one of the keys
    :postcon: print introduction message containing a random int between 101-9999, correct character name and boss name
    :postcon: character and boss remain unchanged after execution
    """

    print(f"Welcome to this world for the {random.randint(101,9999)}th time, {character['name']}."
          f"\nYour girlfriend, {boss['name']}, has been acting weird lately. You think something is not right."
          f"\nMaybe it's you, maybe it's her, maybe there's something else in the dark. You woke up this morning to an"
          f"\nempty bed, she is gone, disappeared. You frantically called all your friends about it, but they don't"
          f"\neven seem to recognize her name anymore. You looked at the calendar, May 23th 2014, the day you met her"
          f"\nseven years ago. You hear a mysterious voice inside your head: She is out there, somewhere waiting to"
          f"\nfall in love with you again. Go, find her. You have so many questions about your current situation."
          f"\nDid you travel back in time? Was this a dream I had before? The mysterious voice remained silent."
          f"\nEven though this is surreal in every aspect, you have decided to find her, again....again...again...?"
          f"\n(Why am I saying AGAIN?)")


def ending() -> None:
    """
    Print ending message for successful game clear.

    :postcon: print nice ascii art and ending message for successful game clear
    """

    print(r"""
    |\_____/|     ////\
    |/// \\\|    /// \\\
     |/O O\|     |/o o\|
     d  ^ .b     C  )  D   
      \\m//      | \_/ |
       \_/        \___/
     __ooo__    _/<|_|>\_
    /_     _\  / |/\_/\| \
    | \_v_/ | |    |\|    |
    || _/ _/\\| |  |\|  | |
    ||)    ( \| |  |\|  | |
    ||  42  \ | \\ |\|  | |
    ||  --  |  (())\_/  | |
    ((      |   |___|___|_|
     |______|   |   Y   |))
      |-||-|    |   |   |
      | || |    |   |   |
      | || |    |   |   |
      | || |    |___|___|
     /u\||/u\   /qp| |qp\
    (_/\||/\_) (___/ \___)
    
    Finally, you meet her, again. You two live happily ever after. (Hopefully)
    But...she seems a little bit...weird. Why is she ALWAYS smiling? Why is there a number on her dress?
    You feel dizzy... The last moment you see is her smile... and a message 'Restarting Source Code Program..'
    """)


def describe_current_location(board: dict, character: dict) -> None:
    """
    Print current location's description string.

    :param board: a dictionary
    :param character: a dictionary
    :precondition: board must be a dictionary that has tuple (indicating coordinates) as key, and a string describing
    the key as value for each key value pair.
    :precondition: character must be a dictionary that contains "X-coordinate", and "Y-coordinate" keys
    :postcondition: print the string value of ('X-coordinate", "Y-coordinate") key within the board dictionary
    :postcondition: board and character remain unchanged after executing the function

    >>> new_board = {(0, 0): 'Empty room', (0, 1): 'Dangerous room', (1, 0): 'Treasure room', (1, 1): 'Treasure room'}
    >>> new_character = {'X-coordinate': 0, 'Y-coordinate': 0, 'Current HP': 5}
    >>> describe_current_location(new_board, new_character)
    You are at (0, 0)
    Current area is Empty room

    """
    print(f"You are at {(character['X-coordinate'], character['Y-coordinate'])}\n"
          f"Current area is {board[(character['X-coordinate'], character['Y-coordinate'])]}")


def current_location(board: dict, character: dict) -> str:
    """
    Return current location of the character on the map.

    :param board: a dictionary
    :param character: a dictionary
    :precondition: board must be a dictionary that has tuple (indicating coordinates) as key, and a string describing
    the key as value for each key value pair.
    :precondition: character must be a dictionary that contains "X-coordinate", and "Y-coordinate" keys
    :postcondition: board and character remain unchanged after executing the function
    :postcondition: return the string value of ('X-coordinate", "Y-coordinate") key within the board dictionary
    :return: location description is a string

    >>> new_board = {(0, 0): 'Empty room'}
    >>> new_character = {'X-coordinate': 0, 'Y-coordinate': 0}
    >>> current_location(new_board, new_character)
    'Empty room'
    """
    return board[(character['X-coordinate'], character['Y-coordinate'])]


def check_for_special(location: str) -> bool:
    """
    Check if the current location is a special one or not.

    :param location: a string
    :precon: location must be one of the elements inside global constant RANDOM_ROOM
    :postcon: return True if location is not the same as the last element in global constant RANDOM_ROOM, otherwise
    return False
    :postcon: location remains unchanged after executing the function
    :return: True if location is not the same as the last element in global constant RANDOM_ROOM, False if otherwise

    >>> new_location = 'DT street'
    >>> check_for_special(new_location)
    False

    >>> another_location = 'Starbucks'
    >>> check_for_special(another_location)
    True
    """

    # all special locations will be place in front of RANDOM_ROOM, last element will always be non-special location
    if location != RANDOM_ROOM[-1]:
        return True
    else:
        return False


def special_event(special_location: str, character: dict) -> None:
    """
    Execute specific event for different special locations.

    :param special_location: a string
    :param character: a dictionary
    :precon: special_location must be one of the elements inside global constant RANDOM_ROOM
    :precon: character must have 'Max HP", 'Current HP', 'exp', 'item' as keys
    :postcon: modify character's 'Max HP' and 'Current HP' according to global const SPECIAL_BOOST_HP if
    special_location is the first element in RANDOM_ROOM
    :postcon: modify character's 'exp' according to global const SPECIAL_BOOST_EXP if special_location is the
    second element in RANDOM_ROOM
    :postcon: modify character's 'item' if special_location is none of above and 'item' is None
    :postcon: print corresponding notification after each special event
    :postcon: special_location remains unchanged after execution the function

    # Starbucks event boosts character exp
    >>> new_location = 'Starbucks'
    >>> new_character = {'Max HP': 5, 'Current HP': 4, 'exp': 0, 'item': None}
    >>> special_event(new_location, new_character)
    Your Exp is boosted by 5.
    >>> new_character['exp'] == 5
    True

    # Top of Vancouver Revolving Restaurant event boosts character HP
    >>> new_location = 'Top of Vancouver Revolving Restaurant'
    >>> special_event(new_location, new_character)
    Your current and max HP is boosted by 2.
    >>> new_character['Max HP'] == 7 and new_character['Current HP'] == 6
    True

    # Nordstrom event gives character item
    >>> new_location = 'Nordstrom'
    >>> special_event(new_location, new_character)
    You bought a LV limited edition handbag.
    >>> new_character['item'] == 'LV limited edition handbag'
    True

    # character can only have one item
    >>> new_location = 'Nordstrom'
    >>> special_event(new_location, new_character)
    You already bought a LV limited edition handbag, please gift it to someone before buying another one.
    >>> new_character['item'] == 'LV limited edition handbag'
    True
    """
    # this event boost character's max and current hp
    if special_location == RANDOM_ROOM[0]:
        character['Max HP'] += SPECIAL_BOOST_HP
        character['Current HP'] += SPECIAL_BOOST_HP
        print(f'Your current and max HP is boosted by {SPECIAL_BOOST_HP}.')

    # this event boost character's exp
    elif special_location == RANDOM_ROOM[1]:
        character['exp'] += SPECIAL_BOOST_EXP
        print(f'Your Exp is boosted by {SPECIAL_BOOST_EXP}.')
    else:
        # if character does not have any item
        if character['item'] is None:
            character['item'] = ITEM_LIST[0]
            print(f'You bought a {character["item"]}.')

        # character can have up to one item
        else:
            print(f'You already bought a {character["item"]}, please gift it to someone before buying another one.')


def erase_special_location(board: dict, character: dict) -> None:
    """
    Restore special location back to ordinary location after character passing through it.

    :param board: a dictionary
    :param character: a dictionary
    :precon: board must be a dictionary that has tuple (indicating coordinates) as key, and a string describing
    the key as value for each key value pair.
    :precon: character must be a dictionary that contains "X-coordinate", and "Y-coordinate" keys
    :postcon: modify character's current location on board with last element in RANDOM_ROOM
    :postcon: character remains unchanged after execution

    >>> new_board = {(0, 0): 'Starbucks'}
    >>> new_character = {'X-coordinate': 0, 'Y-coordinate': 0}
    >>> erase_special_location(new_board, new_character)
    >>> new_board[(0, 0)] == 'DT street'
    True
    """
    board[(character['X-coordinate'], character['Y-coordinate'])] = RANDOM_ROOM[-1]


def get_user_choice() -> str:
    """
    Return valid user input for directional movement or quit.

    :postcondition: return valid user input for directional movement or quit
    :postcondition: print instruction message informing user valid options
    :return: valid user choice is a string
    """
    direction = ['Up', 'Down', 'Left', 'Right']
    valid_input = False

    # keep looping if user does not enter [1-4] or quit
    while not valid_input:
        print("Please choose a direction to move (or quit):")
        for count, element in list(zip(itertools.count(1, 1), direction)):
            print(count, element)
        user_choice = input()
        valid_choices = ['1', '2', '3', '4', 'quit']
        if user_choice not in valid_choices:
            print('Please choose a valid option between 1-4')
        else:
            return user_choice


def convert_to_direction_offset(user_choice: str) -> tuple:
    """
    Convert user input into coordinate offset.

    :param user_choice: a string
    :precon: user_choice must be within ['1', '2', '3', '4']
    :postcon: user_choice is unchanged after execution
    :postcon: convert user input into correct coordinate offset as a tuple
    :return: coordinate offset is a tuple

    >>> choice = '1'
    >>> convert_to_direction_offset(choice)
    (0, -1)

    >>> choice = '4'
    >>> convert_to_direction_offset(choice)
    (1, 0)
    """
    direction_offset = [(0, -1), (0, 1), (-1, 0), (1, 0)]
    return direction_offset[int(user_choice) - 1]


def check_quit(user_choice: str) -> bool:
    """
    Detect if user wants to quit the game.

    :param user_choice: a string
    :precon: user_choice must have at least one character
    :postcon: return True if user_choice is 'quit', False otherwise
    :return: Return True if user_choice is 'quit', False otherwise

    >>> choice = 'quit'
    >>> check_quit(choice)
    True

    >>> choice = 'not quit'
    >>> check_quit(choice)
    False
    """
    if user_choice == 'quit':
        return True
    else:
        return False


def validate_move(board: dict, character: dict, direction: tuple) -> bool:
    """
    Check if the direction change is valid depending on character's current location on the board.

    :param board: a dictionary
    :param character: a dictionary
    :param direction: a tuple
    :precondition: board must be a dictionary that has tuple (indicating coordinates) as key, and a string describing
    the key as value for each key value pair.
    :precondition: character must be a dictionary that contains "X-coordinate", and "Y-coordinate" keys
    :precondition: direction must be a tuple within the this list of tuples: [(0, 1), (0, -1), (1, 0), (-1, 0)]
    :postcondition: add first number of direction tuple to character's 'X-coordinate' value, and add second number of
    direction tuple to character's 'Y-coordinate' value.
    :postcondition: search character's updated coordinate within board's keys
    :postcondition: board remains unchanged after executing the function
    :postcondition: character remains unchanged after executing the function
    :return: True if character's coordinate remains within board's keys after update, otherwise, False.

    # test for valid move
    >>> new_board = {(0, 0): 'Empty room', (0, 1): 'Dangerous room', (1, 0): 'Treasure room', (1, 1): 'Treasure room'}
    >>> current_character = {'X-coordinate': 0, 'Y-coordinate': 0, 'Current HP': 5}
    >>> direction_change = (1, 0)
    >>> validate_move(new_board, current_character, direction_change)
    True

    # test for invalid move
    >>> new_board = {(0, 0): 'Empty room', (0, 1): 'Dangerous room', (1, 0): 'Treasure room', (1, 1): 'Treasure room'}
    >>> current_character = {'X-coordinate': 0, 'Y-coordinate': 0, 'Current HP': 5}
    >>> direction_change = (-1, 0)
    >>> validate_move(new_board, current_character, direction_change)
    False


    """
    if (character['X-coordinate'] + direction[0], character['Y-coordinate'] + direction[1]) in board.keys():
        return True
    else:
        return False


def move_character(character: dict, direction: tuple) -> None:
    """
    Update character location values according to direction change input.

    :param character: a dictionary
    :param direction: a tuple
    :precondition: character must be a dictionary that contains "X-coordinate", and "Y-coordinate" keys
    :precondition: direction must be a tuple within the this list of tuples: [(0, 1), (0, -1), (1, 0), (-1, 0)]
    :postcondition: update X-coordinate value of character according to direction's first number
    :postcondition: update Y-coordinate value of character according to direction's second number

    # test for moving right
    >>> direction_change = (1, 0)
    >>> new_character = {'X-coordinate': 0, 'Y-coordinate': 0}
    >>> move_character(new_character, direction_change)
    >>> new_character['X-coordinate'] == 1 and new_character['Y-coordinate'] == 0
    True

    # test for moving down
    >>> direction_change = (0, 1)
    >>> new_character = {'X-coordinate': 0, 'Y-coordinate': 0}
    >>> move_character(new_character, direction_change)
    >>> new_character['X-coordinate'] == 0 and new_character['Y-coordinate'] == 1
    True
    """
    character['X-coordinate'] += direction[0]
    character['Y-coordinate'] += direction[1]


def check_if_at_boss_location(board: dict, character: dict) -> bool:
    """
    Check if character's current location is the most bottom right room on the board.

    :param board: a dictionary
    :param character: a dictionary
    :precondition: board must be a dictionary that has tuple (indicating coordinates) as key, and a string describing
    the key as value for each key value pair.
    :precondition: character must be a dictionary that contains "X-coordinate", and "Y-coordinate" keys
    :postcondition: compare character's X and Y coordinates with the board's key with largest numbers
    :postcondition: board remains unchanged after executing the function
    :postcondition: character remains unchanged after executing the function
    :return: True if character's X and Y coordinates are the same as the board's largest key pair, otherwise False

    # test for goal attained
    >>> new_board = make_board(4, 4)
    >>> new_character = {'X-coordinate': 3, 'Y-coordinate': 3, 'Current HP': 5}
    >>> check_if_at_boss_location(new_board, new_character)
    True

    # test for goal not attained
    >>> new_board = make_board(4, 4)
    >>> new_character = {'X-coordinate': 2, 'Y-coordinate': 3, 'Current HP': 5}
    >>> check_if_at_boss_location(new_board, new_character)
    False
    """

    biggest_value = 0
    for key in board.keys():
        if sum(key) > biggest_value:
            biggest_value = sum(key)
    if character['X-coordinate'] + character['Y-coordinate'] == biggest_value:
        return True
    else:
        return False


def check_for_girls() -> bool:
    """
    Return True with 20% chance, otherwise return False.

    :postcondition: generate a random integer between one and four
    :postcondition: return True if randomly generated number is one, otherwise return False
    :return: True if randomly generated number is one, otherwise return False

    """
    return random.randint(1, 5) == 1


def generate_girl(character: dict) -> dict:
    """
    Create a dictionary for encountered girl based on character level.

    Girls could be one of four different types.

    :param character: a dictionary
    :precon: character must have 'level' as key
    :postcon: Create a dictionary for girl, girl's HP and damage is based on character['level']
    :postcon: character remains unchanged after execution
    :return: representation for encountered girl is a dictionary
    """
    result_girl = POSSIBLE_GIRLS[random.randint(0, len(POSSIBLE_GIRLS) - 1)]
    return {'name': result_girl[0], 'Current HP': FOO_HP_LEVEL[character['level'] - 1],
            'Max HP': FOO_HP_LEVEL[character['level'] - 1], 'damage': FOO_DMG_LEVEL[character['level'] - 1],
            'type': result_girl[1], 'boss': False}


def describe_girl(girl: dict) -> None:
    """
    Print encounter message with encountered girl's name.

    :param girl: a dictionary
    :precon: girl must have 'name' as key
    :postcon: print a message including girl's name
    :postcon: girl remains unchanged after execution

    >>> new_girl = {'name': 'Alice'}
    >>> describe_girl(new_girl)
    *** A wild Alice appears ! ***
    """

    print(f'*** A wild {girl["name"]} appears ! ***')


def girl_current_hp(girl: dict) -> None:
    """
    Print information with girl's hp status.

    :param girl: a dictionary
    :precon: girl must have 'Current HP' and 'Max HP' as keys
    :postcon: print a message including girl's hp status
    :postcon: girl remains unchanged after execution

    >>> new_girl = {'Current HP': 5, 'Max HP': 10}
    >>> girl_current_hp(new_girl)
    Her resistance to your love is [5 / 10].

    """

    print(f'Her resistance to your love is [{girl["Current HP"]} / {girl["Max HP"]}].')


def character_current_status(character: dict) -> None:
    """
    Print information with character's current status.

    :param character: a dictionary
    :precon: character must have "Current HP", "Max HP", "level", "exp", "damage", "item", "class", and 'name' as keys
    :postcon: character remains unchanged after execution
    :postcon: print character's current status including hp, level, exp, damage, item, class, and name values

    >>> new_character = make_character('Rich Man', 'Bob')
    >>> character_current_status(new_character)
    Bob's current status [Resistance: 5/5] [Level: 1] [Exp: 0] [Charm: 4] [Item: None] [Social Position: Rich Boi]
    """

    print(f'{character["name"]}\'s current status [Resistance: {character["Current HP"]}/{character["Max HP"]}]'
          f' [Level: {character["level"]}] [Exp: {character["exp"]}] [Charm: {character["damage"]}] '
          f'[Item: {character["item"]}] [Social Position: {character["class"]}]')


def get_user_action() -> str:
    """
    Convert user input into one of four possible actions as a string output.

    :postcon: convert valid user input into corresponding action and return it as a string
    :return: user's choice of action is a string
    """

    valid_input = False
    while not valid_input:
        for _, action in enumerate(POSSIBLE_ACTION, 1):
            print(_, action)
        user_action = input('Please choose an action (1-4): ')
        valid_choices = ['1', '2', '3', '4']
        if user_action not in valid_choices:
            print('Please choose a valid option between 1-4')
        else:
            return POSSIBLE_ACTION[int(user_action) - 1]


def execute_action(action: str, character: dict, girl: dict) -> None:
    """
    Execute corresponding action based on user's choice of action.

    :param action: a string
    :param character: a dictionary
    :param girl: a dictionary
    :precon: action must be one of the element in POSSIBLE_ACTION
    :precon: character must have 'skill', 'damage', 'name', 'Current HP', 'class', 'item' as keys with valid values
    :precon: girl must have 'Current HP', 'damage', 'name', 'type' as keys with valid values
    :postcon: execute charm function with character and girl as parameters if action is POSSIBLE_ACTION[0]
    :postcon: execute skill function with character and girl as parameters if action is POSSIBLE_ACTION[1]
    :postcon: execute use_item function with character and girl as parameters if action is POSSIBLE_ACTION[2]
    :postcon: execute flee function with character and girl as parameters if none of above
    """

    if action == POSSIBLE_ACTION[0]:
        charm(character, girl)
    elif action == POSSIBLE_ACTION[1]:
        skill(character, girl)
    elif action == POSSIBLE_ACTION[2]:
        use_item(character, girl)
    else:
        flee(character, girl)


def charm(attacker: dict, receiver: dict) -> None:
    """
    Deduct receiver's current HP value with attacker's damage value.

    :param attacker: a dictionary
    :param receiver: a dictionary
    :precon: attacker must have 'name' and 'damage' keys with valid values
    :precon: receiver must have 'name' and 'Current HP' keys with valid values
    :postcon: deduct receiver's 'Current HP' value with attacker's 'damage' value
    :postcon: print message with attacker and receiver's 'name' value
    :postcon: set receiver's 'Current HP' to zero if it becomes negative

    >>> new_attacker = {'damage': 1, 'name': 'Alice'}
    >>> new_receiver = {'Current HP': 2, 'name': 'Bob'}
    >>> charm(new_attacker, new_receiver)
    Alice tried to charm Bob.
    >>> new_receiver['Current HP'] == 1
    True

    >>> new_attacker = {'damage': 2, 'name': 'Alice'}
    >>> new_receiver = {'Current HP': 1, 'name': 'Bob'}
    >>> charm(new_attacker, new_receiver)
    Alice tried to charm Bob.
    >>> new_receiver['Current HP'] == 0
    True
    """

    # deduct attacker's damage amount of HP from receiver
    receiver['Current HP'] -= attacker['damage']

    # HP will not go into negative
    if receiver['Current HP'] < 0:
        receiver['Current HP'] = 0
    print(f"{attacker['name']} tried to charm {receiver['name']}.")


def skill(character: dict, girl: dict) -> None:
    """
    Deduct girl's HP according to character's skill damage.

    Character's skill will deal more damage if character and girl have same class type, less damage otherwise.

    :param character: a dictionary
    :param girl: a dictionary
    :precon: character must have 'class', 'skill', and 'damage' keys with valid values
    :precon: girl must have 'type', 'Current HP', and 'name' keys with valid values
    :postcon: deduct girl['Current HP'] by two times of character['damage'] if character's class is in girl's type list
    :postcon: deduct girl['Current HP'] by half of character['damage'] if character's class is not in girl's type list
    :postcon: girl's hp value will change after executing the function
    :postcon: character remains unchanged after executing the function
    :postcon: print message including character's skill name and girl's name

    >>> new_girl = {'name': 'Alice', 'type': ['CST Student', 'Indie Game Developer', 'Naoki Yoshida'], 'Current HP': 8}
    >>> new_character = {'class': 'CST Student', 'damage': 2, 'skill': 'Build a game'}
    >>> skill(new_character, new_girl)
    You initiated your special skill: Build a game!
    Alice is super into you! The skill is very effective!
    >>> new_girl['Current HP'] == 4
    True

    >>> new_girl = {'name': 'Alice', 'type': ['CST Student', 'Indie Game Developer', 'Naoki Yoshida'], 'Current HP': 8}
    >>> new_character = {'class': 'Rich Boi', 'damage': 2, 'skill': 'Shopping Spree'}
    >>> skill(new_character, new_girl)
    You initiated your special skill: Shopping Spree!
    Alice smiles at you politely, with a little bit of cringe.
    >>> new_girl['Current HP'] == 7
    True
    """

    # if character's class belong the to same class family as girl's type, extra damage
    if character['class'] in girl['type']:
        girl['Current HP'] -= character['damage'] * 2
        print(f"You initiated your special skill: {character['skill']}!\n"
              f"{girl['name']} is super into you! The skill is very effective!")

    # if character and girl have different class family, less damage
    else:
        girl['Current HP'] -= character['damage'] / 2
        print(f"You initiated your special skill: {character['skill']}!\n"
              f"{girl['name']} smiles at you politely, with a little bit of cringe.")


def use_item(character: dict, girl: dict) -> None:
    """
    Gift item to encountered girl if character has one.

    The item will be extra effective if girl's type belongs to RICH_CLASS.

    :param character: a dictionary
    :param girl: a dictionary
    :precon: character must have 'item' key
    :precon: girl must have 'name', 'type', and 'Current HP' keys with valid values
    :postcon: print fail to gift item message if character['item'] is None
    :postcon: deduct girl's HP with ITEM_DAMAGE * 2 if girl's type belongs to RICH_CLASS and character has item
    :postcon: deduct girl's HP with ITEM_DAMAGE if girl's type does not belong to RICH_CLASS and character has item

    >>> new_girl = {'Current HP': 30, 'type': ['Rich Boi', 'Lottery Winner', 'Elon Musk'], 'name': 'Alice'}
    >>> new_character = {'item': 'something'}
    >>> use_item(new_character, new_girl)
    You gifted Alice something, it's super effective!
    >>> new_girl['Current HP'] == 0
    True

    >>> new_girl = {'Current HP': 15, 'type': ['CST Student', 'Indie Game Developer', 'Naoki Yoshida'], 'name': 'Alice'}
    >>> new_character = {'item': 'something'}
    >>> use_item(new_character, new_girl)
    You gifted Alice something, she happily accepted it.
    >>> new_girl['Current HP'] == 0
    True

    >>> new_character = {'item': None}
    >>> use_item(new_character, new_girl)
    You frantically searched for something to gift her, but you found none. You missed your timing.

    """

    # girl's HP is unchanged if character does not have any item
    if character['item'] is None:
        print("You frantically searched for something to gift her, but you found none. You missed your timing.")
    else:

        # if girl has the type of RICH_CLASS, gifting item to her will be extra effective
        if girl['type'] == RICH_CLASS:
            girl['Current HP'] -= ITEM_DAMAGE * 2
            print(f"You gifted {girl['name']} {character['item']}, it's super effective!")

        # gifting does normal damage otherwise
        else:
            girl['Current HP'] -= ITEM_DAMAGE
            print(f"You gifted {girl['name']} {character['item']}, she happily accepted it.")
        character['item'] = None


def flee(character: dict, girl: dict) -> None:
    """
    Deduct character's HP by girl's damage with 20% chance.

    :param character: a dictionary
    :param girl: a dictionary
    :precon: character must have 'Current HP' key with valid values
    :precon: girl must have 'damage' and 'name' keys with valid values
    :postcon: deduct character's current hp with girl's damage if 1 is randomly picked from range 1 to 5 by system, hp
    does not change otherwise
    :postcon: print corresponding message for both scenarios
    :postcon: girl remains unchanged after executing the function
    """

    if random.randint(1, 5) == 1:
        character['Current HP'] -= girl['damage']
        print(f"{girl['name']} gave you a fly kiss when you shamelessly ran away from her. Now your resistance "
              f"is {character['Current HP']}.")
    else:
        print(f"You told {girl['name']} that you are married, so {girl['name']} let you go free.")


def choose_flee(action: str) -> bool:
    """
    Detect if action chose by the user is to flee.

    :param action: a string
    :postcon: return True if action is the last element in POSSIBLE_ACTION list, which is 'Flee', false otherwise
    :return: True if action is 'Flee', False otherwise

    >>> choose_flee('fight')
    False

    >>> choose_flee('Flee')
    True
    """
    return action == POSSIBLE_ACTION[3]


def girl_flee(girl: dict) -> bool:
    """
    Detect if the girl chooses to flee.

    Girl has 20% chance to flee.

    :param girl: a dictionary
    :precon: girl must have 'name' key with valid value
    :postcon: return True if 1 is randomly picked from integer 1-5 by system, False otherwise
    :postcon: girl remains unchanged after executing the function
    :postcon: print a message with girl's name when she chooses to flee
    :return: True with 20% chance, False otherwise
    """

    flee_happen = random.randint(1, 5) == 1
    if flee_happen:
        print(f'{girl["name"]} is not interested in you anymore, she walked away like you never existed.')
    return flee_happen


def gain_exp(character: dict) -> None:
    """
    Add experience to character.

    :param character: a dictionary
    :precon: character must have 'exp' and 'level' keys with valid values
    :postcon: add exp according to character's level
    :postcon: print how much exp has been gained

    >>> new_character = {'level': 1, 'exp': 0}
    >>> gain_exp(new_character)
    You gained 2 fame.
    >>> new_character['exp']
    2

    >>> new_character = {'level': 2, 'exp': 0}
    >>> gain_exp(new_character)
    You gained 4 fame.
    >>> new_character['exp']
    4
    """
    character['exp'] += COMBAT_EXP[character['level'] - 1]
    print(f"You gained {COMBAT_EXP[character['level'] - 1]} fame.")


def check_level_up(character: dict) -> bool:
    """
    Detect if character's experience is enough to level up.

    :param character: a dictionary
    :precon: character must have 'exp' and 'level' keys with valid values
    :postcon: return True if character exp is sufficient to level up, False otherwise
    :postcon: print how much exp is needed to level up if current exp is not sufficient to level up
    :return: True if if character exp is sufficient to level up, False otherwise

    >>> new_character = {'level': 1, 'exp': 0}
    >>> check_level_up(new_character)
    You are 15 fame away from becoming a better person
    False

    >>> new_character = {'level': 1, 'exp': 30}
    >>> check_level_up(new_character)
    True
    """

    # character's current exp is sufficient to level up according to global constant EXP_TO_LEVEL
    if character['exp'] >= EXP_TO_LEVEL[character['level'] - 1]:
        return True

    # calculate exp needed to next level
    else:
        exp_to_level_up = EXP_TO_LEVEL[character['level'] - 1] - character['exp']
        print(f"You are {exp_to_level_up} fame away from becoming a better person")
        return False


def level_up(character: dict) -> None:
    """
    Level up the character.

    Upon level up, exp resets to zero, current hp, max hp, and damage all increase.

    :param character: a dictionary
    :precon: character must have 'level', 'exp', 'Max HP', 'Current HP', and 'damage' as keys with valid values
    :postcon: increase level by one, reset exp to zero, increase max hp, current hp, and damage accordingly
    :postcon: character's 'level', 'exp', 'Max HP', 'Current HP', and 'damage' values will change upon execution
    :postcon: print level up congradulation message

    >>> new_character = {'level': 1, 'exp': 20, 'Max HP': 10, 'Current HP': 8, 'damage': 5}
    >>> level_up(new_character)
    You feel more confident in yourself! More charming! More Love!
    >>> new_character
    {'level': 2, 'exp': 0, 'Max HP': 25, 'Current HP': 23, 'damage': 6}
    """

    character['level'] += 1
    character['exp'] = 0
    character['Max HP'] += MAX_HP_LEVEL[character['level'] - 1]
    character['Current HP'] += MAX_HP_LEVEL[character['level'] - 1]
    character['damage'] = MAX_DMG_LEVEL[character['level'] - 1]
    print(f"You feel more confident in yourself! More charming! More Love!")


def class_advancement(character: dict) -> None:
    """
    Assign new class name for character according to character's level.

    :param character: a dictionary
    :precon: character must have 'class' and 'level' keys with valid values
    :postcon: update character's class value according to character's class family and level
    :postcon: print congratulatory message with new class name

    >>> new_character = {'class': 'CST Student', 'level': 2}
    >>> class_advancement(new_character)
    Others start to call you Indie Game Developer, you feel like you are on a whole new level!
    >>> new_character['class']
    'Indie Game Developer'
    """

    if character['class'] in RICH_CLASS:
        character['class'] = RICH_CLASS[character['level'] - 1]
    elif character['class'] in SMART_CLASS:
        character['class'] = SMART_CLASS[character['level'] - 1]
    elif character['class'] in SPORT_CLASS:
        character['class'] = SPORT_CLASS[character['level'] - 1]
    elif character['class'] in GAMER_CLASS:
        character['class'] = GAMER_CLASS[character['level'] - 1]
    print(f"Others start to call you {character['class']}, you feel like you are on a whole new level!")


def is_alive(character: dict) -> bool:
    """
    Check if character's Current HP is zero or not.

    :param character: a dictionary
    :precondition: character must be a dictionary that contains "Current HP" key
    :postcondition: compare character's "Current HP" value with zero
    :postcondition: character remains unchanged after executing the function
    :return: False if "Current HP" value is equal to zero, otherwise return True

    # test for alive character
    >>> new_character = make_character('Rich Man', 'Bob')
    >>> is_alive(new_character)
    True

    # test for dead character
    >>> new_character = make_character('Rich Man', 'Bob')
    >>> new_character["Current HP"] = 0
    >>> is_alive(new_character)
    False
    """
    if character['Current HP'] >= 1:
        return True
    else:
        return False


def is_boss(girl: dict) -> bool:
    """
    Detect if the encountered girl is the boss.

    :param girl: a dictionary
    :precon: girl must have 'boss' key with a boolean value
    :postcon: return True if girl's 'boss' value is True, False otherwise
    :postcon: girl remains unchanged after executing the function
    :return: True if girl is a boss, False otherwise

    >>> new_girl = {'boss': True}
    >>> is_boss(new_girl)
    True

    >>> new_girl = {'boss': False}
    >>> is_boss(new_girl)
    False
    """

    return girl['boss']


def game():
    """
    Drive the main game loop.

    """
    board = make_board(ROWS, COLUMNS)
    user_class = choose_class()
    char_name = choose_name()
    character = make_character(user_class, char_name)
    boss = generate_boss()
    achieved_goal = False
    introduction(character, boss)
    while is_alive(character) and not achieved_goal:
        # // Tell the user where they are
        original_map = make_map(ROWS, COLUMNS)
        mark_special_on_map(character, board, original_map)
        print_map(original_map)
        user_choice = get_user_choice()
        if check_quit(user_choice):
            exit()
        direction = convert_to_direction_offset(user_choice)
        valid_move = validate_move(board, character, direction)
        if valid_move:
            move_character(character, direction)
            describe_current_location(board, character)
            location = current_location(board, character)
            special_location = check_for_special(location)
            if special_location:
                special_event(location, character)
                erase_special_location(board, character)
                exp_full = check_level_up(character)
                if exp_full:
                    level_up(character)
                    class_advancement(character)
            if check_for_girls() or check_if_at_boss_location(board, character):
                girl = generate_girl(character)
                if check_if_at_boss_location(board, character):
                    girl = boss
                describe_girl(girl)
                while is_alive(girl) and is_alive(character):
                    girl_current_hp(girl)
                    character_current_status(character)
                    action = get_user_action()
                    execute_action(action, character, girl)
                    if choose_flee(action):
                        break
                    if is_alive(girl) and not is_boss(girl):
                        if girl_flee(girl):
                            break
                    if is_alive(girl):
                        charm(girl, character)
                    else:
                        gain_exp(character)
                        exp_full = check_level_up(character)
                        if exp_full:
                            level_up(character)
                            class_advancement(character)
                achieved_goal = not is_alive(boss)
        else:
            print('You cannot go in that direction, choose again.')
    if is_alive(character):
        print('Congratulation! You win The Truman Game!')
        ending()
        exit()
    else:
        print('Sorry, you fell in love with a girl and lost control of your life.')
        exit()


def main():
    """
    Drive the program.
    """
    game()


if __name__ == "__main__":
    main()
