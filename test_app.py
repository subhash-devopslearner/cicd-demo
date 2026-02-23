from app import add

def test_add():
    assert add(2, 3) == 99
    assert add(0, 0) == 0