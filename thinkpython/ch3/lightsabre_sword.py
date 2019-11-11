sword_charge = float(input("Enter the sword_energy: "))
shield_energy = float(input("Enter the shield_energy: "))

#For example, suppose we can slay the dragon only if our magic lightsabre sword is charged to 90% or higher, and we
#have 100 or more energy units in our protective shield. We find this fragment of Python code in the game:
if not (sword_charge >= 0.90 and shield_energy >= 100):
    print("Your attack has no effect, the dragon fries you to a crisp!")
else:
    print("The dragon crumples in a heap. You rescue the gorgeous princess!")

#or

if sword_charge < 0.90 or shield_energy < 100:
    print("Your attack has no effect, the dragon fries you to a crisp!")
else:
    print("Your attack has no effect, the dragon fries you to a crisp!")


#and
if sword_charge >= 0.90 and shield_energy >= 100:
    print("The dragon crumples in a heap. You rescue the gorgeous princess!")
else:
    print("Your attack has no effect, the dragon fries you to a crisp!")
