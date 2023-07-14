# coding: UTF-8
from django.shortcuts import render
from django.http.response import HttpResponse
from tensorflow.python.keras.models import load_model
from PIL import Image, ImageFilter
import sys
from PIL import Image
from keras.models import load_model
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression


# Create your views here.
def index_template(request):
    return render(request, 'index.html')

def generic_template(request):
    return render(request, 'generic.html')

def elements_template(request):
    return render(request, 'elements.html')

def landing_template(request):
    return render(request, 'landing.html')





def predict_kork(request):
    if request.method == 'POST':
        name = request.FILES["kkimage"]
  
        image = Image.open(name)
        image = image.resize((64, 64))
        model = load_model("static/model.h5")
        np_image = np.array(image)
        np_image = np_image / 255
        np_image = np_image[np.newaxis, :, :, :]
        result = model.predict(np_image)
        if result[0][0] > result[0][1]:
            return render(request, 'result.html', {'result': "カブトムシ"})
            
        else:
            return render(request, 'result.html', {'result': "クワガタムシ"})


    return render(request, 'generic.html')





