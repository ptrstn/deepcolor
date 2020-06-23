def create_method_entry(identifier, module, name, description, url=None):
    return {
        "id": identifier,
        "method": module,
        "name": name,
        "description": description,
        "url": url,
    }


def available_methods():
    return [
        create_method_entry(
            "richzhang", "Richard Zhang", "Colorful Image Colorization by Richard Zhang"
        ),
        create_method_entry(
            "zeruniverse",
            "Richard Zhang",
            "Colorful Image Colorization by Richard Zhang",
        ),
    ]
