from django.db import models

class race( models.Model ):
    id = models.AutoField( primary_key = True )
    create_dtm = models.DateTimeField()
    name = models.CharField( max_length = 30 )

    def __unicode__( self ):
        return self.name

    class Meta:
        db_table = 'rpf_race'
        app_label= 'rpf'