import array
import os
from django.shortcuts import render_to_response
from foodproject.files.models import Entry

def index(request):
    base = "/Users/tgl"

    cwd = base + request.path.replace("/files", "", 1)

    if os.path.isfile(cwd):
        return render_to_response(cwd)
    
    else:
        list = os.listdir(cwd)
        
        dotdot = Entry(cwd + "/..")
    
        listing = [dotdot]
        for entry in list:
            listing.append(Entry(cwd + entry))
        
        return render_to_response('files/index.html', {'list' : listing, 'cwd' : cwd})
    