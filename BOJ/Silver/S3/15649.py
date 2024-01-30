n, m = map(int, input().split())
answer = []

def print_num():
    print(*answer)

def choose(cur_num):
    if cur_num == m + 1:
        print_num()
        return

    for i in range(1, n+1):
        if i in answer:
            continue
        answer.append(i)
        choose(cur_num+1)
        answer.pop()
    
    return

choose(1)
