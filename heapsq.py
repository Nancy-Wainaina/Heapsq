import heapq

def k_largest_elements(arr, k):
    
    max_heap = [-x for x in arr]
    heapq.heapify(max_heap)
    
    largest_elements = []
    for _ in range(k):
        largest_elements.append(-heapq.heappop(max_heap))
    
    return largest_elements


arr = [3, 2, 1, 5, 6, 4]
k = 2

print(k_largest_elements(arr, k))