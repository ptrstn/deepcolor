from django.db import models


class DeepColorResult(models.Model):
    """
    Stores the original black and white image and the colored image.
    """

    original = models.ImageField(blank=False, null=False)
    colored = models.ImageField(blank=False, null=False)
    strategy = models.CharField(max_length=20, blank=False, null=False)

    def __str__(self):
        return (
            f"{self.id} {self.original.name} -> {self.colored.name} <{self.strategy}>"
        )
