import pytest
from bruchrechenapp.src.model.bruch import Bruch


def test_constructor() -> None:
    b = Bruch(2,4)
    assert 2 == b.zaehler
    assert 4 == b.nenner

    with pytest.raises(ValueError) as info:
        Bruch(1,0)
    assert "nenner == 0" in str(info.value)

    b = Bruch(1,-2)
    assert -1 == b.zaehler
    assert 2 == b.nenner

def test_equals() -> None:
    assert Bruch(1,2) == Bruch(1,2)
    assert Bruch(1,2) != Bruch(2,4)

def test_kuerze() -> None:
    assert Bruch(1,2) == Bruch(6,12).kuerze()
    assert Bruch(-2,3) == Bruch(-24,36).kuerze()

def test_addiere() -> None:
    assert Bruch(5,6) == Bruch(1,2).addiere(Bruch(1,3))
    assert Bruch(3,4) == Bruch(1,2).addiere(Bruch(1,4))

def test_subtrahiere() -> None:
    assert Bruch(-1,6) == Bruch(1,3).subtrahiere(Bruch(1,2))
    assert Bruch(1,4) == Bruch(1,2).subtrahiere(Bruch(1,4))

def test_multipliziere() -> None:
    assert Bruch(1,2) == Bruch(3,4).multipliziere(Bruch(2,3))

def test_dividiere() -> None:
    assert Bruch(1,2) == Bruch(3,4).dividiere(Bruch(3,2))
