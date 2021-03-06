from django.db import models
from django.utils.translation import ugettext_lazy as _

from finalProject.account.models import User
from finalProject.shipper.models import Load


class CarrierUser(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='carrier_user')
    MC_number = models.IntegerField(
        _('MC number'), null=False, blank=False, unique=True)

    def __str__(self):
        return "carrier id: {}, User id: {}, Name: {}, MC Number: {}".format(
            self.pk, self.user.pk, self.user.first_name, self.MC_number
        )


class RejectedLoad(models.Model):
    load = models.ForeignKey(Load, on_delete=models.CASCADE)
    carrier = models.ForeignKey(CarrierUser, on_delete=models.CASCADE)

    def __str__(self):
        return "Load: {}, Carrier: {}".format(self.load, self.carrier)
