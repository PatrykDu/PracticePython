checklist = ["Portugal", "Germany", "Munster", "Spain"]

file = open('countries_clean.txt', 'r')
countries = []
for country in file:
    countries.append(country.strip())


print([country for country in checklist if country in countries])
