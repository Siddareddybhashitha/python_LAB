
#dict1 is the first dictionary
dict1 = {'Ritika': 5, 'Sam': 7, 'John': 10}
#dict2 is the second dictionary
dict2 = {'Aadi': 8, 'Sam': 20, 'Mark': 11}
#concatenating two dictionaries
dict2.update(dict1)
for key, value in sorted(dict2.items(), key=lambda item: item[1]):
    print("%s: %s" % (key, value))