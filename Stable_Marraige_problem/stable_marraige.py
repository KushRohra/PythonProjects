import queue

N = int(input("Enter no of men or women: "))

preferList = []

for i in range(0, 2 * N):
    if i < N:
        print("Enter preference List for Men " + str(
            i + 1) + " and the list must contains serial No of Women from 1 to " + str(N) + ": ")
        j = 0
        temp = []
        while j < N:
            choice = int(input("Enter prefernce choice " + str(j + 1) + ": "))
            if choice < 1 or choice > N:
                continue
            else:
                j += 1
                temp.append(choice + N - 1)
    else:
        print("Enter preference List for Women " + str(
            i + 1 - N) + " and the list must contains serial No of Men from 1 to " + str(N) + ": ")
        j = 0
        temp = []
        while j < N:
            choice = int(input("Enter prefernce choice " + str(j + 1) + ": "))
            if choice < 1 or choice > N:
                continue
            else:
                j += 1
                temp.append(choice - 1)
    preferList.append(temp)

menFree = queue.Queue()
for i in range(N):
    menFree.put(i)
womenFree = [-1 for i in range(N)]

while menFree.qsize() > 0:
    man = menFree.get()
    for i in range(N):
        woman = preferList[man][i] - N
        if womenFree[woman] == -1:
            womenFree[woman] = man
            break
        else:
            currChoice = womenFree[woman]
            for j in range(N):
                choice = preferList[woman + N][j]
                if choice == currChoice:
                    pos1 = i
            pos2 = N + 1
            for j in range(pos1):
                choice = preferList[woman + N][j]
                if choice == man:
                    pos2 = i
            if pos2 < pos1:
                womenFree[i] = man
                menFree.put(currChoice)
                break

for i in range(N):
    print("Man " + str(womenFree[i] + 1) + " is paired with Woman " + str(i + N) + ".")
