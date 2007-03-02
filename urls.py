from django.conf.urls.defaults import *

urlpatterns = patterns('',
    # Example:
    # (r'^foodproject/', include('foodproject.foo.urls')),
   (r'^files/.*$', 'foodproject.files.views.index'),
      
    # Uncomment this for admin:
#     (r'^admin/', include('django.contrib.admin.urls')),
)
