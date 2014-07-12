import sys
import json

def main():
    tweet_file = open(sys.argv[1])

    hashtag_count_dict = {}

    for line in tweet_file:
        tweet_object  = json.loads(line)
        key = "entities"
        if key in tweet_object.keys():
            if "hashtags" in tweet_object[key].keys() and tweet_object[key]['hashtags'] != []:
                for hashtag_term in tweet_object[key]['hashtags']:
                    if hashtag_term['text'] in hashtag_count_dict.keys():
                        hashtag_count_dict[hashtag_term['text']] += 1
                    else:
                        hashtag_count_dict[hashtag_term['text']] = 1

    for hashtag in sorted(hashtag_count_dict, key=hashtag_count_dict.get, reverse=True)[0:10]:
        print hashtag + " " + str(hashtag_count_dict[hashtag])

if __name__ == '__main__':
    main()
