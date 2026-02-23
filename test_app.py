from app import add

def test_add():
    assert add(7, 3) == 10
    assert add(0, 0) == 0