class CaffeNotFoundError(ModuleNotFoundError):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if self.args:
            self.message = args[0]
        else:
            self.message = None

        self.instructions = (
            "Caffe is not installed. Unable to colorize picture.\n"
            "Check https://caffe.berkeleyvision.org/installation.html for instructions."
        )

    def __str__(self):
        if self.message:
            return f"{self.message}. {self.instructions}"
        return f"{self.instructions}"
