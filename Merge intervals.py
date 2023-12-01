def merge_intervals(intervals):
    if not intervals:
        return []

    # Sort intervals based on the start times
    intervals.sort(key=lambda x: x[0])

    merged = [intervals[0]]
    
    for i in range(1, len(intervals)):
        current_start, current_end = intervals[i]
        last_merged_start, last_merged_end = merged[-1]

        if current_start <= last_merged_end:
            # Update the end time of the last interval in 'merged'
            merged[-1][1] = max(last_merged_end, current_end)
        else:
            # No overlap, add the current interval to 'merged'
            merged.append([current_start, current_end])

    return merged

# Example
intervals = [[1,4],[4,5]]
result = merge_intervals(intervals)
print(result)
