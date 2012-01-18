from characters.models import Character
from django.contrib import admin

class CharacterAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,          {'fields': ["name", "birthday",
                                    'create_dtm']}),
        ("Stats",       {'fields': ["gender",
                                    # "age",
                                    "bodyweight_kg",
                                    "bodyweight_uom",
                                    # "bodyweight",
                                    "height_cm",
                                    "height_uom",
                                    # "height",
                                    # "race",
                                    ]})]
    list_display = ("name", "bodyweight_kg", "height_cm", ) #"race")
    # list_filter = ["race"]

admin.site.register(Character, CharacterAdmin)
