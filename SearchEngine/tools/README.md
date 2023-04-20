# Useful tools for developing the Search Engine

## databaseFaker.py

This tool aims to generate a somehow "real" simulation of the NoSQL databse for the cars. You can use it from the command line and make two types of ouptputs :

1. Create a fake database in your MongoDB local server

`python3 databaseFaker.py <MONGO_URL> <DB_NAME> <COLLECTION> <N_CARS> `

Example :

`python3 databaseFaker.py mongodb://localhost:27017 test cars 2000 `

2. Create a fake database in a database.json file

`python3 databaseFaker.py json <N_CARS>`

Example :

`python3 databaseFaker.py json 100`
