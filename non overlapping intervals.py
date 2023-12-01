def nonOverlapIntervals(intervals):
    if not intervals:
        return 0

    intervals.sort(key=lambda x: x[1])  # Sort intervals by their end times
    count = 0
    end = intervals[0][1]

    for i in range(1, len(intervals)):
        if intervals[i][0] < end:  # Overlapping intervals found
            count += 1  # Increment count as we need to remove an interval
        else:
            end = intervals[i][1]  # Update end time

    return count

intervals =[[1,2],[2,3]]
print(nonOverlapIntervals(intervals))  # Output: 1
