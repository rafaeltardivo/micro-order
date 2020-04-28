from django.db import models

class Shipping(models.Model):
    """Model definition for Shipping."""
    order = models.PositiveIntegerField()
    shipped_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'shipping'
        verbose_name_plural = 'shippings'

    def __str__(self):
        """Unicode representation of Shipping."""
        return 'Shipping {} made at {} associated to order id {}'.format(
            self.id,
            self.made_at,
            self.order
        )