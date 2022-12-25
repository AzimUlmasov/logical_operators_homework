def main(a):
    """
    Given integer a,  check the following statement "The integer is three-digit number".
    Args:
        a(int): parameter a
    Returns:
        bool: answer
    """
    result = a >= 100 and a < 1000

    return result

print(main(210))