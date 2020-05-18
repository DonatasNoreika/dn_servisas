from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('uzsakymai/', views.uzsakymai, name='uzsakymai'),
    path('uzsakymai/<int:uzsakymas_id>', views.uzsakymas, name='uzsakymas'),
]