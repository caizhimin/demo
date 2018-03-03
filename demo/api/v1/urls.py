from django.conf.urls import url

from . import views

urlpatterns = [
    url(
        regex=r'^echo$',
        view=views.echo,
        name='/api/v1/echo'
    ),

]
