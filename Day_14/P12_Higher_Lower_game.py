import random
import game_data

logo = '''
    __  ___       __             
   / / / (_)___ _/ /_  ___  _____
  / /_/ / / __ '/ __ \/ _ \/ ___/
 / __  / / /_/ / / / /  __/ /    
/_/ ///_/\__, /_/ /_/\___/_/     
   / /  /____/_      _____  _____
  / /   / __ \ | /| / / _ \/ ___/
 / /___/ /_/ / |/ |/ /  __/ /    
/_____/\____/|__/|__/\___/_/   
'''

vs = ''' _    __    
| |  / /____
| | / / ___/
| |/ (__  ) 
|___/____(_)
'''

score = 0

a = random.choice(game_data.data)

while (True):

    print(logo)

    b = random.choice(game_data.data)

    if (a == b):
        b = random.choice(game_data.data)

    print(f"Compare A: {a['name']}, {a['description']}, {a['country']}")

    print(vs)

    print(f"Compare B: {b['name']}, {b['description']}, {b['country']}")

    tell = input("Who has more followers? Type 'A' or 'B': ").lower()

    if ((a["follower_count"] > b["follower_count"] and tell == "a") or (a["follower_count"] < b["follower_count"] and tell == "b")):
        a = b
        score += 1
        print("\n" * 5)
        print(f"You're right! Current score: {score}")

    else:
        print("\n" * 22)
        print(f"Sorry, that's wrong. Final score: {score}")
        break
