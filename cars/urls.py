from django.urls import path

from cars.views import index, show_car, create_advertisement, delete_car, edit_car, report_view, delete_report

urlpatterns = [
    path('', index, name='index'),
    path('car/<int:pk>', show_car, name='show car'),
    path('add/', create_advertisement, name='add car'),
    path('delete_car/<int:pk>', delete_car, name='delete car'),
    path('edit/<int:pk>', edit_car, name='edit car'),
    path('reports/', report_view, name='reports'),
    path('remove_report/<int:pk>', delete_report, name='remove report')
]
