state_to_code_file = open('map_state_name_to_code')
state_to_coordinates_file = open('state_geographical_centre_mapping')

state_to_code = {} # initialize an empty dictionary
for line in state_to_code_file:
    code, state  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
    state_to_code[state.strip()] = code  # Convert the score to an integer.

state_to_coordinates = {} # initialize an empty dictionary
for line in state_to_coordinates_file:
    state, latitude, longitude  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
    state_to_coordinates[state.strip()] = [longitude.strip(), latitude.strip()]  # Convert the score to an integer.

for state in state_to_coordinates.keys():
	print state_to_code[state] + " " + state_to_coordinates[state][0] + " " + state_to_coordinates[state][1]