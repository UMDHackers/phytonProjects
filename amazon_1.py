def cont_streak(lis, k):
    max = 0
    trail = 0
    temp_k = k
    if(len(lis) == 0):
        return 0
    if (len(lis) == 1):
        return 1 if lis[0] == 1 else 0
    for i in range(1, len(lis) - 1):
        if(lis[i-1] == 1):
            trail = trail  + 1
        else:
            if (temp_k == 0) :
                if (trail > max):
                    max = trail
                trail = 0;
                temp_k = k
            else:
                temp_k = temp_k - 1
                trail = trail + 1
    return max
if __name__ == "__main__":
    print cont_streak([1,1,0,0,1,1,1,0,1,1], 1)
