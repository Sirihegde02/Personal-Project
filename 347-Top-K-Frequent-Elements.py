class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #Solution-1 (Sorting):

        # my_dict = {}
        # #Putting all the numbers into a dictionary to count their frequencies:
        # for num in nums:
        #     if num in my_dict:
        #         my_dict[num] += my_dict.get(num, 0)
        # #Sorting the dictionary in descending order to have the top values (of frequences) be in the beginning.
        # #The lambda function lets us use the sorted() function on the tuples by sorting them in accordance with tuple's values (item[1])
        # sorted_dict = sorted(my_dict.items(), key=lambda item: item[1], reverse = True)
        # #The result will look at all the tuples before the k+1th pair and will append its keys (item[0]) into result
        # result = [item[0] for item in sorted_dict[:k]]
        # return result

        #Solution-2 (Using a heap):
        
        # counts = {}
        # for num in nums:
        #     if num in counts:
        #         counts[num] += 1
        #     else:
        #         counts[num] = 1
        # heap = []
        # for num in counts.keys():
        #     #Push the tuple of the count value with the num:
        #     heapq.heappush(heap, (count[num], num))
        #     #Only collect k, pop to maintain the length to be k:
        #     if len(heap) > k:
        #         heapq.heappop(heap)
        # res = []
        # for i in range(k):
        #     #Pop the smallest element (by frequency) from the heap and append the number to the result:
        #     res.append(heapq.heappop(heap)[1])
        # return res

        #Solution-3 (Using Bucket Sort):

        counts = {}
        frequencies = [] #List that will be the same size as nums
        for i in range(len(nums) + 1):
            frequencies.append([])
        for num in nums:
            counts[num] = 1 + counts.get(num, 0)
        for num, cnt in counts.items():
            frequencies[cnt].append(num) 
        
        res = []
        for i in range(len(frequencies) - 1, 0, -1):
            for n in frequencies[i]:
                res.append(n)
                if len(res) == k:
                    return res
        