#coding=utf-8

#文件功能:提供一些基础排序算法

#----------------------函数说明开始----------------------#
#函数功能:冒泡排序
#函数参数:sortList:list
#函数返回值类型:list
#备注:无
#----------------------函数说明结束----------------------#
def BubbleSort(sortList:list):
    size = len(sortList)
    for i in range(0,size - 1):
        for j in range(0,size - 1 - i):
            if(sortList[j] > sortList[j+1]):
                tmp = sortList[j+1]
                sortList[j+1] = sortList[j]
                sortList[j] = tmp
    return sortList

#----------------------函数说明开始----------------------#
#函数功能:选择排序
#函数参数:sortList:list
#函数返回值类型:list
#备注:无
#----------------------函数说明结束----------------------#
def SelectionSort(sortList:list):
    size = len(sortList)
    for i in range(0,size):
        minIndex = i
        for j in range(i+1,size):
            if(sortList[j] < sortList[minIndex]):
                minIndex = j
        tmp = sortList[i]
        sortList[i] = sortList[minIndex]
        sortList[minIndex] = tmp
    return sortList

#----------------------函数说明开始----------------------#
#函数功能:插入排序
#函数参数:sortList:list
#函数返回值类型:list
#备注:无
#----------------------函数说明结束----------------------#
def InsertionSort(sortList:list):
    size = len(sortList)
    for i in range(1,size):
        preIndex = i - 1
        current = sortList[i]
        while(preIndex >= 0 and sortList[preIndex] > current):
            sortList[preIndex + 1] = sortList[preIndex]
            preIndex -= 1
        sortList[preIndex + 1] = current
    return sortList

#----------------------函数说明开始----------------------#
#函数功能:希尔排序
#函数参数:sortList:list
#函数返回值类型:list
#备注:无
#----------------------函数说明结束----------------------#
def ShellSort(sortList:list):
    size = len(sortList)
    gap = int(size / 2)
    while gap > 0:
        for i in range(gap,size):
            j = i
            current = sortList[i]
            while j - gap >= 0 and current < sortList[j - gap]:
                sortList[j] = sortList[j - gap]
                j = j - gap
            sortList[j] = current
        gap = int(gap / 2)
    return sortList

if __name__ == '__main__':
    x = [9,8,7,6,5,4,3,2,1]
    print(ShellSort(x))

