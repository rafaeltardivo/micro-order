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
        return 'Order {} made at {} customer id {} status {}.'.format(
            self.id,
            self.customer,
            self.made_at,
            self.status
        )
