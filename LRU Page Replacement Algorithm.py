from collections import deque

def lru_page_fault(pages, capacity):
    if capacity <= 0:
        return "Capacity should be greater than 0."

    page_faults = 0
    page_queue = deque(maxlen=capacity)
    page_set = set()

    for page in pages:
        if page not in page_set:
            page_set.add(page)

            if len(page_queue) >= capacity:
                page_removed = page_queue.popleft()
                page_set.remove(page_removed)

            page_queue.append(page)
            page_faults += 1
        else:
            page_queue.remove(page)
            page_queue.append(page)

    return page_faults

# Example usage:
pages = [1, 2, 3, 2, 1, 5, 2, 1, 6, 2, 5, 6, 3, 1, 3]
capacity = 3
total_faults = lru_page_fault(pages, capacity)
print("Total page faults using LRU algorithm:", total_faults)
