def calculate_love_score(male, female):
    count1 = 0
    count2 = 0
    new = male+female
    a = ["t", "r", "u", "e"]
    b = ["l", "o", "v", "e"]

    for i in a:
        count1 += new.lower().count(i)

    for i in b:
        count2 += new.lower().count(i)

    print(str(count1) + str(count2))


calculate_love_score("mayank", "rupa")
