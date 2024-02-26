import main


def test_hello():
    assert main.hello() == "Hello, world!"


def test_add():
    assert main.add(1, 2) == 3
    assert main.add(0, 0) == 0
    assert main.add(-1, 1) == 0
    assert main.add(0, -1) == -1
    assert main.add(-1, -1) == -2


def test_subtract():
    assert main.subtract(1, 2) == -1
    assert main.subtract(0, 0) == 0
    assert main.subtract(-1, 1) == -2
    assert main.subtract(0, -1) == 1
    assert main.subtract(-1, -1) == 0


def test_addStringsWithSpace():
    assert main.addStringsWithSpace("Hello", "World") == "Hello World"
    assert main.addStringsWithSpace("Hello", "") == "Hello "
    assert main.addStringsWithSpace("", "World") == " World"
    assert main.addStringsWithSpace("", "") == " "
