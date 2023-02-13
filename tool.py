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
    exec(open('carrotFarm.py').read())
elif choice == 'eggplant':
    exec(open('eggplantSacrifice.py').read())
elif choice == 'fishing':
    exec(open('fishing.py').read())
elif choice == 'pepper':
    exec(open('pepperFarm.py').read())
elif choice == 'potato':
    exec(open('potatoSacrifice.py').read())
else:
    'Invalid choice.'
