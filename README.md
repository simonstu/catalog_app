# Catalog App Description
Code for a Catalog App written in Python based on Flask and SQLalchemy. Users can login with their Google or Facebook accounts to add new items to the fixed set of categories. Users that are logged in can edit or delete the items they have created. User that are not logged in can only view the different items. It also possible to get the underlying data of categories and items as a JSON file (e.g. at http://localhost:5000/catalog/name_of_category/JSON).

# Installation
First download or clone this repository. To start the application with some dummy data first run "python lots_of_item.py" in the app folder to fill the database.
To start the application execute "python application.py" in the root folder from your terminal. The web app should be accessible at http://localhost:5000/.

# Setup of Google Logins
In order to allow a login through Google you have to create an OAuth-2.0-Client at [https://console.developers.google.com/apis/credentials](https://console.developers.google.com/apis/credentials). Choose a web app and add http://localhost:5000 as source and http://localhost:5000/categories/ as URI. Download the JSON file and save it as "google_client_secrets.json" in the root folder. Replace "YOUR_CLIENT_ID_XXX.apps.googleusercontent.com" in app/templates/login.html with your Client-ID (ends with .apps.googleusercontent.com).

# Setup of Facebook Logins
In order to allow a login through Facebook you have to create an app at [https://developers.facebook.com/apps](https://developers.facebook.com/apps). Replace "XXX" and "YYY" in the fb_client_secrets.json file in the root folder with the data of your newly created app. Replace "YOUR_APP_ID_XXX" in app/templates/login.html with the ID of your app.