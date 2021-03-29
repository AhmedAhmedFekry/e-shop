from django.urls import path
from order import views

urlpatterns = [
    path("create/", views.order_create, name="order_create"),
    path(
        "admin/order/<int:order_id>/",
        views.admin_order_detail,
        name="admin_order_detail",
    ),
    # path("pdf_view/<int:order_id>/", views.ViewPDF.as_view(), name="pdf_view"),
    # path("pdf_download/", views.DownloadPDF.as_view(), name="pdf_download"),
]
