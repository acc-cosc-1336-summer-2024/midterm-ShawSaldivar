#add import
import question_b

def main():
    Kill = int(input("Please enter Kilometers: " ))
    Minoot = int(input("Please Enter your Minutes: "))

    if (Kill >= 0 and Minoot >= 0):
        Flash = question_b.get_miles_per_hour(Kill, Minoot)
        print("Your speed will be: ", Flash, "Miles Per Hour")
    else:
        print("Invalid speed.")
main()