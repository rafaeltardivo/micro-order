from django.db import models

from django.db import models

class Order(models.Model):
    """Model definition for Order."""
    customer = models.PositiveIntegerField()
    made_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        """Meta definition for Order."""
        verbose_name = 'order'
        verbose_name_plural = 'orders'

    def __str__(self):
        """Unicode representation of Order."""
        return 'Order {} made at {} by customer id {}'.format(
            self.id,
            self.made_at,
            self.customer
        )


