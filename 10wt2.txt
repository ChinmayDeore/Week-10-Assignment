## Chinmay D. 11/9/2022 Hg5590
def print_range(start,end):
# Naming and starting the function with starting and ending parameters.
    if start==end:
        print(start)
    else:
        if start<end:
            print(start)
            print_range(start + 1,end)
        else:
            print(end)
            print_range(start, end + 1)
# Ensures code prints out the numbers when start is larger/smaller than end.
start = int(input("First integer: "))
end = int(input("Last integer: "))
# Accepts input for the start and end integer parameters. 
print_range(start,end)
# Prints the range of numbers from start to end.
## HALF-LIFE, Ron Bass, John Richards Sr., After-Burner Elite