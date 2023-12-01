def find_content_children(g, s):
    # Sort the children's greed factors and the available cookies
    g.sort()
    s.sort()
    
    content_children = 0
    child_index = 0
    
    for cookie in s:
        if child_index == len(g):
            break  # No more children to satisfy
            
        # If the cookie satisfies the current child's greed
        if cookie >= g[child_index]:
            content_children += 1
            child_index += 1  # Move to the next child
    
    return content_children



greed_factors = [1, 2, 3]
cookie_sizes = [1, 1]

result = find_content_children(greed_factors, cookie_sizes)
print("Maximum content children:", result)
