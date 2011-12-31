from django.db import models
from django.contrib.auth.models import User

# models
class character( models.Model ):
    # auto-fields
    id = models.AutoField( primary_key = True )
    user = models.OneToOneField( User )
    create_dtm = models.DateTimeField()

    #  character specific fields
    name = models.CharField( max_length = 30 )
    birthday = models.DateField()
    bodyweight_kg = models.DecimalField( max_digits = 7, decimal_places = 3 )
    height_cm = models.DecimalField( max_digits = 7, decimal_places = 3 )

    # character classes
    race = models.ForeignKey( 'race' )

    def __unicode__( self ):
        return self.name

    class Meta:
        db_table = 'rpf_character'
        app_label= 'rpf'