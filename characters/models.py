from datetime import datetime
from django.db import models
from django.contrib.auth.models import User
from dateutil.relativedelta import relativedelta
from Jarnheim.util import convert_height
from Jarnheim.util import convert_weight
from Jarnheim.util import UNITS_OF_MEASURE_HEIGHT
from Jarnheim.util import UNITS_OF_MEASURE_WEIGHT
from Jarnheim.util import GENDER

class Character( models.Model ):
    id = models.AutoField( primary_key = True )
    user = models.OneToOneField( User,
                                 verbose_name="User",
                                 related_name="character_user",
                                 blank=False,
                                 unique=True)
    create_dtm = models.DateTimeField(verbose_name="Date created",
                                      db_index=False,
                                      blank=False,
                                      unique=False,
                                      default=datetime.today())

    #  character specific fields
    name = models.CharField( max_length = 30,
                             verbose_name = "User Name",
                             blank=False)
    birthday = models.DateField(verbose_name="Birthday",
                                blank=True,
                                unique=False,
                                db_index=True)
    gender = models.CharField("Gender",
                              max_length=3,
                              blank=False,
                              choices=GENDER,
                              db_index=True)
    bodyweight_kg = models.DecimalField( verbose_name="Bodyweight in Kg",
                                         max_digits = 7,
                                         decimal_places = 3,
                                         blank=False,
                                         default=0,
                                         db_index=True)
    bodyweight_uom = models.CharField( verbose_name="Bodyweight Unit of Measure",
                                       choices=UNITS_OF_MEASURE_WEIGHT,
                                       max_length=3)
    height_cm = models.DecimalField( verbose_name = "Height in cm",
                                     max_digits = 7,
                                     decimal_places = 3,
                                     default=0)
    height_uom = models.CharField( verbose_name="Height Unit of Measure",
                                   choices=UNITS_OF_MEASURE_HEIGHT,
                                   max_length=3)

    weight_uom = models.CharField( verbose_name="Weights Unit of Measure",
                                   choices=UNITS_OF_MEASURE_WEIGHT,
                                   max_length=3)
    # character classes
    # TODO: Update after race is set up
    # race = models.ForeignKey( 'race',
    #                           verbose_name="Race",
    #                           db_index=True)

    def height( self ):
        return convert_height(self.height_cm, self.height_uom)

    def weight( self ):
        return convert_weight(self.bodyweight_kg, self.bodyweight_uom)

    def age( self ):
        return datetime.today() - self.birthday

    def __unicode__( self ):
        return self.name

    class Meta:
        ordering = ["name"]
        verbose_name_plural = "characters"
        get_latest_by = "create_dtm"

