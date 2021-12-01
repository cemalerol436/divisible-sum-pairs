def divi():

    dividing_number = 3
    given_array = [1, 2, 3, 4, 5, 6]
    i=0
    total_numbers = []


    #Using loop checking the numbers if they are divisible with dividing number.

    for num1 in given_array:

        for num2 in given_array[(i+1):]:

            if ((num1+num2)%dividing_number)==0:
                res = num1 + num2
                total_numbers.append(res)
        i += 1

    #It returns an integer which is total number of the two numbers which are consist of two numbers in array.

    return print(len(total_numbers))

divi()
