from simple_typer import add


def test_add() -> None:
    assert 5.0 == add(2.0, 3.0)
