from random import randint
dice_images = ["1️⃣", "2️⃣", "3️⃣", "4️⃣", "5️⃣", "6️⃣"]
# upperbound and lowerbound has to be fixed 1 -> 0 and 6 -> 5
dice_num = randint(0, 5)
print(dice_images[dice_num])
