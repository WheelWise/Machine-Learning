# WW Natural Language Search Engine Concept

This directory contains a demo of the first approach to developing the "natural language search" requirement.

## The Idea

We propose a system where every Car document (in a NoSQL databse) can be vectorized by an [Embedding](https://en.wikipedia.org/wiki/Word_embedding) model, which will take all the information of the Car and transform it into a vector, allowing us to use the [KNN](https://en.wikipedia.org/wiki/K-nearest_neighbors_algorithm) algorithm to represent every Car as a point in a map, and the search of the user as another point, then we can calculate the nearest neighbors that are more relevant to the user.

## How to run this code ?

In this directory you can find all the files needes to run the code, we suggest runnig it in a Collab Notebook, so you dont need to download all the `tensorflow` and `sklearn` libaries. You can access it frome [here](https://colab.research.google.com/drive/1Zj_22HcRSZea0FYz8P8TmWn9pZtLS_23?usp=sharing).

### Files

Explanation of what is in each file and what it does.

#### `database.json`

This file contains an array of javascript objects, this file represents what will be in the NoSQL database. Each object in the array is supossed to be a Car document uploadd by the agency, you can notice how some of the documents are different than others, some have different characteristics from the others, this to represent how the agencies will have the flexibility to upload their catalogs in the format they want.

#### `main.py`

The is the main file, it contains all the code to test the functionality yourself, you can find more of how it workes by reading the comment in the file.

#### `requirements.txt`

The python version of the `package.json` file, it contains a list of the dpendecies so you dont forget to install them before tying to run de code

### Functions

The main object in the `main.py` file its the _Search Engine_ object, you can use it to train a knn model from a databse file or add knowledge from an individual object, but the most important function is _search_, this function accepts a search string as an argument and returns the index of the most relevant object in the databse related to the search.

## Advantages

- The system does not depend on almost any external api, reducing our costs as much as possible.
- The system will have the ability to receive more knowledge when an agency uploads its catalog, without having to train the entire model from scratch.
- We will have absolute control of how the search engine works, allowing us to decide how it will scale in addition to adapting it to the other requirements.

## License

To determinate.
