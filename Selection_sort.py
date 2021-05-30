#function selection_sort that takes a list as argument.
def selection_sort(alist):
    for i in range(0, len(alist) - 1):
        smallest = i
        for j in range(i + 1, len(alist)):
            if alist[j] < alist[smallest]:
                smallest = j
        alist[i], alist[smallest] = alist[smallest], alist[i]
 
alist=[66,18,28,47,5,13,19,72,33,9,18,11,39] 
#alist = input('Enter the list of numbers: ').split()
alist = [int(x) for x in alist]
#The list is passed to the selection_sort function.
selection_sort(alist)
#The sorted list is displayed.
print('Sorted list: ', end='')
print(alist)
