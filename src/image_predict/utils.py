from flask import make_response, Request
import base64
import numpy as np
import cv2
import requests

def build_response(content, status_code: int = 200):
    response = make_response({"content": content}, status_code)
    response.headers.add("Access-Control-Allow-Origin",
                        "*")
    response.headers.add('Access-Control-Allow-Headers', "*")
    response.headers.add('Access-Control-Allow-Methods', "*")
    response.headers.add("Content-Type", "image/png") # multipart/form-data
    return response

def image_from_string(buffer):
    img_str = buffer.read()
    image_np = np.frombuffer(img_str, np.uint8)
    img_np = cv2.imdecode(image_np, cv2.IMREAD_COLOR)
    print("IMAGE SHAPE", img_np.shape)
    return img_np

def image_to_string(img):
    img_str = cv2.imencode('.png', img)[1].tostring()
    return base64.b64encode(img_str).decode("utf-8")

def get_request_input(request: Request, key="content", default=""):
    print("external IP:", requests.get('https://ident.me').content)
    status_code = 200
    request_json = request.get_json()
    
    if request.args and key in request.args:
        return request.args.get(key), status_code
    elif request_json and key in request_json:
        return request_json[key], status_code
    else:
        print("params not defined, defaulting to {}".format(
            key))
        status_code = 204
        
        return key, status_code