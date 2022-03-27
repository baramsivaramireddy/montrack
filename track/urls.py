
from django.urls import path,include
from . import views 
urlpatterns = [
   
    path('',views.index),
    path('stat',views.stat),
    path('add',views.add_view),
    path('api/add',views.add),
    path('logout',views.logout_view),
    
    path('took',views.all_took),
    
    path('stats',views.all_stats),
    path('gave',views.all_gave),
    path('expenses',views.expenses_view),
   
]
