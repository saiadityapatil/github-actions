from app import add, subtract, multiply

def test_add():
    assert add(3,4)==7
def test_subtract():
    assert subtract(10,5)==5
def test_multiply():
    assert multiply(2,3)==6