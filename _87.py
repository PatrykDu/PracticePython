file1 = open('countries_missing.txt', 'r')
checklist = ["Portugal", "Germany", "Spain"]
countries = [country.strip() for country in file1]
print(countries)
countries += checklist
countries.sort()
with open('countries_not_missing', 'w') as file2:
    for country in countries:
        file2.write(country + '\n')
