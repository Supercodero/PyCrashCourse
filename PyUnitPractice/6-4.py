aliens = []

for alien_num in range(30):
    new_alien = {'color' : 'green', 'points' : alien_num,'speed': 'slow'}
    aliens.append(new_alien)

for alien in aliens[:]:
    print(alien)
print("...")

print ("Total number of aliens is "+str(len(aliens)))