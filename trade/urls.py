from inspect import getclasstree
from django.urls import path
from . import tb_loading
from . import views

app_name = "trade"


urlpatterns = [    
    path('client/', views.client, name="client"),
    path('client/getclient', views.getTable, name="getClient"),
    path('client/trade', views.clientTrade, name="clientTrade"),
    path('client/trade/get', views.getTable, name="getClientTrade"),
    path('client/trade/edit', views.editTrade, name="editTrade"),
    path('client/trade/gettrade', views.getTrade, name="getTrade"),

    path('fix/', views.fix, name="fix"),
    path('fix/getFix', views.getTable, name="getFix"),
    path('fix/cost', views.fixCost, name="fixCost"),
    path('fix/cost/getCost', views.getTable, name="getFixCost"),

    path('manage/', views.manage, name="manage"),

    path('royalty/', views.royalty, name="royalty"),
    path('royalty/getRoyalty', views.getTable, name="getRoyalty"),

    path('rant/', views.rant, name="rant"),
    path('rant/getrant', views.getTable, name="getRant"),
    path('rant/pay', views.rantPay, name="rantPay"),
    path('rant/pay/getRantPay', views.getTable, name="getRantPay"),

    path('etc/', views.etc, name="etc"),
    path('client/getetc', views.getTable, name="getEtc"),

    path('etc/pay', views.etcPay, name="etcPay"),
    path('etc/pay/getPay', views.getTable, name="getEtcPay"),

]
