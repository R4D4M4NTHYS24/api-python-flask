# api-python-flask
creating a simple api using python and flask

The first line of code imports the Flask class from the Flask library.

The second line imports the CORS module and the cross_origin function from the flask_cors library.

An instance of the Flask class is created and assigned to the 'app' variable.

The following line creates an instance of the CORS class and assigns it to the 'cors' variable. The CORS class is used to handle cross-resource requests (CORS) in the Flask app.

The following line defines a Flask application route using the '@app.route' decorator. In this case, the path is '/api/prices'.

The following line uses the '@cross_origin' decorator to allow CORS requests in the path.

The 'get_prices' function is the controller function for the '/api/prices' route. The function returns a list of prices for different currencies in JSON format.

The function uses the Python 'round' function to round prices to two decimal places.

The last line of the code starts the Flask server when the app runs.
