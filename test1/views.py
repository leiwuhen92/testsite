from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
import time
from django.utils.translation import ugettext as _


def test1_view(request):
    t = time.localtime()
    n = t[6]

    #weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    # weekdays = [_('Monday'), _('Tuesday'), _('Wednesday'), _('Thursday'),_('Friday'), _('Saturday'), _('Sunday')]
    # return HttpResponse(weekdays[n])

    weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    return HttpResponse(_(weekdays[n]))
