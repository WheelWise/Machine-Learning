# Search Engine Demo

This is just a quick demo of how the Search Engine Works.

## Server

In the server directory you will find two .py files, main.py is a server Flask that runs on port `8080` and creates an instance of SearchEngine and mounts it on top of the pretrained model found in ../src/models. Then, creates a Flask application that has a single `Search` route, there you can send a query from the frontend and it will return the elements of the mongo database.

## Frontend

It is a small application made quickly with creat-react-app, which has in App.js the basic logic to be able to receive an input from the user and send it to the server to receive a list of cars.

## How to run this demo?

1. Clone the repo in your machine.

`git clone https://github.com/WheelWise/Machine-Learning.git`

2. Start your MongoDB server on : `mongodb://localhost:27017`

3. Use the databaseFaker tool to create a fake database using :

```
# make sure you are in the /tools dir
python3 databaseFaker.py mongodb://localhost:27017 test cars 2000
```

4. Now you can train a SearchEngine object running the annoy model :

```
# make sure you are in the /src dir
python3 SearchEngineAN.py
```

This will create a trained model file in the /models dir

5. Now that you have a trained model and a database you only have to run the server and the client :

```
# inside the /demo/server
python3 main.y

# inside the /demo/client
npm i && npm run start
```

6. Thats it!
