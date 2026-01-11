import heapq
def dijstra(start,graph):
   # 'sample graph->   
    #'build a map where each node has associated value of distance to get to that node'
    distanceGraph={node:float('infinity')for node in graph}
    distanceGraph[start]=0
    piority_queue=[(0,start)]
    while piority_queue:
        cur_distance,cur_node=heapq.heappop(piority_queue)
        if cur_distance>distanceGraph[cur_node]:continue
        for neighbour,weight in graph[cur_node]:
            distance=cur_distance+weight
            if distance>distanceGraph[neighbour]:
                distanceGraph[neighbour]=distance
                heapq.heappush(piority_queue,(distance,neighbour))
    return distance

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
        arr[0],arr[i]=arr[i],arr[0]
        heapify(0,i)
    return arr

