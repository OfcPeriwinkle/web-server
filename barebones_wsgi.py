def run_application(application):
    """
    This is code implemented by a server for a WSGI application.

    A server is simply a process that creates a socket, binds that socket to a port, and listens
    for new connections on that socket.
    """

    # This is a header object that we'll populate with the headers from the WSGI app we're
    # going to be running. This is kinda like using a SleakSimulator, as long as the API
    # is fulfilled, we can abstract any details and just work on the results that are returned
    # to us. This is dependency injection in action!
    headers = []

    # Here is where we will store required state that WSGI apps can use to handle requests
    wsgi_env = {}

    # This is a function that is called to communicate state from the app back to us in server land
    def start_response(status, response_headers, exc_info=None):
        headers[:] = [status, response_headers]

    # This is where we honest to goodness run the application, note the callback we're passing
    result = application(wsgi_env, start_response)

    # From here we can create an HTTP response to send back across our connection with the client
    print(*headers)
    print(result)


def app(environ, start_response):
    """A bare-bones WSGI app"""
    start_response('200 OK', [('ContentType', 'text/plain'), ('X-GoodMusic', '1940s')])
    return [b'Hello World from a barebones WSGI application, yo!']
