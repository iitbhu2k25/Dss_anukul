from django.urls import path
from . import views

app_name="gwm"
urlpatterns = [
  path('groundwater/',views.groundwater,name="groundwater_page"), 

  path('get_raster_file/', views.get_raster_file, name='get_raster_file'),

]