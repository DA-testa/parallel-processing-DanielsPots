# python3

def parallel_processing(n, m, data):
    output = []
    next_free_time = [0] * n
    for i in range(m):
        # Find the thread with the earliest free time
        min_free_time = min(next_free_time)
        j = next_free_time.index(min_free_time)
        # Assign the job to the thread and update its free time
        output.append((j, min_free_time))
        next_free_time[j] += data[i]
    return output


def main():
    # Read input from keyboard
    n, m = map(int, input().split())
    data = list(map(int, input().split()))

    # Call the function
    result = parallel_processing(n, m, data)

    # Print the output
    for thread, start_time in result:
        print(thread, start_time)




if __name__ == "__main__":
    main()