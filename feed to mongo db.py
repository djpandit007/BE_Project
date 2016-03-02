import random 
import string
import time
import pymongo as mongo


if __name__ == "__main__":
    
    WORDLIST_FILENAME = "wordsMean.txt"

    client = mongo.MongoClient('mongodb://alexander:netake1234@ds011168.mlab.com/alex_db', 11168)
    db = client.alex_db
    collection = db.words


    def loadWords():
        """
        Returns a list of valid words. Words are strings of lowercase letters.
        
        Depending on the size of the word list, this function may
        take a while to finish.
        """
        print "Loading word list from file..."
        # inFile: file
        inFile = open(WORDLIST_FILENAME, 'r', 0)
        # line: string
        line = inFile.readline()
        wordlist = inFile.readlines()
        #print l
        # wordlist: list of strings
        #wordlist = string.split(line)
        temp = {}
        print "  ", len(wordlist), "words loaded."        
        for i in wordlist:
            #print i
            #processing to make a jason data
            temp = {}
            w = i.split('\t')
            name = str(w[0])
            mean = str(w[1])
            usage = str(w[2])
            points = str(w[3])
            diff = str(w[4][:2])

            temp['name'] = name
            temp['mean'] = mean
            temp['usage'] = usage
            temp['points'] = points
            temp['difficulty'] = diff


            result = collection.insert(temp)
            print result
            #print temp            
        return wordlist
    loadWords()
