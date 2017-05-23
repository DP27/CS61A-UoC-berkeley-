def cube(x):
    return x*x*x
def run_test():
    print("should be 1:",cube(1))
    print("should be 8:",cube(2))
    print("should be 27:",cube(3))

from ucb import main
@main
def main():
    print("Start Program")
    run_test()
    print("End of the program")
    
