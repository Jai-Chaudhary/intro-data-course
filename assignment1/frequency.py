import sys
import json

def main():
    tweet_file = open(sys.argv[1])

    term_count_dict = {}
    count_all_terms = 0

    for line in tweet_file:
        tweet_object  = json.loads(line)
        textkey = "text"
        if textkey in tweet_object.keys():
            for tweet_term in tweet_object[textkey].encode('utf-8').split():
            	if tweet_term in term_count_dict.keys():
            		term_count_dict[tweet_term] += 1
            	else:
            		term_count_dict[tweet_term] = 1
            	count_all_terms += 1

    # print non_sentiment_term_dict
    for tweet_term in term_count_dict.keys():
        print tweet_term + " " + str(float(term_count_dict[tweet_term])/count_all_terms)

if __name__ == '__main__':
    main()
