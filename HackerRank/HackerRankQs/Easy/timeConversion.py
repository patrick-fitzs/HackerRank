time = "07:05:45AM"



def timeConversion(s):
    hour = int(s[:2])
    rest = s[2:]

    if s[-2:] == "AM":
        if hour == 12:
            hour = "00"
        else:
            hour = f"{hour:02}"
    else:
        if hour != 12:
            hour += 12

    return f"{hour}{rest[:-2]}"


print(timeConversion(time))


#
# if s[:-2] == "AM":
#     if hour == 12:
#         hour = "00"
#     else:
#         hour = f"{hour:02}"
# else:
#     if hour != 12:
#         hour += 12
#
# return (f"{hour}{rest[:-2]}")