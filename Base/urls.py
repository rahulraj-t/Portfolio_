from django.urls import path
from . import views

# urlpatterns = [

#     path('',views.contact,name='contact'),
# ]

urlpatterns = [
    path("api/contact/", views.contact_api, name="contact_api"),
    path("contacts/", views.contacts, name="contacts"),
]