def boyer_moore(text, pattern):
    m = len(pattern)
    n = len(text)
    if m == 0:
        return -1  # Invalid pattern
    
    # Preprocess the pattern
    last_occurrence = {}
    for i, char in enumerate(pattern):
        last_occurrence[char] = i
    
    # Searching phase
    i = m - 1  # Index for the end of the pattern
    j = m - 1  # Index for the end of the text window
    
    while i < n:
        if text[i] == pattern[j]:
            if j == 0:
                return i  # Match found
            else:
                i -= 1
                j -= 1
        else:
            if text[i] not in last_occurrence:
                i += m
            else:
                last_occurred = last_occurrence[text[i]]
                i += m - min(j, last_occurred + 1)
            j = m - 1  # Reset j to the end of pattern
    
    return -1  # Match not found

# Example usage
text = "ABAAABCD"
pattern = "ABC"
result = boyer_moore(text, pattern)
if result != -1:
    print(f"Pattern found at index {result}.")
else:
    print("Pattern not found.")
