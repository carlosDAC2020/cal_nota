from django.urls import path
from . import views

app_name="final_note"

urlpatterns = [
    path('',views.index, name='index'),
    path('calcular/',views.calcular_nota, name='calcular')
]