from django.urls import path
from . import views
urlpatterns = [
    path('edit/<int:id>', views.EditPostView.as_view() , name = 'edit_post'),
    path('delete/<int:id>', views.DeletePostView.as_view() , name = 'delete_post'),
]