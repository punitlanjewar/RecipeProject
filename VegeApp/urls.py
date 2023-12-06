from django.conf import settings
from django.urls import path
from VegeApp import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static

urlpatterns = [
    path('', views.recipes, name='recipes'),
    path('delete-recipe/<int:id>', views.delete_recipe, name='delete-recipe'),
    path('update-recipe/<int:id>', views.update_recipe, name='update-recipe'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)