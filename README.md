# Flask CRUD App

A simple Flask app with user management (Create, Read, Update, Delete) featuring Bootstrap styling and image upload support.

Group Members
- Padilla, Justin Mark G.
- Cruz, Llord Andrei R.
- Santiago, Stephen Ivan F.
- Fadrigalan, Vonn Ryan Albert
- Mendoza, Jefferson V.

## 🔧 Features

- Create, edit, delete users
- Upload profile images
- Modal-based user detail view
- SQLite database
- Docker support (optional)

## 🚀 Setup Instructions

```bash
# Install dependencies
pip install -r requirements.txt

# Run the app
flask run

## 🐳 Docker Build and Run
##To build and run the app using Docker:

## Build the Docker image:
docker build -t flask-crud-app .

##Run the Docker container:
docker run -d -p 5000:5000 flask-crud-app

##The app will now be accessible at:
http://localhost:5000

## 🌐 Expose App Publicly with Ngrok
##To make your local app accessible over the internet:

Download Ngrok and install it

##Run Ngrok to expose the Flask app:
ngrok http 5000

##Copy the HTTPS URL from Ngrok's output (e.g., https://abc123.ngrok.io) and use it to access your app remotely