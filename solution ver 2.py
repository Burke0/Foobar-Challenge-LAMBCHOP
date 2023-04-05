import time
start = time.time()


def solution(M, F):
    M, F = int(M), int(F)
    
    cycles = 0
    
    while True:
        if M==1 and F==1:
            return str(cycles)
        elif M <= 0 or F <= 0 or M==F:
            return "impossible"
        else:
            if M > F:
                if M >10*F:
                    multiple = (int(M/F)-1)
                    cycles += multiple
                    M=M-(multiple * F)
                else:
                    M -= F
                    cycles += 1
            else: 
                if F > 10*M:
                    multiple = (int(F/M)-1)
                    cycles += multiple
                    F = F - (multiple * M)
                else:
                    F-=M
                    cycles += 1
                    

print(solution(2,4))
print(solution(1,2))
print(solution(2000000,400000000000))
print(solution(1,50000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000))
print(solution(7, 1147289))

end = time.time()
print("time elapsed: " , end - start)


