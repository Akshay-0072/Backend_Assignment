
from django.urls import path,include
from accounts.views import AccountsListView,AccountsDetailView

urlpatterns = [
    path('', AccountsListView.as_view(),name='list-view'),
    path('<int:id>/', AccountsDetailView.as_view(),name='detail-view'),
]
