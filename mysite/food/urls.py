from . import views
from django.urls import path

app_name = 'food' #namespacing the url boz many people may work in same project
urlpatterns = [
     # IndexClassView is the class based list view
    path('',views.IndexClassView.as_view(),name='index'), #localhost/food
    path('<int:pk>/',views.FoodDetail.as_view(),name='detail'),#localhost/food/1
    path('item/',views.item,name='item'), #localhost/food/item
    # add items
    path('add',views.create_item,name='create_item'),
    path('update/<int:id>/',views.update_item,name='update_item'),
    path('delete/<int:id>/',views.delete_item,name='delete_item'),

]
#if done like below then need to add in main url file of project mysite too
# urlpatterns = [
#     path('',views.bye,name='bye'),
# ]