from django.db import models


class Shipping(models.Model):
    """Model definition for Shipping."""
    PROCESSING = 0
    SUCCESS = 1
    FAIL = 2

    STATUS_CHOICES = [
        (PROCESSING, "PROCESSING"),
        (SUCCESS, "SUCCESS"),
        (FAIL, "FAIL"),
    ]
    order = models.PositiveIntegerField()
    shipped_at = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS_CHOICES, default=PROCESSING)

    class Meta:
        verbose_name = 'Shipping'
        verbose_name_plural = 'Shippings'

    def __str__(self):
        """Unicode representation of Shipping."""
        return (
            f'{self.pk} - shipped at {self.shipped_at} associated to'
            f' {self.order}. Status {self.status}'
        )

    def __repr__(self):
        """Unambiguous representation of a Shipping."""
        return (
            f'{self.__class__.__name__}'
            f'({self.pk},{self.order},{self.shipped_at},{self.status})'
        )
