from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.http import HttpResponseRedirect

from foodproject.files.models import Entry

from time import gmtime, strftime, localtime, mktime, time
import os
import string
import re
import array

PATH_SERVER = '/Users/tgl'
PATH_WWW = '/files'
PATH_ADMIN = '/admin/files'

def index(request):
    path = PATH_SERVER + request.path.replace(PATH_WWW, '', 1)
    
    list = os.listdir(path)
    
    dotdot = Entry(path + "/..")
    
    listing = [dotdot]
    for entry in list:
        listing.append(Entry(path + entry))
        
    return render_to_response('files/index.html', {'list' : listing, 
                                                   'cwd' : path,
                                                   'path' : path.replace(PATH_SERVER, '', 1)})
         
def delete(request):
    path = PATH_SERVER + request.path.replace('/files/delete', '', 2)

    if os.path.isfile(path) or os.path.isdir(path):
        os.remove(path)

    return HttpResponse('OK')

def download(request):
    base = "/Users/tgl"

    cwd = PATH_SERVER + request.path.replace("/download", "", 1)

    entry = Entry(cwd)
    
    f = open(entry.path, 'rb')
 
    return HttpResponse(f, mimetype='application/octet-stream') 

def mkdir(request):
    redirect_url =  request.path.replace("/mkdir", '', 1)
    
    if request.POST:
        if request.POST.get('directory[name]'):
            path = PATH_SERVER + request.path.replace('/files/mkdir', '', 1) + request.POST.get('directory[name]').lower()
            try:
                os.mkdir(path)
                os.chmod(path, 0775)
                
            except OSError, (errno, strerror):
                error = errno
        
            if request.POST.get('submit_btn') != 'Create':
                redirect_url = path.replace(PATH_SERVER, PATH_WWW, 1)

    return HttpResponseRedirect(redirect_url) 

def rename(request):
    result = request.path.replace('/rename', '', 1)
    
    if request.method == 'POST':
        new_name = request.POST['rename[new_name]']
        old_name = request.POST['file[original_name]']
        
        source = request.POST['file[original_path]']
        target = source.replace(old_name, new_name, 1)
        
        os.rename(source, target) 
    
        result = result.replace(old_name, "", 1)
    
    return HttpResponseRedirect(result)
  
def upload(request):
    redirect_url = request.path.replace(PATH_SERVER, '', 1)

    dir_name = redirect_url.replace('/files/upload', '', 1)
    
    redirect_url = redirect_url.replace('/upload', '', 1)
    
    path = PATH_SERVER + dir_name + '/'
    
    if request.method == 'POST':
        if request.FILES:
            for file in request.FILES.getlist('incoming[file]'):
                filename = file['filename']
                fileExists = 'false'
            
                dir_list = os.listdir(path)
                for entry in dir_list:
                    if filename == entry:
                        fileExists = 'true'
            
                if fileExists == 'false':
                    file = file['content']
                    length = len(file)

                    thispath = path + filename
                    f = open(thispath, 'wb')
                    f.write(file)
                    os.chmod(thispath, 0664)
                    f.close()
                
    return HttpResponseRedirect(redirect_url)
 
 