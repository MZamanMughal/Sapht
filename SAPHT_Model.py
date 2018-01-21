
# coding: utf-8

# # Steps Required

# ### 1. Install Stanford CoreNLP

# 
# The latest version at this time (2017-07-11) is 3.8.0:
# 
# wget http://nlp.stanford.edu/software/stanford-corenlp-full-2017-06-09.zip
# unzip stanford-corenlp-full-2017-06-09.zip

# ### 2. Start the Server

# 1) cd stanford-corenlp-full-(2017-06-09)folder
# 
# 2) Write down following command in terminal:
#     java -mx5g -cp "*" edu.stanford.nlp.pipeline.StanfordCoreNLPServer -timeout 10000
# 
# NB: timeout is in milliseconds, I set it to 10 sec above. You should increase it if you pass huge blobs to the server.
# 

# ### 3. Install the python package
# 

# pip install pycorenlp

# # Model Code

# #### Import

from pycorenlp import StanfordCoreNLP


# #### Connect the wrapper to the server 

nlp = StanfordCoreNLP('http://localhost:9000')


# #### Sentiment Funtion

def give_me_sentiments(sentence):
    '''
    Args:
        sentence (string): either a single sentence or multiple sentences separeted by '.'
    
    Returns:
        sentiment_values ( list ) : list of sentiment values
        
        Range (0-4)
        0-Strongly Negative
        1-Negative
        2-Neutral
        3-Positive
        4-Strongly Positive
    
    '''
    
    
    sentiment_values=[]
    res = nlp.annotate(sentence,
                   properties={
                       'annotators': 'sentiment',
                       'outputFormat': 'json'
                   })
   

    for s in res["sentences"]:
        sentiment_values.append(s["sentimentValue"])
        
        #If you want to print the sentences and values too please uncomment below lines
#        print ("%d: '%s': %s %s" % (
#             s["index"],
#             " ".join([t["word"] for t in s["tokens"]]),
#             s["sentimentValue"], s["sentiment"]))
        
    
    return sentiment_values


# ### Test run on Trump Tweets

#sentence_trump_tweets="More Russian media from February 2014 Headline Donald Trump Stop picking on Russia. Donald Trump s new FBI director pick has Russian ties of his own Vote NO. Donald Trump is Motivated By his HATE of Barack Obama amp Love for Money Not His LOVE for America If You Agree"
#give_me_sentiments(sentence_trump_tweets)

