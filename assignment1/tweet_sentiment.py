import sys
import json

def hw():
    print 'Hello, world!'

def lines(fp):
    print str(len(fp.readlines()))

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    # hw()
    # lines(sent_file)
    # lines(tweet_file)

    scores = {} # initialize an empty dictionary
    for line in sent_file:
        term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
        scores[term] = int(score)  # Convert the score to an integer.

    # print scores.items() # Print every (term, score) pair in the dictionary

    for line in tweet_file:
        tweet_object  = json.loads(line)
        tweet_sentiment = 0

        textkey = "text"
        if textkey in tweet_object.keys():
            for tweet_term in tweet_object[textkey].encode('utf-8').split():
                if tweet_term in scores.keys():
                    # print tweet_term, scores[tweet_term]
                    tweet_sentiment += scores[tweet_term]
        print str(tweet_sentiment)

    

    # print scores.items() # Print every (term, score) pair in the dictionary

    # print json.loads(tweet_file)

if __name__ == '__main__':
    main()
