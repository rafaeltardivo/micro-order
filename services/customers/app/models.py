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
        return f'{self.pk} - {self.email} who lives at {self.address}'

    def __repr__(self):
        """Unambiguous representation of a Customer."""
        return (
            f'{self.__class__.__name__}'
            f'({self.pk},{self.email},{self.address})'
        )
