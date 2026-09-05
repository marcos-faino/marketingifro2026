from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('detalhe/servico/<int:pk>', views.ServicoDetailView.as_view(),
         name='servico_detalhe'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)