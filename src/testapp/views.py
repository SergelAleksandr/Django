from django.shortcuts import render
from django.http import HttpResponse
# from .models import Parsing_string
from .models import Parsing_ip
from .models import Parsing_browser
from .models import Parsing_date
# from .pars import pars_all

# Create your views here.



def pars(request):
   
    # line = Parsing_string.objects.all()
    ip_line = Parsing_ip.objects.all()
    brow_line = Parsing_browser.objects.all()
    date_obj = Parsing_date.objects.all()

    context = {'ip_line' : ip_line, 'brow_line' : brow_line, 'date_obj' : date_obj}
    return render(request, template_name="parsing.html", context=context)
    