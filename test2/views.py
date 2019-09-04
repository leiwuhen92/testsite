from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.utils.translation import ugettext_lazy as _


def test2_view(request):
    code = _("The second sentence is from the Python code.");
    print(request.LANGUAGE_CODE)
    Context = {
        'lang': request.LANGUAGE_CODE,
        'code': code
    }
    return render(request,'test2/index.html',Context)

