from django.conf.urls import url
from scrap import views

urlpatterns = [
    url(r'^$', views.index, name = 'index'),
    url(r'^questao1$', views.questao1, name = 'questao1'),
	url(r'^questao2$', views.questao2, name = 'questao2'),
	url(r'^questao3$', views.questao3, name = 'questao3'),
	url(r'^questao4$', views.questao4, name = 'questao4'),
]


