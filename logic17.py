def main(a):
    """
    Given a five-digit integer a,  check the following statement "All digits of the number are in ascending order".
    Args:
        a(int): parameter a
    Returns:
        bool: answer
    """
    x_1 = a % 10
    x_2 = a // 10 % 10
    x_3 = a // 100 % 10
    x_4 = a // 1000 % 10
    x_5 = a // 10000
    
    answer = x_5 > x_4 and x_4 > x_3 and x_3 > x_2 and x_2 > x_1
    return answer

print(main(75421))