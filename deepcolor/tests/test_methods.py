from deepcolor.methods import create_method_entry, available_method_names


def test_create_method_entry():
    expected = {
        "method_name": "A",
        "short": "B",
        "description": "C",
        "url": None,
    }

    assert create_method_entry("A", "B", "C") == expected

    expected = {
        "method_name": "A",
        "short": "B",
        "description": "C",
        "url": "D",
    }

    assert create_method_entry("A", "B", "C", "D") == expected


def test_available_method_names():
    assert ["richzhang", "colornet", "zeruniverse"] == available_method_names()
