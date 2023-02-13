options = ['Carrot Farm (carrot)',
        'Eggplant Sacrifice (eggplant)', 
        'Fishing Bot (fishing)', 
        'Pepper Farm (pepper)', 
        'Potato Sacrifice (potato)']
import pyfiglet

print(pyfiglet.figlet_format('FarmRPG Tool'))
print('Welcome to FarmRPG Tool. Below are your options:')
for option in options:
    print(option)
choice = input('Please select one of the above options, for example: "pepper"\n').lower()

if choice == 'carrot':
    execfile('carrotFarm.py')
elif choice == 
