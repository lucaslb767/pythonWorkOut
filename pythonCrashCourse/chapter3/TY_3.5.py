guests = ['Schumpeter', 'Einstein', 'Seu Zé']

def guest_invite():
    for i in range(0,len(guests)):
        print('Dear ' + guests[i] + ' would you like to grab a lunch?')

guest_invite()

print('Oh, I see that you ' + guests[2] + ' is too busy to attend. Shame.')

guests[2] = 'Obama'

guest_invite()

#TY_3.9

print(len(guests))

