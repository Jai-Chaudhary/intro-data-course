import sys
import json

def get_tweet_location(tweet_object):
    coordinate_key = "coordinates"
    language_key = "lang"
    place_key = "place"

    required_keys = [coordinate_key, language_key]

    code_to_coordinates_file = open('map_code_to_geographical_centre')

    code_to_coordinates = {} # initialize an empty dictionary
    for line in code_to_coordinates_file:
        code, longitude, latitude  = line.split()  # The file is tab-delimited. "\t" means "tab character"
        code_to_coordinates[code.strip()] = [longitude.strip(), latitude.strip()]  # Convert the score to an integer.

    nearest_code = 'XX'
    # print code_to_coordinates

    if all(key in tweet_object.keys() for key in required_keys):
      if tweet_object[language_key] == "en":
        if type(tweet_object[coordinate_key]) == dict:
            min_dist = float("inf")
            # print tweet_object[coordinate_key]
            if coordinate_key in tweet_object[coordinate_key].keys():
                tweet_coordinates =  tweet_object[coordinate_key][coordinate_key]
                for code in code_to_coordinates.keys():
                    dist = (float(tweet_coordinates[0]) - float(code_to_coordinates[code][0]))**2 + (float(tweet_coordinates[1]) - float(code_to_coordinates[code][1]))**2
                    # print tweet_coordinates, code_to_coordinates[code]
                    if dist < min_dist and dist < 1500:
                        nearest_code = code
                        min_dist = dist
    place_code = 'XX'
    if "place" in tweet_object.keys():
        if type(tweet_object["place"]) == dict:
            if "country_code" in tweet_object["place"].keys():
                if tweet_object["place"]["country_code"] == "US":
                    if "full_name" in tweet_object["place"].keys():
                        if tweet_object["place"]["full_name"].split()[-1] in code_to_coordinates.keys():
                            place_code = tweet_object["place"]["full_name"].split()[-1]

    if nearest_code == place_code:
        return place_code
    else:
        return 'XX'   

    # print nearest_code, place_code

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])

    scores = {} # initialize an empty dictionary
    for line in sent_file:
        term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
        scores[term] = int(score)  # Convert the score to an integer.

    # print scores.items() # Print every (term, score) pair in the dictionary
    state_sentiment = {}
    for line in tweet_file:
        tweet_object  = json.loads(line)
        tweet_sentiment = 0

        textkey = "text"
        if textkey in tweet_object.keys():
            for tweet_term in tweet_object[textkey].encode('utf-8').split():
                if tweet_term in scores.keys():
                    # print tweet_term, scores[tweet_term]
                    tweet_sentiment += scores[tweet_term]
        # print str(tweet_sentiment)
        state = get_tweet_location(tweet_object)
        if state != 'XX':
            if state in state_sentiment.keys():
                state_sentiment[state]['sum'] += tweet_sentiment
                state_sentiment[state]['count'] += 1
            else:
                state_sentiment[state] = {}
                state_sentiment[state]['sum'] = tweet_sentiment
                state_sentiment[state]['count'] = 1


    # print state_sentiment
    max_sentiment = -5
    max_happy_state = "ND"
    for state in state_sentiment.keys():
        normalized_sentiment = float(state_sentiment[state]['sum'])/state_sentiment[state]['count']
        if normalized_sentiment > max_sentiment:
            max_sentiment = normalized_sentiment
            max_happy_state = state
            # print max_sentiment, max_happy_state

    print max_happy_state


    # print scores.items() # Print every (term, score) pair in the dictionary

    # print json.loads(tweet_file)

if __name__ == '__main__':
    main()
