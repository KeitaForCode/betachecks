from django.conf.urls import url
from betterchecks_app import views


app_name = 'betterchecks_app'

urlpatterns = [
    url(r'^$',views.Fakenews.as_view(), name='fakenews'),
    url(r'^betterchecks_app/$',views.Factchecking.as_view(), name='factchecking'),
    url(r'^training/$',views.Training, name='training'),
    url(r'^inforesearch360/$', views.InfoResearch, name='inforesearch'),
    url(r'^infodemic/$', views.Infodemic, name='infodemic'),
    url(r'^contact/$', views.Contacts, name='contacts'),
    url(r'^factcheck/$', views.FactCheck, name='factcheck'),
    url(r'^moneytrail/$', views.MoneyTrail, name='moneytrail'),
    url(r'^shadyspotlight/$', views.ShadySpotlight, name='shadyspotlight'),
    url(r'^coronavirus/$', views.Coronavirus.as_view(), name='coronavirus'),
    url(r'^privacy/$', views.PrivacyPolicy.as_view(), name='privacy'),
]