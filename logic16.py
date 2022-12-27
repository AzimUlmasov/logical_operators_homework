def main(a):
    """
    Given integer a,  check the following statement "The integer is a five-digit number".
    Args:
        a(int): parameter a
    Returns:
        bool: answer
    """
    result = a >= 10000 and a < 100000

    return result

print(main(1346))