people = [
    {"name": "Peter Parker", "superhero-name": "Spider-Man"},
    {"name": "Tony Stark", "superhero-name": "Iron Man"},
    {"name": "Frank Castle", "superhero-name": "The Punisher"}
]

people.sort(key=lambda person: person["name"])
print(people)