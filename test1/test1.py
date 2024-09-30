# test1
i = 1
answer = ""
complete = False

answer += str(i)

while True:
    #print("Enter two whole positive numbers, divided by a Space")
    try:
        n, m = map(int, input().split())
        complete = True
    except:
        #print("Try again")
        pass
    
    if complete:
        break

while True:
    # Formula is (i + m - 1) % n
    # need -2 then +1 so no zeroes
    i = 1 + (i + m - 2) % n

    if i == 1:
        break
    else:
        answer += str(i)

print(answer)

input()