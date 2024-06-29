#write functions here, don't add input('') statements here!
def reverse_string(string1):
    counts = len(string1)-1
    string2 = ""
    while(counts >= 0):
        string2 = string2+string1[counts]
        counts -= 1
    return string2