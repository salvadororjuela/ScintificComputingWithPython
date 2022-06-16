def arithmetic_arranger(problems, validator=False):
    # List to store one list for each operation
    listOfProblems = list()
    results = list()
    result = 0
    moreDigits = 0
    # Elements of the operation to print
    element1 = list()
    element2 = list()
    separationLine = list()
    total = list()

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
            element1 = (" " * (element[-1] - len(str(element[0])) + 1), element[0], "    ")
        # The opposite case of if the elements 0 and 2 have the same
        # number of digits
        else:
            element1 = (f"  {element[0]}     ")

    for element in results:
        # When the number of digits of the element 0 is greater than
        # the numberof digits of the element 2, print the operation
        # symbol (element[1]), and then white spaces ahead of the
        # number to align the element to the right when displaying.
        if len(str(element[0])) < len(str(element[2])):
            element2 = (f"{element[1]} {element[2]}     ")
        # The opposite case
        elif len(str(element[0])) > len(str(element[2])):
            element2 = (element[1], " " * (len(str(element[0])) - len(str(element[2]))-1), element[2], "    ")
        # If the elements 0 and 2 have the same number of digits
        else:
            element2 = (f"{element[1]} {element[2]}     ")

    # Print the divisory line between operation and result addign the
    # same number  of dashes as the number of digits of the larger
    # number plus two additional dashes.
    for element in results:
        separationLine = ("-" * (element[-1] + 2))

    # Determine if the output will display or not the result element of the
    # operation
    if validator is True:
        for element in results:
            # If the result has more digits than the largest element
            if len(str(element[3])) > element[-1]:
                total = (f" {element[3]}     ")
            else:
                total = (f"  {element[3]}     ")
    
    print(element1, "\n", element2, "\n", separationLine, "\n", total, "\n")


# If the arguments include a second argument with value of  "True", display
# the result. Otherwise, don't print the result
arithmetic_arranger(['32 - 698', '1 - 3801', '45 + 43',
                    '123 + 49', '988 + 40'], True)
