from django.db import models


class Customer(models.Model):
    """Model definition for Customer."""
    email = models.EmailField(max_length=254)
    address = models.CharField(max_length=254)

    class Meta:
        """Meta definition for Customer."""

        verbose_name = 'Customer'
        verbose_name_plural = 'Customers'

    def __str__(self):
        """Unicode representation of Customer."""
        return 'Customer {} email {} address {}'.format(
            self.id,
            self.email,
            self.address
        )
