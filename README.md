# SAPHT_Model is available in 3 formats (.py, .ipynb, .html)

## Pre-Requisites

### 1. Install Stanford CoreNLP


The latest version at this time (2017-07-11) is 3.8.0:

wget http://nlp.stanford.edu/software/stanford-corenlp-full-2017-06-09.zip
unzip stanford-corenlp-full-2017-06-09.zip

### 2. Start the Server

1) cd stanford-corenlp-full-(2017-06-09)folder

2) Write down following command in terminal:
    java -mx5g -cp "*" edu.stanford.nlp.pipeline.StanfordCoreNLPServer -timeout 10000

NB: timeout is in milliseconds, I set it to 10 sec above. You should increase it if you pass huge blobs to the server.


### 3. Install the python package

pip install pycorenlp
