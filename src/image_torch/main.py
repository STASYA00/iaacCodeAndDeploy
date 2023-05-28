from flask import make_response
import functions_framework
import cv2
import torch
from utils import *

@functions_framework.http
def run(request):
    """Responds to any HTTP request.
    Args:
        request (flask.Request): HTTP request object.
    Returns:
        The response text or any set of values that can be turned into a
        Response object using
        `make_response <http://flask.pocoo.org/docs/1.0/api/#flask.Flask.make_response>`.
    """
    files = request.files.to_dict()
    for file_name, file1 in files.items():
        print(file1)
        print(file_name)
        img = image_from_string(file1)
        break

    img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    model = torch.hub.load('ultralytics/yolov5', "yolov5l")
    res = model(img)
    cat = res.xywh[0][:, -1]
    res = {"categories": [res.names[int(x)] for x in cat]}
    res["image"] = image_to_string(img)
    
    return build_response(res, 200)

