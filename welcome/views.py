from django.shortcuts import render
from django.http import HttpResponse
from django.utils.translation import gettext_lazy as _
from django.utils.translation import gettext, get_language, activate

# Create your views here.

def test(request):
    trans = translate('who are you?')
    return render(request, 'welcome/welcome1.html',{'trans':trans})
def translate(language):
    cur_lang = 'es'
    activate(cur_lang)
    text = gettext(language)
    return text


