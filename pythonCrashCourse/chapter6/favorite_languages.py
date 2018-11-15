favorite_languages = {
    'jen':'python',
    'sarah':'C',
    'jon':'ruby'
}

print('Jon favorite language is ', favorite_languages['jon'])

friends = ['sarah']

#using a list to sort a dictionary's value
for name in favorite_languages:
    print(name.title())

    if name in friends:
        print('Hi', name.title(),'I see your favorite language is', favorite_languages[name],'!')


#using the value() method to only loop trhough values

print('the following values have been mentioned:')

for language in favorite_languages.values():
    print(language.title())