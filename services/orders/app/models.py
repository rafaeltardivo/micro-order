from django.db import models


class Order(models.Model):
    """Model definition for Order."""
    PROCESSING = 1
    SHIPPED = 2
    CANCELLED = 3

    STATUS_CHOICES = [
        (PROCESSING, "PROCESSING"),
        (SHIPPED, "SHIPPED"),
        (CANCELLED, "CANCELLED"),
    ]
    customer = models.PositiveIntegerField()
    made_at = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS_CHOICES, default=PROCESSING)

    class Meta:
        """Meta definition for Order."""
        verbose_name = 'order'
        verbose_name_plural = 'orders'

    def __str__(self):
        """Unicode representation of Order."""
        return (
            f'{self.pk} - made at {self.made_at} by customer'
            f'{self.customer}. Status: {self.status}'
        )

    def __repr__(self):
        """Unambiguous representation of an Order."""
        return (
            f'{self.__class__.__name__}'
            f'({self.pk},{self.customer},{self.made_at},{self.status})'
        )
