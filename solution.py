import time
start = time.time()


def solution(M, F): 
    M, F = int(M), int(F)                     # Convert inputs to integers
    
    cycles = 0                                # Initialize cycle count to zero
    
    while M != 1 or F != 1:                   # Continue loop until one of M or F equals 1
        if M <= 0 or F <= 0 or M == F:        # Check for impossible cases
            return "impossible" 
        elif M > F: 
            multiple = (M - 1) // F          # Calculate how many times F fits into M
            M -= multiple * F                # Subtract the appropriate multiple of F from M
            cycles += multiple               # Increment the cycle count by the multiple
        else: 
            multiple = (F - 1) // M         # Calculate how many times M fits into F
            F -= multiple * M               # Subtract the appropriate multiple of M from F
            cycles += multiple              # Increment the cycle count by the multiple

    return str(cycles) 


print(solution(2,4))
print(solution(1,2))
print(solution(2000000,400000000000))
print(solution(1,50000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000))
print(solution(7, 1147289))

end = time.time()
print("time elapsed: " , end - start)