import random

def insertionsort(arr):
    '''
    for each current element, find where it should be in,
    compare it with the previous elements
    '''
    for i in range(1,len(arr)):
        cur=arr[i]
        j=i-1
        while cur<arr[j]and j>=0:
            arr[j+1]=arr[j]
            j=j-1
        arr[j+1]=cur

def selectionsort(arr):
    '''
    for each current element, we set it to be the min first, 
    then compare each element behind it,find the smallest one,
    swap the current element with the smallest one behind it
    '''

    length =len(arr)
    l=length-1
    for i in range(l):
        min=arr[i]
        minindex=i
        for j in range(i+1,length):
            if arr[j]<min:
                min=arr[j]
                minindex=j
        arr[i],arr[minindex]=arr[minindex],arr[i]
    return arr

def selectionsort2(arr:list):
    l=len(arr)
    for i in range(l-1):
        cur_list=arr[i+1:]
        cur_min=min(cur_list)
        min_index=arr.index(cur_min)
        if arr[i]>arr[min_index]:
            arr[i],arr[min_index],=arr[min_index],arr[i]
    
def quicksort(arr):
    'this is a simplified version of quicksort'

    '''
    each time,
    choose the last element as the pivot,
    find the list of elements smaller than it and bigger than it
    reculsively the quicksort function using these two lists
    '''

    l=len(arr)
    if l<2:return arr
    pivot=arr[-1]
    #exclude the pivot
    smaller=[x for x in arr[:-1] if x<pivot]
    bigger=[x for x in arr[:-1] if x>=pivot]
    left=quicksort(smaller)
    right=quicksort(bigger)
    return left+[pivot]+right

def quicksort2(arr,start,end):
    '''
    classic version
    '''

    def partition(arr,start,end)->int:
        #we choose the num at index end as pivot
        #goal is to put pivot at its correct position
        pivot=arr[end]
        j=start
        for i in range(start,end):
            if arr[i]<pivot:
                arr[j],arr[i]=arr[i],arr[j]
                j+=1
        arr[end],arr[j]=arr[j],arr[end]
        return j
    
    if len(arr)==1:
        return 
    if start>=end:
        return
    #pi is final index(position)of the pivot we just chose
    pi=partition(arr,start,end)
    quicksort2(arr,start,pi-1)
    quicksort2(arr,pi+1,end)

def quicksort3(arr,start=0,end=None):
    if not end:
        end =len(arr)
    '''
    random pivot
    '''

    def partition(arr,start,end)->int:
        #we choose the num at index as pivot
        #goal is to put pivot at its correct position
        #index j is for tracking the position for number less than pivot

        index=random.randint(start,end-1)
        pivot=arr[index]
        j=start
        for i in range(start,end):
            if arr[i]<pivot:
                arr[j],arr[i]=arr[i],arr[j]
                if j==index:
                    index=i
                
                j+=1
        arr[index],arr[j]=arr[j],arr[index]
        return j
    
    if len(arr)==1:
        return 
    if start>=end:
        return
    
    #pi is final index(position)of the pivot we just chose
    pi=partition(arr,start,end)
    quicksort3(arr,start,pi-1)
    quicksort3(arr,pi+1,end)

def mergesort(arr):

    def merge(left,right):
        len1=len(left)
        len2=len(right)
        list=[0]*(len1+len2)
        i,j,k=0,0,0
        while i<len1 and j<len2:
            if left[i]<right[j]:
                list[k]=left[i]
                i=i+1
            else :
                list[k]=right[j]
                j=j+1
            k=k+1
        while i<len1:
            list[k]=left[i]
            k=k+1
            i=i+1
        while j<len2:
            list[k]=right[j]
            k=k+1
            j=j+1    
        return list
    
    if len(arr)<=1:return arr

    half=int(len(arr)/2)
    left=mergesort(arr[0:half])
    right=mergesort(arr[half:])
    
    return merge(left,right)

def heapsort(arr):
    length=len(arr)
    def heapify(i,len):
        #make sure that each parent's value is greater than its left and right child
        largest=i
        left=2*i
        right=2*i+1
        if left<len and arr[largest]<arr[left]:
            largest=left
        if right<len and arr[largest]<arr[right]:
            largest=right
        if largest!=i:
            arr[i],arr[largest]=arr[largest],arr[i]
            heapify(largest,len)

    for i in range(length//2-1,-1,-1):
        heapify(i,length)
    
    for i in range(length-1,0,-1):
        #after heapifying,the first element is going to be the greatest, then swap it with the last element
        #to put it in its correct position
        arr[0],arr[i]=arr[i],arr[0]
        heapify(0,i)
    return arr

def counting_sort(arr):
    '''
    get the maximun number of the arr, and 
    set the length of our count array to be max+1,
    since the arr of len m+1 has the largest index of m
    '''
    m=max(arr)
    arr_count=[0 for i in range(m+1)]
    for num in arr:
        #count of the number of ouccurence of each num in thr list
        arr_count[num]+=1
    arr=[]
    for num,count in enumerate(arr_count):
        if count>0:
            arr+=[num]*count
    return arr