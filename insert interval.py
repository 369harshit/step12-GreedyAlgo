def insert_interval(intervals, newInterval):
    result = []
    i = 0
    n = len(intervals)

    # Add all intervals that come before the newInterval
    while i < n and intervals[i][1] < newInterval[0]:
        result.append(intervals[i])
        i += 1

    # Merge overlapping intervals
    while i < n and intervals[i][0] <= newInterval[1]:
        newInterval[0] = min(newInterval[0], intervals[i][0])
        newInterval[1] = max(newInterval[1], intervals[i][1])
        i += 1

    # Add the merged interval
    result.append(newInterval)

    # Add remaining intervals after merging
    while i < n:
        result.append(intervals[i])
        i += 1

    return result

# Example
intervals = [[1,3],[6,9]]
newInterval = [2,5]
result = insert_interval(intervals, newInterval)
print(result)
