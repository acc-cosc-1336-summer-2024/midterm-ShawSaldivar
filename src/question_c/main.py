#add import
import question_c

def main():
    Tables = []
    Celcius = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

    print("Degrees in Celcius: ")
    for c in range(0, len(Celcius)):
        Tables = question_c.Get_Fahrenheit(Celcius[c])
        print(Celcius[c], " Degrees in Fahrenheit: ", round(Tables))

main()