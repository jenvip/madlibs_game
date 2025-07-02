# string concatenation methods:
# youtuber = "netflix party"
# print("subscribe to " + youtuber)
# print("subscribe to {}".format(youtuber))
# print(f"subscribe to {youtuber}") #f-string is easiest way


adj = input("Adjective: ")
magical_object = input("Magical Object: ")
place_at_hogwarts = input("Place at Hogwarts: ")
name_of_character = input("Name of HP Character: ")
adj_2 = input("Adjective: ")
magical_creature = input("Magical Creature: ")
same_character = input("Name of Same Character: ")
food = input("Plural Food Item: ")
character_2 = input("Name of Another HP Character: ")
hp_class = input("Name of HP Class: ")
magical_transportation = input("Mode of Magical Transportation: ")
adj_3 = input("Adjective: ")

hp_madlib = (f"One day, Harry Potter woke up feeling very {adj}. He grabbed his {magical_object} and ran down to the {place_at_hogwarts}, where {name_of_character} was waiting with a/an {adj_2} surprise. \n"
             f"''Blimey!'' Harry shouted. ''Is that a {magical_creature}?''"
             f" ''Yes,'' said {same_character}, ''and it loves to eat {food}!''\n"
             f" Suddenly, {character_2} burst in, yelling, ''Quick! We're late for {hp_class}!\n"
             f" Everyone jumped on their {magical_transportation} and zoomed off into the {adj_3} sky.\n")

print(hp_madlib)