# Datatype define
# age: int
# name: srtr
# height: float
# is_human: bool


# Useful for to debugg after completion in case of any error

def police_check(age: int) -> bool:  # (->) represent expected output
    if age >= 18:
        can_drive = True
    else:
        can_drive = False

    return can_drive


print(police_check(18))
