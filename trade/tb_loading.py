from http import client
from matplotlib.pyplot import table
from rest_framework import serializers
from django.core import serializers
from django.http import HttpResponse
from .models import *

class GetTable:
    tableDB = {
        'getClient' : Client,
        'getClientTrade' : ClientTrade,
        'getFix' : Fix,
        'getFixCost' : FixCost,
        'getRoyalty' : Royalty,
        'getRant' : Rant,
        'getRantPay' : RantPay,
        'getEtc' : Etc,
        'getEtcPay' : EtcPay,
        'getManage' : Manage,
    }
    

        

    # def getTable(request):
    #     name = request
    #     key = request.GET.get("key")
    #     data = .objects.filter(id=key)
    #     post_list = serializers.serialize('json', data)
    #     return HttpResponse(post_list, content_type="text/json-comment-filtered")
