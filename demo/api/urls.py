from django.conf.urls import url, include
app_name = 'api'

urlpatterns = [
    url(r'^v1/', include('demo.api.v1.urls')),
]
