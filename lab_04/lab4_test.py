from lab4 import *
def test_zpz():
    assert ' '.join(zpz("2 ^ 3")) == "2 3 ^"
    assert ' '.join(zpz("4 * 5 - 3 / 1 + 2")) == "4 5 * 3 1 / - 2 +"
    assert ' '.join(zpz("( 7 - 4 ) ^ 2 + 6 / 3")) == "7 4 - 2 ^ 6 3 / +"
    assert ' '.join(zpz("5 + 3 * 8 / 2")) == "5 3 8 * 2 / +"


def test_answ():
    assert answ(zpz("2 ^ 3")) == 8
    assert answ(zpz("4 * 5 - 3 / 1 + 2")) == 19
    assert answ(zpz("( 7 - 4 ) * 2 + 6 / 3")) == 8
    assert answ(zpz("5 + 3 * 8 / 2")) == 17