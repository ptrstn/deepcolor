from deepcolor.strategies import create_strategy_entry, available_strategy_names


def test_create_strategy_entry():
    expected = {
        "strategy_name": "A",
        "short": "B",
        "description": "C",
        "url": None,
    }

    assert create_strategy_entry("A", "B", "C") == expected

    expected = {
        "strategy_name": "A",
        "short": "B",
        "description": "C",
        "url": "D",
    }

    assert create_strategy_entry("A", "B", "C", "D") == expected


def test_available_strategy_names():
    assert ["richzhang", "colornet", "zeruniverse"] == available_strategy_names()
