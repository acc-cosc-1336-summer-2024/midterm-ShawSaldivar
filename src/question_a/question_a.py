#write functions here, don't add input('') statements here!
def test_config():
    return True

def Get_Whats_Today(day):
    if (day >= 1 and day <= 7):
        names = day
        return names
    elif (day >= 0 or day < 7):
        print("Sorry that is not a valid day, enter a name that is in the range of 1 - 7 inclusive.")

def Name_That_Day(names):
    if (names == 1):
        return "Monday"
    elif (names == 2):
        return "Tuesday"
    elif (names == 3):
        return "Wednesday"
    elif (names == 4):
        return "Thursday"
    elif (names == 5):
        return "Friday"
    elif (names == 6):
        return "Saturday"
    elif (names == 7):
        return "Sunday"
    
def Exit(Answer):
    ReallyReally = Answer
    if ReallyReally == "y":
        return True
    elif ReallyReally == "n":
        return False
