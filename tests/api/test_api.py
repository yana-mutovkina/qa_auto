class User:
    def __init__(self) -> None:
        self.name = "Yana"
        self.surname = "Mutovkina"

user = User()

def test_remove_name():
    user.name = ""
    assert user.name == ""

def test_name():
    assert user.name == "Yana"

def test_surname();
    assert user.surname == "Mutovkina"