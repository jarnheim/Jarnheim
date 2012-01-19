from django.db import models
from django.contrib.auth.models import User

class Ban( models.Model ):
    id = models.AutoField( primary_key = True )
    user = models.OneToOneField( User )
    ip_address = models.IPAddressField()
    start_dtm = models.DateTimeField()
    end_dtm = models.DateTimeField()
    permaban = models.BooleanField()
    reason = models.TextField()

    def __unicode__( self ):
        return self.user.name

    class Meta:
        db_table = 'rpf_ban'
        app_label= 'rpf'
