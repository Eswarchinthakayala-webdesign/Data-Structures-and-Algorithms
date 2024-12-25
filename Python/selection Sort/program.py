nums=[2,3,4,1,5,10,9,9,7,8]


def getIndex(nums, start, last):
    max=start
    for i in range(start,last+1):
        if(nums[max]<nums[i]):
            max=i
    return max

def swap(first,second):
    nums[first],nums[second]=nums[second],nums[first]
def main():
    for i in range(len(nums)):
        last=len(nums)-i-1
        maxIndex=getIndex(nums,0,last)
        swap(last,maxIndex)
    print(nums)

main()
