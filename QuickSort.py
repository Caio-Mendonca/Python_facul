def quickSort(list):
   quickSortHelper(list,0,len(list)-1)

def quickSortHelper(list,first,last):
   if first<last:

       splitpoint = partition(list,first,last)

       quickSortHelper(list,first,splitpoint-1)
       quickSortHelper(list,splitpoint+1,last)


def partition(list,first,last):
   pivo = list[first]

   leftmark = first+1
   rightmark = last

   done = False
   while not done:

       while leftmark <= rightmark and list[leftmark] <= pivo:
           leftmark = leftmark + 1

       while list[rightmark] >= pivo and rightmark >= leftmark:
           rightmark = rightmark -1

       if rightmark < leftmark:
           done = True
       else:
           temp = list[leftmark]
           list[leftmark] = list[rightmark]
           list[rightmark] = temp

   temp = list[first]
   list[first] = list[rightmark]
   list[rightmark] = temp


   return rightmark

lista = [54,26,93,17,77,31,44,55,20]
quickSort(lista)
print(lista)
