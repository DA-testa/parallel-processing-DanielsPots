import heapq

def parallel_processing(n, m, data):
    # Initialize a priority queue with the first n jobs and the time it takes to process them
    pq = [(0, i) for i in range(n)]
    heapq.heapify(pq)

    # Initialize a list to keep track of the completion time for each job
    completion_time = [0] * m

    # Process the remaining jobs one by one
    for i in range(n, m):
        # Pop the next job from the priority queue and update the completion time
        processing_time, thread_idx = heapq.heappop(pq)
        completion_time[i] = processing_time
        # Add the next job to the priority queue with the updated processing time
        heapq.heappush(pq, (processing_time + data[i], thread_idx))
    
    # Process the remaining jobs in the priority queue
    while pq:
        processing_time, thread_idx = heapq.heappop(pq)
        completion_time[m-n+thread_idx] = processing_time
    
    # Create the output pairs
    output = [(i % n, completion_time[i]) for i in range(m)]
    return output

# Test case input
input_str = '2 5\n1 2 3 4 5\n'

# Call the function with the test case input
n, m = map(int, input_str.strip().split('\n')[0].split())
data = list(map(int, input_str.strip().split('\n')[1].split()))
result = parallel_processing(n, m, data)

# Print out the results, each pair in its own line
for thread_idx, start_time in result:
    print(thread_idx, start_time)
