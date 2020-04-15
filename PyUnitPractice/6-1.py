person = {
    'first_name' : 'Helen',
    'last_name' : 'Keller',
    'age' : 18,
    'city' : 'New York'
}
print(person)

favorite_number = {
    'sarah': 3,
    'someone' : 7
}
print(favorite_number)

rivers = {
    'huanghe' : 'china',
    'changjiang' : 'china',
    'nile' : 'egypt',
    'mixixibi' : 'america'
}
for river in rivers.keys():
    print("The "+river+"runs through "+rivers[river])

print(rivers.keys())
print(set(rivers.values()))

favorite_languages = {
    'sarah' : 'python',
    'lucy' : 'c++',
    'lily' : 'java',
    'ella' : 'powershell'
}

persons = ['selina','lucy','lily','hebe']

for person in favorite_languages.keys():
    if person in persons:
        print("Hi, "+person.title()+", your favorte language is "+favorite_languages[person].title()+" thank you !")
    else:
        print(person+", please conplete the exam.")