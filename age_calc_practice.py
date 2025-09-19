dob = datetime.strptime(data[i]["children"][j]["dob"], "%d-%m-%Y")
age = datetime.today().year - dob.year - ((datetime.today().month, datetime.today().day) < (dob.month, dob.day))
