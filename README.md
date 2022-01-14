# The Greatest Beverage

This web application is designed in a Django framework. The backend is developed in Python and the 
front end using React.js.  

The landing page has 3 main components. The title, the image, the description and a form to place
and order for the drink. Once the fields are completed the 'Pay me later' button generates a unique
URL with details of the order confirmation including a unique order number. 

If the user has not provided a customer name a random name is generated for the order. If the user 
has not provided a quantity amount, the default quantity is set to 1. City, province and country
details must be provided, otherwise the user is alerted to do so when the 'Pay me later' button
is clicked. 

Note: the front end fetch requests are mate using a global variable called 
PORT = "http://127.0.0.1:8000". If you are running the application on a different port, you will 
need to change the value of this variable in App.js to make the application function correctly.

The request for all orders are stored in a sqllite3 database.  

### Details for admin access to database
Admin Username: Superuser 
Admin Password: Password

In order to run this application you need to have python and node.js installed. 
You need to cd into the frontend/react-frontend directory and run the "npm build" command to 
create the build directory.
You can run "pip3 install -r requirements.txt" in your virtual environment and then run the 
"python3 manage.py runserver" to start the django server. 
