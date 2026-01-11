def main():
    list=[23,2,1]
    print ( [num for num in list if num==uniqueNum(list)])

def insertionsort(arr):
    for i in range(1,len(arr)):
        cur=arr[i]
        j=i-1
        while cur<arr[j]and j>=0:
            arr[j+1]=arr[j]
            j=j-1
        arr[j+1]=cur

def uniqueNum(arr):
    re=-999
    for num in arr:
         if num > re and num>transformNum(num):
             re=num
             

def transformNum(num):
    num=abs(num)
    l=0
    sum=0
    while num>0:
        sum+=num%10
        num=num/num
        l=l+1
    return sum*l
main()