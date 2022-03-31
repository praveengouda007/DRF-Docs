from django.urls import path
from snippets import views
from rest_framework.urlpatterns import format_suffix_patterns

# urlpatterns = format_suffix_patterns([
#     path('snippets/', views.SnippetList.as_view(), name='snippets-list'),
#     path('snippets/<int:pk>/', views.SnippetDetails.as_view(), name='snippets-detail'),
#     path('users/', views.UserList.as_view(), name='user-list'),
#     path('users/<int:pk>/', views.UserDetail.as_view(), name='user-detail'),
#     path('', views.api_root),
#     path('snippets/<int:pk>/highlight/', views.SnippetHighlight.as_view(), name='snippets-highlight'),
# ])


"""
Binding ViewSets to urls explicitly
"""
# from snippets.views import SnippetViewSet, UserViewSet, api_root
# from rest_framework import renderers
#
# snippets_list = SnippetViewSet.as_view({
#     'get': 'list',
#     'post': 'create'
# })
#
# snippets_detail = SnippetViewSet.as_view({
#     'get': 'retrieve',
#     'put': 'update',
#     'patch': 'partial_update',
#     'delete': 'destroy'
# })
# snippets_highlight = SnippetViewSet.as_view({
#     'get': 'highlight'
# }, renderer_classes=[renderers.StaticHTMLRenderer])
#
# user_list = UserViewSet.as_view({
#     'get': 'list'
# })
# user_detail = UserViewSet.as_view({
#     'get': 'retrieve'
# })
# urlpatterns = format_suffix_patterns([
#     path('', api_root),
#     path('snippets/', snippets_list, name='snippets-list'),
#     path('snippets/<int:pk>/', snippets_detail, name='snippets-detail'),
#     path('snippets/<int:pk>/highlight/', snippets_highlight, name='snippets-highlight'),
#     path('users/', user_list, name='user-list'),
#     path('users/<int:pk>/', user_detail, name='user-detail')
# ])

"""
Using Routers
"""
from django.urls import path, include
from rest_framework import routers
from snippets import views

# Creating a router and register our viewsets with it.
router = routers.DefaultRouter()
router.register(r'snippets', views.SnippetViewSet, basename="snippets")
router.register(r'users', views.UserViewSet, basename="users")

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
]
