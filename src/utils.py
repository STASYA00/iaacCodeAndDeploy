from flask import make_response

def build_response(content, status_code: int = 200):
    response = make_response({"content": content}, status_code)
    response.headers.add("Access-Control-Allow-Origin",
                        "*")
    response.headers.add('Access-Control-Allow-Headers', "*")
    response.headers.add('Access-Control-Allow-Methods', "*")
    return response