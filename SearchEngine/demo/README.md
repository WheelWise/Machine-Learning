# Search Engine Demo

This is just a quick demo of how the Search Engine Works.

## Server

In the server directory you will find two .py files, main.py is a server Flask that runs on port `8080` and creates an instance of SearchEngine and mounts it on top of the embeedings from the database. Then, creates a Flask application that has a two routes, there you can send a query from the frontend and it will return the elements of the mongo database.

## Frontend

It is a small application made quickly with creat-next-app, its a playgorund for simulating how the final product would be implemented in the frontend.

## How to run this demo?

1. Clone the repo in your machine.

```
git clone https://github.com/WheelWise/Machine-Learning.git
```

2. Start your MongoDB server on : `mongodb://localhost:27017`

3. Use the csv_faker.py tool to create fake csv catalogs using :

```
python csv_faker.py Ford 1000
python csv_faker.py Nissan 1000
python csv_faker.py Mazda 1000
```

4. Run the frontend and the two servers with their respective command :

```
cd client && npm run dev
cd server && python upload_server.py
cd server && python search_server.py
```

5. Play with the frontend, upload a csv file in the `Seller` interface.

6. Thats it!
