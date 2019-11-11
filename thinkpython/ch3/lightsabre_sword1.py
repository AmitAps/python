sword_charge = float(input("Enter the sword_energy: "))
shield_energy = float(input("Enter the shield_energy: "))

sword_check = sword_charge >= 0.90
shield_check = shield_energy >= 100

if sword_check and shield_check:
    print("The dragon crumples in a heap. You rescue the gorgeous princess!")
else:
    print("Your attack has no effect, the dragon fries you to a crisp!")
