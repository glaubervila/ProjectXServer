from advertising import views as advertising_views
from rest_framework import routers

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()

router.register(r'product', advertising_views.ProductViewSet)
