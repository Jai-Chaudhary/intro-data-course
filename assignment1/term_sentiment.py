import sys
import json

def hw():
    print 'Hello, world!'

def lines(fp):
    print str(len(fp.readlines()))

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])

    scores = {} # initialize an empty dictionary
    for line in sent_file:
        term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
        scores[term] = int(score)  # Convert the score to an integer.

    # print scores.items() # Print every (term, score) pair in the dictionary

    non_sentiment_term_dict = {}
    for line in tweet_file:
        tweet_object  = json.loads(line)
        textkey = "text"
        if textkey in tweet_object.keys():
            sentiment_term_dict_per_tweet = {}
            non_sentiment_term_dict_per_tweet = {}
            for tweet_term in tweet_object[textkey].encode('utf-8').split():
                if tweet_term in scores.keys():
                    sentiment_term_dict_per_tweet[tweet_term] = scores[tweet_term]
            # print sentiment_term_dict_per_tweet
            for tweet_term in tweet_object[textkey].encode('utf-8').split():
                if tweet_term not in scores.keys():
                    non_sentiment_term_dict_per_tweet[tweet_term] = float(sum(sentiment_term_dict_per_tweet.values()))/len(sentiment_term_dict_per_tweet.values())
        for non_sentiment_term in non_sentiment_term_dict_per_tweet.keys():
            if non_sentiment_term in non_sentiment_term_dict.keys():
                non_sentiment_term_dict[non_sentiment_term].append(non_sentiment_term_dict_per_tweet[non_sentiment_term])
            else:
                non_sentiment_term_dict[non_sentiment_term] = [non_sentiment_term_dict_per_tweet[non_sentiment_term]]

    # print non_sentiment_term_dict
    for non_sentiment_term in non_sentiment_term_dict.keys():
        print non_sentiment_term + " " + str(float(sum(non_sentiment_term_dict[non_sentiment_term]))/len(non_sentiment_term_dict[non_sentiment_term]))

if __name__ == '__main__':
    main()
