from django.conf.urls.defaults import *

urlpatterns = patterns('',
    # Example:
    # (r'^foodproject/', include('foodproject.foo.urls')),
   (r'^files/delete/.*$', 'foodproject.files.views.delete'),

   (r'^files/download/.*$', 'foodproject.filesviews.download'),

   (r'^files/mkdir/.*$', 'foodproject.files.views.mkdir'),

   (r'^files/rename/.*$', 'foodproject.files.views.rename'),
      
   (r'^files/upload/.*$', 'foodproject.files.views.upload'),

   (r'^files/.*$', 'foodproject.files.views.index'),

   (r'^images/(?P<path>.*)$', 'django.views.static.serve', {'document_root': '/Users/tgl/workspace/foodproject/templates/images'}),
   
   (r'^javascripts/(?P<path>.*)$', 'django.views.static.serve', {'document_root': '/Users/tgl/workspace/foodproject/templates/javascripts'}),

   (r'^stylesheets/(?P<path>.*)$', 'django.views.static.serve', {'document_root': '/Users/tgl/workspace/foodproject/templates/stylesheets'}),
   
    # Uncomment this for admin:
#     (r'^admin/', include('django.contrib.admin.urls')),
)
