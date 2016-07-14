from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import TemplateView

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('website.urls', namespace='website')),
    """
    url(r'^$',
        TemplateView.as_view(template_name='base.html'),
        name="add_invitation"
        ),
    """
]

from django.conf import settings
from django.conf.urls import static
urlpatterns += \
    static.static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
