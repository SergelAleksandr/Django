from django.contrib import admin
# from .models import Parsing_string
from .models import Parsing_ip
from .models import Parsing_browser
from .models import Parsing_date

# Register your models here.

admin.site.register(Parsing_browser)
admin.site.register(Parsing_date)
admin.site.register(Parsing_ip)
# admin.site.register(Parsing_string)