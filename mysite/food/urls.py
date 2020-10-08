from . import views
from django.urls import path

app_name = 'food' #namespacing the url boz many people may work in same project
urlpatterns = [
     # IndexClassView is the class based list view
    # localhost/food
    path('', views.IndexClassView.as_view(), name='index'),
    #localhost/food/1
    path('<int:pk>/',views.FoodDetail.as_view(),name='detail'),
    #localhost/food/item
    path('item/',views.item,name='item'),
    # add items
    path('add',views.CreateItem.as_view(),name='create_item'),
    path('update/<int:id>/',views.update_item,name='update_item'),
    path('delete/<int:id>/',views.delete_item,name='delete_item'),

]
