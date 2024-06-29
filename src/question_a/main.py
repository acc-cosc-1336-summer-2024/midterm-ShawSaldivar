#add import
import question_a


def main():
    AnythingElse = 'y'
    while(question_a.Exit(AnythingElse)):
        WeekNum = int(input("Please enter a number to display a day of the Week: "))
        if (WeekNum >= 1 and WeekNum <= 7 ):
            ConvNum = question_a.Get_Whats_Today(WeekNum)
            names = question_a.Name_That_Day(ConvNum)

            print("You chose: ", WeekNum,"Which is: ", names)
            AnythingElse = input("Your question has been answered, do you have another? Say [ Y ] to continue, [ N ] to quit. ")
            question_a.Exit(AnythingElse)

            if (AnythingElse != "y"):
                return False

        else:
            print("Invaid day, please choose a number within the week.")
            

main()