from deepcolor.methods import create_method_entry, available_method_names


def test_create_method_entry():
    expected = {
        "method_name": "A",
        "description": "B",
        "url": None,
    }

    assert create_method_entry("A", "B") == expected

    expected = {
        "method_name": "A",
        "description": "B",
        "url": "C",
    }

    assert create_method_entry("A", "B", "C") == expected


def test_available_method_names():
    assert ['richzhang', 'colornet', 'zeruniverse'] == available_method_names()

