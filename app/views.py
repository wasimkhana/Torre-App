from app import app


@app.route('/')
def hello_world():
    """
    hello_world function to test route.
    return: 'Hello World!'
    """
    return 'Hello World!'
