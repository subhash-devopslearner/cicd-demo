# from app import add

# def test_add():
#     assert add(7, 3) == 10
#     assert add(0, 0) == 0

from app import app

def test_home():
    client = app.test_client()
    response = client.get('/')
    assert response.status_code == 200

def test_add():
    client = app.test_client()
    response = client.get('/add/2/3')
    assert response.json['result'] == 5