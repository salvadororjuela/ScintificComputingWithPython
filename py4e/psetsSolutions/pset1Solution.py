def arithmetic_arranger(problems, validator=False):
    # List to store one list for each operation
    listOfProblems = list()
    results = list()
    result = 0
    moreDigits = 0
    # Elements of the operation to print
    element1 = element2 = separationLine = total = ""
    # Temporary tuples to store the values that will be converted into str to
    # be stored in the previous variables (line 8)
    tupleElement1 = tupleElement2 = sepLineTup = ""
    tupleTotal = ""
    separationSpace = "    "

    # Verify that the number of operations is no greater than 5 operations
    if len(problems) > 5:
        return "Error: Too many problems."

    for problem in problems:
        # Add each operation into a listOfProbles for further validation
        listOfProblems.append([problem])

    # Loop through listOfProblems, and then Loop throug each operation for
    # further validations
    for operation in listOfProblems:
        for operationElement in operation:
            # Verify if the operation is addition or subtraction only
            if ("*" in operationElement or "/" in operationElement):
                return "Error: Operator must be '+' or '-'."
            # Split each element of the operation to get individual values and
            # validate that the numbers have no more than 4 digits
            operationElement = operationElement.split()
            if len(operationElement[0]) > 4 or len(operationElement[2]) > 4:
                return "Error: Numbers cannot be more than four digits."

            # Verify if the numbers in the operation are only digits and not
            # letters or other characters
            try:
                operationElement[0] = int(operationElement[0])
                operationElement[2] = int(operationElement[2])
            except:
                return "Error: Numbers must only contain digits."

            # Develop the mathematical operation and store the elements into
            # the results list with each result
            if operationElement[1] == "+":
                result = operationElement[0] + operationElement[2]
            else:
                result = operationElement[0] - operationElement[2]

            # Store the length of the element with more digits in each
            # operation
            if len(str(operationElement[0])) > len(str(operationElement[2])):
                moreDigits = len(str(operationElement[0]))
            elif len(str(operationElement[0])) < len(str(operationElement[2])):
                moreDigits = len(str(operationElement[2]))
            else:
                moreDigits = len(str(operationElement[0]))

            # Append the elements of the operation to a list
            results.append([operationElement[0], operationElement[1],
                            operationElement[2], result, moreDigits])

    for element in results:
        # When the number of digits of the element 0 is less than the
        # number of digits of the element 2, print white spaces ahead
        # of the number to align the element to the right when
        # displaying.
        if len(str(element[0])) < len(str(element[2])):
            # Store each value in a tuple and then convert all values in
            # a single str called element1
            tupleElement1 = " " * \
                (element[-1] - len(str(element[0]))
                 ), "  ", element[0], separationSpace
            for i in tupleElement1:
                element1 += str(i)

        # The opposite case of if the elements 0 and 2 have the same
        # number of digits
        else:
            # Store each value in a tuple and then convert all values in
            # a single str called element1
            tupleElement1 = "  ", element[0], separationSpace
            for i in tupleElement1:
                element1 += str(i)

    for element in results:
        # When the number of digits of the element 0 is greater than
        # the number of digits of the element 2, print the operation
        # symbol (element[1]), and then white spaces ahead of the
        # number to align the element to the right when displaying.
        if len(str(element[0])) < len(str(element[2])):
            tupleElement2 = element[1], " ", element[2], separationSpace
            for i in tupleElement2:
                element2 += str(i)
        # The opposite case
        elif len(str(element[0])) > len(str(element[2])):
            tupleElement2 = element[1], " " * (len(str(element[0])) - len(
                str(element[2]))-1), "  ", element[2], separationSpace
            for i in tupleElement2:
                element2 += str(i)
        # If the elements 0 and 2 have the same number of digits
        else:
            tupleElement2 = element[1], " ", element[2], separationSpace
            for i in tupleElement2:
                element2 += str(i)

    # Print the divisory line between operation and result adding the
    # same number  of dashes as the number of digits of the larger
    # number plus two additional dashes.
    for element in results:
        sepLineTup = "-" * (element[-1] + 2), separationSpace
        for i in sepLineTup:
            separationLine += i

    # Remove the final separationSpace of each element to avoid errors
    element1 = element1.rstrip(" ")
    element2 = element2.rstrip(" ")
    separationLine = separationLine.rstrip(" ")
    
    # Determine if the output will display or not the result element of the
    # operation
    if validator is True:
        for element in results:
            # If the result has more digits than the largest element
            if len(str(element[3])) > element[-1]:
                tupleTotal = " ", element[3], separationSpace
                for i in tupleTotal:
                    total += str(i)
            # If the result has less digits than the largest element
            elif len(str(element[3])) < element[-1]:
                tupleTotal = "   ", element[3], separationSpace
                for i in tupleTotal:
                    total += str(i)
            # If the result has the same digits the largest element has
            else:
                tupleTotal = "  ", element[3], separationSpace
                for i in tupleTotal:
                    total += str(i)
        # Remove the final separationSpace of the total to avoid errors
        total = total.rstrip(" ")
        print(element1 + "\n" + element2 + "\n" + separationLine + "\n" + total)
    else:
      print(element1 + "\n" + element2 + "\n" + separationLine)

arithmetic_arranger(['32 - 698', '1 - 3801', '45 + 43',
                   '123 + 49', '988 + 40'], True)