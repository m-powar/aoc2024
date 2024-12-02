def part1(data:list[str]):
    levels = []
    count = 0
    for level in data:
        levels.append(level.rstrip().split())
    for level in levels:
        diff = 0
        incr = sorted(level,key=int,reverse=False)
        decr = sorted(level,key=int,reverse=True)
        valid = True
        if level != incr and level !=decr:
            continue
        else:
            for i in range(len(level)-1):
                diff = abs(int(level[i+1]) - int(level[i]))
                if abs(diff) <4 and abs(diff)>0:
                    pass
                else: 
                      valid = False
        if valid == True:
            count+=1
    print(count)


def part2(data:list[str]):
    levels = []
    count = 0
    for level in data:
        levels.append(level.rstrip().split())
    for level in levels:
       for i in range(len(level)):
            temp = level.copy()
            temp.pop(i) 
            diff = 0
            incr = sorted(temp,key=int,reverse=False)
            decr = sorted(temp,key=int,reverse=True)
            valid = True
            if temp != incr and temp !=decr:
                continue
            else:
                for i in range(len(temp)-1):
                    diff = abs(int(temp[i+1]) - int(temp[i]))
                    if abs(diff) <4 and abs(diff)>0:
                        pass
                    else: 
                            valid = False
            if valid == True:
                count+=1
                break
        
    print(count)   

def main():
    file = open("../inputs/2.txt")
    data1 = file.readlines()
    data2 = data1.copy()
    part1(data1)
    part2(data2)
main()