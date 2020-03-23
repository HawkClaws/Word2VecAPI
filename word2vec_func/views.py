from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView
import word2vec_func
import functools
from gensim.models import word2vec

# Create your views here.
@csrf_exempt
def word2vec_calc(request):
    wordvector = word2vec_func.models.WordVector()
    model = get_model()
    return wordvector.calc(request, model)

@functools.lru_cache()
def get_model():
    return word2vec.Word2VecKeyedVectors.load_word2vec_format("./word2vec_func/wiki.model",binary=True)