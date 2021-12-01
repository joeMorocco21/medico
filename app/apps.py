from flask import Flask, render_template, request, Response, redirect
from flask import jsonify
import io
import os
import string
import torch
import pandas as pd
from torch._C import device
import torchvision as tv
import torch.nn as nn
import torchvision.transforms as transforms
from torchvision import models
from PIL import Image
from mednet import MedNet
    # Modelling Task
model = torch.load('mdl',map_location=torch.device('cpu'))
model.eval()
classNames = ["AbdomenCT", "BreastMRI", "ChestCT", "CXR", "Hand", "HeadCT"]

#path='C:\\Users\\Joe\\Desktop\py\\bref11\\application\\app\\static\\upload\\000000.jpeg'
def scaleImage(y):          
        if(y.min() < y.max()):  
            y = (y - y.min())/(y.max() - y.min()) 
        z = y - y.mean()        
        return z
def predict(file):
        img = Image.open(file)
        my_transforms = transforms.Compose([transforms.ToTensor(),transforms.Resize(64),transforms.Normalize([0.5 ],[0.5 ])])
        xtest= my_transforms(img).unsqueeze(0)
        xtest=scaleImage(xtest)
        yOut = model(xtest)
        indices = yOut.max(1)[1].tolist()[0]
        pred = classNames[indices]
        df = pd.DataFrame([pred])
        return Response(df.to_json(orient="records"), mimetype='application/json')

