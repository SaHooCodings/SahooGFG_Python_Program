import heapq
class Geeks:
    
    # Function to insert element into the queue
    def insert(self, q, k):
        
        # Your code here
        # Just insert k in q and don't return anything
        heapq.heappush(q,-k)
    
    # Function to find an element k
    def find(self, q, k):
        
        # Your code here
        # If k is in q return true else return false
        return -k in q
    
    # Function to delete the max element from queue
    def delete(self, q):

        # Your code here
        # Delete the max element from q. The priority queue property might be useful here
        return -heapq.heappop(q)
