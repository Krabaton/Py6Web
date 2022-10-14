from django.urls import path
from . import views

urlpatterns = [
    path("", views.main, name='main'),
    path("losses/actual", views.get_losses_actual, name="getlossesactual"),
    path("losses/list", views.losses_list, name="losseslist"),
    path("sync/", views.sync_losses_list, name="lossessync"),
    path("chart/<int:id>", views.get_chart, name="lossessync"),
    path("chart-info/<int:id>", views.get_chart_info),
    path("chart-info/<int:id>/<int:day>", views.get_chart_info),
    path("chart-info/<int:id>/<int:day>/<int:month>", views.get_chart_info),
]
