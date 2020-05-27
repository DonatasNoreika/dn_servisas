from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('uzsakymai/', views.uzsakymai, name='uzsakymai'),
    path('uzsakymai/<int:uzsakymas_id>', views.uzsakymas, name='uzsakymas'),
    path('automobiliai/', views.AutomobiliaiView.as_view(), name='automobiliai'),
    path('automobiliai/<int:pk>', views.AutomobilisView.as_view(), name='automobilis'),
    path('manouzsakymai/', views.UzsakymaiByUserListView.as_view(), name='mano-uzsakymai')
]