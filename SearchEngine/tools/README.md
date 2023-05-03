# Useful tools for developing the Search Engine

## database_faker.py

This tool aims to generate a somehow "real" simulation of the NoSQL database for the cars. You can use it from the command line and make two types of outputs :

1. Create a fake database in your MongoDB local server

`python3 database_faker.py <MONGO_URL> <DB_NAME> <COLLECTION> <N_CARS> `

Example :

`python3 database_faker.py mongodb://localhost:27017 test cars 2000 `

2. Create a fake database in a database.json file

`python3 database_faker.py json <N_CARS>`

Example :

`python3 database_faker.py json 100`

## csv_faker.py

This tool aims to generate a somehow "real" simulation of the CSV or XLS file where the agencies have stored their catalog :

1. Create a fake csv of the agency of your choice :

`python3 csv_faker.py <AGENCY> <N_CARS>`

Example :

`python3 csv_faker.py Ford 1000`
