# import smtplib

# my_email = "rohankumar94942@gmail.com"
# password = "mvwkhjakykglsxyc"


# with smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(from_addr=my_email,
#                         to_addrs="mayankkulahara@gmail.com", msg="Subject:Hello\n\nThis is the body of my email.")


# import datetime as dt

# now = dt.datetime.now()

# year = now.year
# month = now.month
# day = now.day
# day_of_week = now.weekday()

# print(f"{day}-{month}-{year}/ {day_of_week}")

# date_of_birth = dt.datetime(year=2003, month=11, day=21)
# print(date_of_birth)

emojis = "🍰🎈🎉🎂🌟"
codes = [ord(char) for char in emojis]
print(codes)
