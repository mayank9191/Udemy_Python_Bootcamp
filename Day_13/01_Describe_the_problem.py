def my_function():
  # here ERROR  is upperbound 20 -> 21 which is not including in  a loop
    for i in range(1, 21):
        if (i == 20):
            print("You got it")


my_function()
