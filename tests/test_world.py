from world import World, InvalidCharacterError


def test_add_rocks():
    world = World()
    world.add_rocks(str.encode(". .\n. .\n :T.\n. .\n   ."))
    assert world.state == {3: [{'type': '.', 'row': 0}, {'type': '.', 'row': 2}], 0: [{'type': '.', 'row': 1}, {'type': '.', 'row': 3}, {'type': '.', 'row': 4}], 2: [{'type': '.', 'row': 1}, {'type': 'T', 'row': 2}, {'type': '.', 'row': 3}, {'type': '.', 'row': 4}], 1: [{'type': ':', 'row': 2}]}


def test_add_rocks_error():
    world = World()
    error_caught = False
    try:
        world.add_rocks(str.encode(". .\n. .\n :U.\n. .\n   ."))
    except InvalidCharacterError:
        error_caught = True
    assert error_caught is True


def test_gravity():
    world = World()
    world.state = {3: [{'type': '.', 'row': 0}, {'type': '.', 'row': 2}], 0: [{'type': '.', 'row': 1}, {'type': '.', 'row': 3}, {'type': '.', 'row': 4}], 2: [{'type': '.', 'row': 1}, {'type': 'T', 'row': 2}, {'type': '.', 'row': 3}, {'type': '.', 'row': 4}], 1: [{'type': ':', 'row': 2}]}
    world.apply_gravity()
    assert world.col_cnt == 4
    assert world.row_cnt == 4


def test_get_graphical():
    world = World()
    world.state = {3: [{'type': ':', 'row': 0}], 0: [{'type': ':', 'row': 0}, {'type': '.', 'row': 1}], 2: [{'type': '.', 'row': 0}, {'type': 'T', 'row': 2}, {'type': ':', 'row': 3}], 1: [{'type': ':', 'row': 0}]}
    world.col_cnt = 4
    world.row_cnt = 4
    assert world.get_graphical_world() == str.encode("  : \n  T \n.   \n::.:")


def test_empty_col():
    world = World()
    world.add_rocks(str.encode(". . \n. .    .\n :T.   \n. .    :\n   .."))
    world.apply_gravity()
    assert world.col_cnt == 8
    assert world.row_cnt == 4
