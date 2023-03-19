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
    output = [(i%n, completion_time[i]) for i in range(m)]
    return output

def main():
    # Read input from test case
    n, m = map(int, input().strip().split())
    data = list(map(int, input().strip().split()))

    # Call the function
    result = parallel_processing(n, m, data)
    
    # Print out the results, each pair in its own line
    output = ""
    for thread_idx, start_time in result:
        output += str(thread_idx) + " " + str(start_time) + "\n"
    print(output.strip())

if __name__ == "__main__":
    main()
