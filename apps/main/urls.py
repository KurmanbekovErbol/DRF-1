from rest_framework.routers import DefaultRouter
from apps.main.views import ProductMixins, СharacteristicAPI

router = DefaultRouter()

router.register(r'products', ProductMixins, basename='product')
router.register(r'characteristic', СharacteristicAPI, basename='api_characteristic')

urlpatterns = router.urls