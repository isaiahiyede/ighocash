from django.urls import path
from . import views

urlpatterns = [
    path("", view=views.IndexView.as_view(), name="web.index"),
    path("about/", view=views.AboutView.as_view(), name="web.about"),
    path("contact/", view=views.ContactView.as_view(), name="web.contact"),
    path("services/capacity-development", view=views.CapacityView.as_view(), name="web.services.capacity"),
    path("services/analytics-modelling", view=views.AnalyticsView.as_view(), name="web.services.analytics"),
    path("sme/", view=views.SmeLoanView.as_view(), name="web.sme"),
    path("silver/", view=views.SilverLoanView.as_view(), name="web.silver"),
    path("gold/", view=views.GoldLoanView.as_view(), name="web.gold"),
    path("diamond/", view=views.DiamondLoanView.as_view(), name="web.diamond"),
    path("industries/", view=views.IndustriesView.as_view(), name="web.industries"),
]