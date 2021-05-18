import sys
def convert_f2c(S):
    """ (str) : float 
converts a Farenhiet temperature rep as a string to Celsius. """

    Fahrenheit = float(S)
    celsious = (Fahrenheit - 32) * 5/9 
    return celsious 

def main():
    if len(sys.argv) == 1:
        print('Usage: {} temp1 temp2 ....',format(sys.argv[0]))
        sys.exit(0)

    for arg in sys.argv[1:]:
        try:
            celsious = convert_f2c(arg)
        except ValueError:
            print("{!r} is not a numeri value".format(arg),file=sys.stderr)
        else:
            print('{}\N{DEGREE SIGN}F = {:g}\N{DEGREE SIGN}C'.format(arg, round(celsius, 0)))

        if __name__ == '__main__':
import sys

def convert_f2c(S):
    """ (str) : float 
converts a Farenhiet temperature rep as a string to Celsius. """

    Fahrenheit = float(S)
    celsious = (Fahrenheit - 32) * 5/9 
    return celsious 

def main():
    if len(sys.argv) == 1:
        print('Usage: {} temp1 temp2 ....',format(sys.argv[0]))
        sys.exit(0)

    for arg in sys.argv[1:]:
        try:
            celsious = convert_f2c(arg)
        except ValueError:
            print("{!r} is not a numeri value".format(arg),file=sys.stderr)
        else:
            print('{}\N{DEGREE SIGN}F = {:g}\N{DEGREE SIGN}C'.format(arg, round(celsius, 0)))

if __name__ == '__main__':
            main()
   