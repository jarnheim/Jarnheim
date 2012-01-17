from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from dateutil.relativedelta import relativedelta

class Ban( models.Model ):
    id = models.AutoField( primary_key = True )
    user = models.ForeignKey( User,
                              verbose_name="User",
                              related_name="banned_user",
                              blank=False,
                              unique=False)
    banned_by = models.ForeignKey( User,
                                   verbose_name="Banned By",
                                   related_name="banned_by_user",
                                   blank=False,
                                   unique=False)
    ip_address = models.IPAddressField(verbose_name="IP Address",
                                       blank=False,
                                       unique=False)
    start_dtm = models.DateTimeField(verbose_name="Start Date",
                                     blank=False,
                                     default=datetime.today(),
                                     unique=False)
    end_dtm = models.DateTimeField(verbose_name="End Date",
                                   blank=False,
                                   default=(datetime.today() +
                                            relativedelta( months=+1 )),
                                   unique=False)
    permaban = models.BooleanField(verbose_name="Permaban",
                                   blank=False,
                                   default=False,
                                   unique=False)
    reason = models.TextField(verbose_name="Reason",
                              blank=True,
                              unique=False)
    notes = models.TextField(verbose_name="Notes",
                             blank=True,
                             unique=False)

    def __unicode__( self ):
        return "%s %s (%s-%s)" % (self.user.first_name,
                                  self.user.last_name,
                                  self.start_dtm,
                                  self.end_dtm)

    class Meta:
        ordering = ["-end_dtm", "-start_dtm"]
        unique_together = ("user", "start_dtm")

