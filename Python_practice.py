# Test
print("Hello World")

# 3.8.2 If statement
counties = ['Arapahoe', 'Denver', 'Jefferson']
if counties[1] == 'Denver':
    print(counties[1])

# Membership operator
if "El Paso" in counties:
    print("El Paso is in the list of counties.")
else:
    print("El Paso is not the list of counties.")

# For loop
for county in counties:
    print(county)

# Make dictionary
counties_dict = {"Arapahoe": 369237, "Denver": 413229, "Jefferson": 390222}
# for county, voters in counties_dict.items():
#     print(county + "count has " + str(voters) + " registered voters.")

# F-String
for county, voters in counties_dict.items():
    print(f"{county} count has {voters} registered voters.")

# List of dictionaries
voting_data = voting_data = [{"county":"Arapahoe", "registered_voters": 422829}, {"county":"Denver", "registered_voters": 463353}, {"county":"Jefferson", "registered_voters": 432438}]
for county_dict in voting_data:
    print(f"{county_dict['county']} county has {county_dict['registered_voters']} registered voters.")
