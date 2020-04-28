from django.db import models


class Shipping(models.Model):
    """Model definition for Shipping."""
    PROCESSING = 1
    SUCESS = 2
    FAIL = 3

    STATUS_CHOICES = [
        (PROCESSING, "PROCESSING"),
        (SUCESS, "SUCESS"),
        (FAIL, "FAIL"),
    ]
    order = models.PositiveIntegerField()
    shipped_at = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS_CHOICES, default=PROCESSING)

    class Meta:
        verbose_name = 'shipping'
        verbose_name_plural = 'shippings'

    def __str__(self):
        """Unicode representation of Shipping."""
        return 'Shipping {} order {} shipped_at {} status {}'.format(
            self.id,
            self.order,
            self.shipped_at,
            self.status
        )
