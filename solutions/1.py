def part1(data):
    diff = 0
    left = []
    right = []
    for pair in data:
        vals = pair.split()
        left.append(int(vals[0]))
        right.append(int(vals[1]))
    left.sort()
    right.sort()
    for i in range(len(left)):
        diff += abs(left[i]-right[i])
    print(diff)

def part2(data):
    simscore = 0
    left = []
    right = []
    for pair in data:
        vals = pair.split()
        left.append(int(vals[0]))
        right.append(int(vals[1]))
    for i in range(len(left)):
        count = right.count(left[i])
        simscore += left[i]*count
    print(simscore)
def main():
    data = open("../inputs/1.txt")
    part1(data)
    data.seek(0)
    part2(data)
main()