from django.db import models
from django.http import HttpResponse
import json

# Create your models here.
class WordVector():
    def calc(self, request, model):
        print('-------------------------------')
        data =''
        try:
            data = json.loads(request.body)
        except:
            data =''
        print(data)

        posiData = data['Positive']
        negaData = data['Negative']

        results = []
        try:
            if posiData and negaData:
                results = model.wv.most_similar(positive=posiData,negative=negaData)
            elif posiData:
                results = model.wv.most_similar(positive=posiData)
            elif negaData:
                results = model.wv.most_similar(negative=negaData)
        except:
            results = []


        res_json = json.dumps(results, ensure_ascii=False)
        return HttpResponse(res_json)
