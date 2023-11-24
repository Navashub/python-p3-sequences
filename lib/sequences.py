#!/usr/bin/env python3

# def print_fibonacci(length):
#     if not isinstance(length, int) or length <= 0:
#         print("Error: Please provide a positive int length.")
        
#     x, y = 0, 1
#     fib_sequence = [x, y]

#     while len(fib_sequence) < length:
#         x, y = y, x + y
#         fib_sequence.append(y)

#     print(f"Fibonacci sequence up to length {length}:")
#     print(fib_sequence)


# print_fibonacci(9)



def print_fibonacci(length):
    num_list = list()
    if length == 0:
      print(num_list)
      return;
    
    for i in range(length):
        if len(num_list) > 1:
            next_number = num_list[-1] + num_list[-2]
            num_list.append(next_number)
            
        else:
            num_list.append(i)

    print(num_list)
print_fibonacci(100)