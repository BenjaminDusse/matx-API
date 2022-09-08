from rest_framework.routers import DefaultRouter

from store import views

router = DefaultRouter()
router.register('collections', views.CollectionViewSet, basename='collections')
# router.register('collections', views.CollectionViewSet, basename='collection')
# router.register('carts', views.CartViewSet, basename="carts")
# router.register('customers', views.CustomerViewSet, basename="customers")

# products_router = routers.NestedDefaultRouter(router, 'products', lookup='product')

router.register('products', views.ProductViewSet, basename='products')



# carts_router = routers.NestedDefaultRouter(router, 'carts',
#                                            lookup='cart')  # lookup bu get_queryset funcda cart_id ga tablitsadan userni idsini olayapman
# carts_router.register('items', views.CartItemViewSet, basename='cart-items')


# URL conf
urlpatterns = router.urls
