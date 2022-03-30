"""7.2 Write a program that prompts for a file name, then opens that file and reads through the file, looking for lines of the form:
X-DSPAM-Confidence:    0.8475
Count these lines and extract the floating point values from each of the lines and compute the average of those values and produce
an output as shown below. Do not use the sum() function or a variable named sum in your solution.
You can download the sample data at http://www.py4e.com/code3/mbox-short.txt when you are testing below enter mbox-short.txt as the file name."""


try:
    fhandler = open(input("Name of the File:"))
    count = 0
    form = "X-DSPAM-Confidence:"
    addition = 0
    
    for line in fhandler:
        if form in line:
            # find the : character position
            num = line.find(":")
            # find the characters from ":" up to the end of the line
            numb = line[num + 1:-1]
            # convert the characters to float
            number = float(numb.strip())
            # update addition and count
            addition = addition + number
            count = count + 1

    average = addition / count
    print(f"Average spam confidence: {average}")

except:
    print(f"The file does not exist.")