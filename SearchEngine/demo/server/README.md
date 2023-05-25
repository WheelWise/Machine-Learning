# Getting Started with Search Engine Demo Server

This is only the server of the demo, make sure you follow the steps in the demo readme file.

## API Routes and Examples

The server for Wheelie and the car database. Its actually deployed on :

### Get All Cars

Make a GET request to https://wheelies.wheelwise.xyz/cars

### Get Car by ID

Make a post request to https://wheelies.wheelwise.xyz/cars

With the id of the car url encoded, here is an example in react.

```
try {
      const response = await fetch("https://wheelies.wheelwise.xyz/cars/", {
        method: "POST",
        headers: { "content-type": "application/x-www-form-urlencoded" },
        body: new URLSearchParams({ id : <ID CARRO> }),
      });
      const data = await response.json();
    } catch (err) {}

```

### Get Car with common make

Make a post request to https://wheelies.wheelwise.xyz/cars/make

With the id of the make url encoded, here is an example in react.

```
try {
      const response = await fetch("https://wheelies.wheelwise.xyz/cars/make/", {
        method: "POST",
        headers: { "content-type": "application/x-www-form-urlencoded" },
        body: new URLSearchParams({ id : <ID MARCA> }),
      });
      const data = await response.json();
    } catch (err) {}

```

### Get Car with common agency

Make a post request to https://wheelies.wheelwise.xyz/cars/agency

With the id of the agency url encoded, here is an example in react.

```
try {
      const response = await fetch("https://wheelies.wheelwise.xyz/cars/agency/", {
        method: "POST",
        headers: { "content-type": "application/x-www-form-urlencoded" },
        body: new URLSearchParams({ id : <ID AGENCIA> }),
      });
      const data = await response.json();
    } catch (err) {}

```

## How its made?

If you are curious what we used to create this mini server we use :

- [Flask](https://flask.palletsprojects.com/en/2.2.x/) : HTTP simple server for python
- [PyMongo](https://pymongo.readthedocs.io/en/stable/) : Mongo adapter for python
