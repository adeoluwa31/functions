def reverse_number(digit):
    reversed_number: int = 0

    while digit > 0:

        digit = digit % 10

        reversed_number = (reversed_number * 10) + digit

        digit = digit // 10
    return reversed_number


number = int(input("Enter a number: "))
reversed_number = reverse_number(number)
print("Reversed number:", reversed_number)
