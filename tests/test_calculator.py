from calculator import add, div, sub, mul


def test_add():
    assert add (1,1)==2

def test_sub():
    assert sub(1,1)==2

def test_mul():
    assert mul(1,1)==1

def test_div():
    assert div(2,1)==2
