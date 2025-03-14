from django.contrib import admin

# Register your models here.
from myapp.models import Contract, Property, WorkGenM, BuildsecM, ElectsectionM, CivilsectionM, UserProfile

from django.contrib import admin


# login
# LGCVault
# pws:q123456789q
admin.site.site_header = "MANGU LGC"  # Changes the header
admin.site.site_title = "MANGU LGC"  # Changes the browser title
admin.site.index_title = "Welcome to MANGU LGC"  # Changes the dashboard title

admin.site.register(Contract)
admin.site.register(Property) # Register the model



admin.site.register(WorkGenM)
admin.site.register(BuildsecM) # Register the model
admin.site.register(ElectsectionM)
admin.site.register(CivilsectionM) #
admin.site.register(UserProfile)