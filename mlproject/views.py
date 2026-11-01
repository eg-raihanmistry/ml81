from django.http import HttpResponse
from django.shortcuts import render
from django.conf import settings
import os
import pickle

model_path = os.path.join(settings.BASE_DIR, 'crop_prediction_model.pkl')
with open(model_path, "rb") as file:
    model = pickle.load(file)

def home(request):
    predict = None
    if request.method == "POST":
        temperature = float(request.POST['temperature'])
        humidity = float(request.POST['humidity'])
        ph = float(request.POST['ph'])
        water_avalilablity = float(request.POST['water_avalilablity'])
        season = float(request.POST['season'])

        data = [[ temperature, humidity, ph, water_avalilablity, season ]]
        predict = model.predict(data)

    payload = {
        'predict' : predict
    }

    return render(request, "index.html", payload)