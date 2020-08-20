"""(1)

    Given this sort of dict (country:city-list):

	{'Israel': ['Jerusalem', 'Tel Aviv'],
	 'USA': ['Boston', 'New York', 'Chicago'],
	 'China': ['Beijing', 'Shanghai']}

    Use a nested list comprehension to produce a list of
    tuples that look like (city, country).

"""

country_city = {
    "Israel": ["Jerusalem", "Tel Aviv"],
    "USA": ["Boston", "New York", "Chicago"],
    "China": ["Beijing", "Shanghai"],
}

country_city_tuple_list = [
    (each_country, each_city)
    for each_country, cities in country_city.items()
    for each_city in cities
]

# for each_country, cities in country_city.items():
#     for each_city in cities:
#         country_city_tuple_list.append((each_country, each_city))

print(country_city_tuple_list)
