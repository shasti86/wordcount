from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from collections import OrderedDict
import re

# Create your views here.


def home(request):
    print request
    return render_to_response('index.html')

@csrf_exempt
def search(request, input_text=None):
    input_text = request.POST['input_text']
    words = [w.strip() for w in re.findall(r'\b.*?\S.*?(?:\b|$)', input_text)]
    result = dict()
    for word in words:
        try:
            result[word] += 1
        except:
            result[word] = 1

    return render_to_response('index.html', {'result': result})