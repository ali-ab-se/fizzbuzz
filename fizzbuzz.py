def fizzbuzz(n: int) -> list:
    """
    Implementation of FizzBuzz function.
    Returns a list of strings representing the FizzBuzz sequence up to n.

    Parameters:
    n (int): The upper limit of the range.

    Returns:
    list of str: List containing Fizz, Buzz, FizzBuzz, or the numbers.
    """
    return [('Fizz' * (i % 3 == 0) + 'Buzz' * (i % 5 == 0)) or str(i) for i in range(1, n + 1)]


def main():
    """
    Main function to execute FizzBuzz function.
    """
    try:
        limit = int(
            input("Enter the limit for FizzBuzz, ( * Tip: enter a positive integer > 0 ): "))
        if limit < 1:
            print("Please enter a positive integer greater than zero.")
            return
        result = fizzbuzz(limit)
        print(', '.join(result))
    except ValueError:
        print("Invalid input! Please enter a valid integer.")


if __name__ == "__main__":
    main()
