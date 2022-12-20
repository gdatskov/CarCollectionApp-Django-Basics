from django.urls import path, include

from car_collection.car_collection_app.views import *

"""
•	http://localhost:8000/ - index page
•	http://localhost:8000/catalogue/ - catalogue page
•	http://localhost:8000/car/create/ - car create page
•	http://localhost:8000/car/<car-id>/details/ - car details page
•	http://localhost:8000/car/<car-id>/edit/ - car edit page
•	http://localhost:8000/car/<car-id>/delete/ - car delete page
•	http://localhost:8000/profile/create - profile create page
•	http://localhost:8000/profile/details/ - profile details page
•	http://localhost:8000/profile/edit/ - profile edit page
•	http://localhost:8000/profile/delete/ - profile delete page
"""

urlpatterns = [
    path('', index, name='index'),
    path('catalogue/', catalogue, name='catalogue'),
    path('car/',
         include([
             path('create/', create_car, name='create_car'),
             path('<int:pk>/',
                  include([
                      path('details/', car_details, name='car_details'),
                      path('delete/', delete_car, name='delete_car'),
                      path('edit/', car_edit, name='car_edit'),
                  ]))
         ])),
    path('profile/',
         include([
             path('create/', create_profile, name='create_profile'),
             path('details/', profile_details, name='profile_details'),
             path('edit/', edit_profile, name='edit_profile'),
             path('delete/', delete_profile, name='delete_profile'),
         ])),

]
