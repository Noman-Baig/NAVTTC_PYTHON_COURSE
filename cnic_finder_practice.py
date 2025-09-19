from datetime import datetime

data = [
    {
        "name":"Aslam",
        "cnin":"41304-1829006-1",
        "dob":"16-08-1911",
        "children":[
            {
              "name":"Rizwan",
              "cnin":"41304-1829007-2",
              "dob":"16-08-1967",
              "children":[
                {
                    "name":"Nouman",
                    "cnin":"41304-1829008-3",
                    "dob":"18-11-1999",
                    "children":[]
                },
                {
                    "name":"Moiz",
                    "dob":"03-07-2003",
                    "cnin":"41304-1829009-4",
                    "children":[]
                }
              ]
            },
            {
              "name":"Furqan",
              "cnin":"41304-1829097-2",
              "dob":"02-09-1972",
              "children":[
                {
                    "name":"Abdullah",
                    "dob":"02-08-2005",
                    "cnin":"41304-1829238-3",
                    "children":[]
                },
                {
                    "name":"Zubair",
                    "dob":"10-07-2008",
                    "cnin":"41304-1829939-4",
                    "children":[]
                }
              ]
            },
            {
              "name":"Rehman",
              "cnin":"41304-1822397-2",
              "dob":"02-09-1968",
              "children":[
                {
                    "name":"Umar",
                    "cnin":"41304-1249238-3",
                    "dob":"04-01-2000",
                    "children":[]
                },
                {
                    "name":"Hammad",
                    "cnin":"41304-1229939-4",
                    "dob":"02-04-2002",
                    "children":[]
                }
              ]
            }
        ]
    }
]

target_cnic = input("Enter CNIC: ")

found = False

for i in range(len(data)):
    if data[i]["cnin"] == target_cnic:
        dob = datetime.strptime(data[i]["dob"], "%d-%m-%Y")
        age = datetime.today().year - dob.year - ((datetime.today().month, datetime.today().day) < (dob.month, dob.day))
        print("Record Found : ")
        print("Name:", data[i]["name"])
        print("Father: None")
        print("Grandfather: None")
        print("DOB:", data[i]["dob"])
        print("Age:", age)
        found = True

    for j in range(len(data[i]["children"])):
        if data[i]["children"][j]["cnin"] == target_cnic:
            dob = datetime.strptime(data[i]["children"][j]["dob"], "%d-%m-%Y")
            age = datetime.today().year - dob.year - ((datetime.today().month, datetime.today().day) < (dob.month, dob.day))
            print("Record Found : ")
            print("Name:", data[i]["children"][j]["name"])
            print("Father:", data[i]["name"])
            print("Grandfather: None")
            print("DOB:", data[i]["children"][j]["dob"])
            print("Age:", age)
            found = True

        for k in range(len(data[i]["children"][j]["children"])):
            if data[i]["children"][j]["children"][k]["cnin"] == target_cnic:
                dob = datetime.strptime(data[i]["children"][j]["children"][k]["dob"], "%d-%m-%Y")
                age = datetime.today().year - dob.year - ((datetime.today().month, datetime.today().day) < (dob.month, dob.day))
                print("Record Found : ")
                print("Name:", data[i]["children"][j]["children"][k]["name"])
                print("Father:", data[i]["children"][j]["name"])
                print("Grandfather:", data[i]["name"])
                print("DOB:", data[i]["children"][j]["children"][k]["dob"])
                print("Age:", age)
                found = True

if not found:
    print("CNIC not found.")
