guests = ['Schumpeter', 'Einstein', 'Seu Zé']

def guest_invite():
    for i in range(0,len(guests)):
        print('Dear ' + guests[i] + ' would you like to grab a lunch?')

guest_invite()

# print('Oh, I see that you ' + guests[2] + ' is too busy to attend. Shame.')

guests[2] = 'Obama'

guest_invite()

guests.insert(0,'Gandhi')
guests.insert(2,'Bill Gates')
guests.append('Fred')

guest_invite()

print('Well, unfortunately I can only invite 2 people.')

for i in range (0,len(guests)-2):
   removed_guest = guests.pop(0)

   print ('Sorry for the inconvinience,', removed_guest)
   print(guests)

for i in range(0,2):
    print('You are still invited ', guests[0])
    del guests[0]

print(guests)