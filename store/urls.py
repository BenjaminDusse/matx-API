from rest_framework_nested import routers

from store import views

router = routers.DefaultRouter()
router.register('products', views.ProductViewSet, basename='products')
router.register('collections', views.CollectionViewSet, basename='collection')
router.register('carts', views.CartViewSet, basename="carts")
router.register('customers', views.CustomerViewSet, basename="customers")
router.register("orders", views.OrderViewSet, basename='orders')
products_router = routers.NestedDefaultRouter(router, 'products', lookup='product')
products_router.register('reviews', views.ReviewViewSet, basename='product-reviews')



carts_router = routers.NestedDefaultRouter(router, 'carts',
                                           lookup='cart')  # lookup bu get_queryset funcda cart_id ga tablitsadan userni idsini olayapman
carts_router.register('items', views.CartItemViewSet, basename='cart-items')


# URL conf
urlpatterns = router.urls + products_router.urls + carts_router.urls

# another way
# urlpatterns = [
#     path("", include("router.urls")
# ]

# urlpatterns = [
#     # path('products/', views.ProductList.as_view(), name="product_list"),
#     # path('products/<int:pk>/', views.ProductDetail.as_view(), name="product_detail"),
#     # path("collections/", views.CollectionList.as_view(), name="collection_list"),
#     # path("collections/<int:pk>/", views.CollectionDetail.as_view(), name='collection-detail')
#
#     # path('products/<int:id>/', views.ProductDetail.as_view(), name="product_detail"),
#     # path('products/', views.product_list, name="product_list"),
#     # path('products/<int:id>/', views.product_detail, name="product_detail"),
#     # path("collections/", views.collection_list, name="collection_list"),
#     # path("collections/<int:pk>/", views.collection_detail, name='collection-detail')
# ]

