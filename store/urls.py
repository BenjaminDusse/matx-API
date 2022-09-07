from rest_framework_nested import routers

from store import views

router = routers.DefaultRouter()
router.register('collections', views.CollectionViewSet, basename='collections')
# router.register('collections', views.CollectionViewSet, basename='collection')
# router.register('carts', views.CartViewSet, basename="carts")
# router.register('customers', views.CustomerViewSet, basename="customers")

# products_router = routers.NestedDefaultRouter(router, 'products', lookup='product')
# products_router.register('reviews', views.ReviewViewSet, basename='product-reviews')

# carts_router = routers.NestedDefaultRouter(router, 'carts',
#                                            lookup='cart')  # lookup bu get_queryset funcda cart_id ga tablitsadan userni idsini olayapman
# carts_router.register('items', views.CartItemViewSet, basename='cart-items')


# URL conf
urlpatterns = router.urls
