'''
if __name__ == "__main__":
    N = 10
    # input data
    print 'please input ten num:\n'
    l = []
    for i in range(N):
        l.append(int(raw_input('input a number:\n')))
    print
    for i in range(N):
        print l[i]
    print

    #sort ten num
    for i in range(N - 1):
        min = i
        for j in range(i + 1,N):
            if l[min] > l[j]:min = j
        l[i],l[min] = l[min],l[i]
    print 'after sorted'
    for i in range(N):
        print l[i]
'''
'''
if __name__ == '__main__':
    a = []
    sum = 0.0
    for i in range(3):
        a.append([i])
        for j in range(i):
            a[i].append(float(raw_input("input num:\n")))
    for i in range(3):
        sum += a[i][i]
    print sum
    print a
'''
'''
if __name__ == '__main__':
    #insert another number
    a = [1,4,6,9,13,16,19,28,40,100,0]
    print 'original list is:'
    for i in range(len(a)):
        print a[i]
    number = int(raw_input("insert a new number:\n"))
    end = a[9]
    if number > end:
        a[10] = number
    else:
        for i in range(10):
            if a[i] > numer:
                temp1 = a[i]
                a[i] = number
                for j in range(i + 1,11):
                    temp2 = a[j]
                    a[j] = temp1
                    temp1 = temp2
                break
    for i in range(11):
        print a[i]
'''
'''
num = 2
def autofunc():
    num = 1
    print 'internal block num = %d' % num
    num += 1
for i in range(3):
    print 'The num = %d' % num
    num += 1
    autofunc()
'''
'''
import external
if __name__ == '__main__':
    print external.add(10,20)
'''


