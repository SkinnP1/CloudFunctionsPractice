from flask import escape
import functions_framework

@functions_framework.http
def hello_nigel(request):
    """HTTP Cloud Function.
    Args:
        request (flask.Request): The request object.
        <https://flask.palletsprojects.com/en/1.1.x/api/#incoming-request-data>
    Returns:
        The response text, or any set of values that can be turned into a
        Response object using `make_response`
        <https://flask.palletsprojects.com/en/1.1.x/api/#flask.make_response>.
    """
    request_json = request.get_json(silent=True)
    request_args = request.args
    a = 5 
    if request_json and 'fname' in request_json and 'lname' in request_json:
        fname = request_json['fname']
        lname = request_json['lname']
    elif request_args and 'fname' in request_args and 'lname' in request_args :
        fname = request_args['fname']
        lname = request_args['lname']
    else:
        fname = 'World'
        lname = 'Piyush'
    return 'Hello {} {}!'.format(escape(fname), escape(lname))