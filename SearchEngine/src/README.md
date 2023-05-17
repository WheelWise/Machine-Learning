# Search Engine Source Code

This directory its where you can find the main logic and AI Development scripts and libaries.

## reader.py

This class, its a mongo client interface that its in charge of processing raw data (csv or xls) and saving it in and efficient way inside de NoSQL database.

## search_engine.py

This class its also a mongo client interface, that save a KNN model and creates and index that makes a match bewtween Mongo id and KNN indexes.

## utils.py

This file has important and key functions for things like : generating sentences, word2vec model handlers and other.
