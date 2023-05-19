from utils import build_response, get_request_input

def hello_world(request):
    """Responds to any HTTP request.
    Args:
        request (flask.Request): HTTP request object.
    Returns:
        The response text or any set of values that can be turned into a
        Response object using
        `make_response <http://flask.pocoo.org/docs/1.0/api/#flask.Flask.make_response>`.
    """
    res, status_code = get_request_input(request, "content", "H")

    res += " another string"
    
    return build_response(res, status_code)