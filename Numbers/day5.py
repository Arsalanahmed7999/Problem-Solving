# Day 5: Sum of odd and even in a single function 

def sum_of_odd_even(n):
    odd_sum = 0
    even_sum = 0
    total_sum = 0

    for num in range(n + 1):
        if(num % 2 == 0):
            even_sum+=num
            # print(f"Even Sum: {even_sum}")
        elif(num % 2 != 0):
            odd_sum+=num
            # print(f"Odd Sum: {odd_sum}")
        total_sum+=num
        
    return (f"Even Sum: {even_sum}"), (f"Odd Sum: {odd_sum}"), (f"Total Sum: {total_sum}")

print(sum_of_odd_even(100))