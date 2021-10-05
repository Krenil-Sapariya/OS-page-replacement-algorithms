def fifo(refStr,frames):
    refString = refStr[:]
    q = []
    cnt = frames

    for i in range(frames):
        q.append(refString[0])
        refString.pop(0)

    # print(q,"After initial ass")
    
    for i in refString:
        if i in q:
            # print(i,"found ! in ",q)
            continue
        else:
            cnt+=1
            # print(i, "not found! ",q)
            q.pop(0)
            # print("after pop", q)
            q.append(i)
            # print(i," appended ",q)
    return cnt



# Logic: when one page is referenced and present in frame then move that to the last block of arr
# if page is not present then remove first page and append new page at the end
def LRU(refStr, frames):

    refString = refStr[:]
    q = [None]*frames
    cnt = frames

    for i in range(frames):
        q[i] = refString[0]
        refString.pop(0)

    # print("Initial ass ",q)

    for i in refString:
        if i in q:
            # print(i," found in ",q)
            index = q.index(i)
            q.remove(i)
            q.append(i)
            # q[0] , q[index] = q[index] , q[0]
            # print(i," swaped at first from index ",index," -> ",q)
            continue
        else:
            cnt+=1
            # print(i,"  not in ", q)
            q.pop(0)
            q.append(i)
            # print(q)
    
    return cnt


def MRU(refStr, frames):

    refString = refStr[:]
    q = [None]*frames
    cnt = frames

    for i in range(frames):
        q[i] = refString[0]
        refString.pop(0)

    # print("Initial ass ",q)

    for i in refString:
        if i in q:
            # print(i," found in ",q)
            index = q.index(i)
            q.remove(i)
            q.append(i)
            # q[0] , q[index] = q[index] , q[0]
            # print(i," swaped at first from index ",index," -> ",q)
            continue
        else:
            cnt+=1
            # print(i,"  not in ", q)
            q.pop(-1)
            q.append(i)
            # print(q)
    
    return cnt




if __name__=="__main__":

    refString = [7,0,1,2,0,3,0,4,2,3,0,3,2,1,2,0,1,7,0,1]
    
    # FIFO
    print("------------------FIFO-------------------")
    print("\nreference string:", refString)
    print("frames: 3")
    print("page faults: ", fifo(refString,3))

    print("\nreference string:", refString)
    print("frames: 4")
    print("page faults: ", fifo(refString,4))

    # LRU
    print("------------------LRU-------------------")
    print("\nreference string:", refString)
    print("frames: 3")
    print("page faults: ", LRU(refString,3))

    print("\nreference string:", refString)
    print("frames: 4")
    print("page faults: ", LRU(refString,4))

    #MRU
    print("------------------MRU-------------------")
    print("\nreference string:", refString)
    print("frames: 3")
    print("page faults: ", MRU(refString,3))

    print("\nreference string:", refString)
    print("frames: 4")
    print("page faults: ", MRU(refString,4))





    refString2 = [6,1,2,3,4,2,1,4,1,2,3,5,6,2,1,4,1,3,6,5,1]

    # FIFO
    print("------------------FIFO-------------------")
    print("\nreference string:", refString2)
    print("frames: 3")
    print("page faults: ", fifo(refString2,3))

    print("\nreference string:", refString2)
    print("frames: 4")
    print("page faults: ", fifo(refString2,4))

    # LRU
    print("------------------LRU-------------------")
    print("\nreference string:", refString2)
    print("frames: 3")
    print("page faults: ", LRU(refString2,3))

    print("\nreference string:", refString2)
    print("frames: 4")
    print("page faults: ", LRU(refString2,4))

    #MRU
    print("------------------MRU-------------------")
    print("\nreference string:", refString2)
    print("frames: 3")
    print("page faults: ", MRU(refString2,3))

    print("\nreference string:", refString2)
    print("frames: 4")
    print("page faults: ", MRU(refString2,4))
