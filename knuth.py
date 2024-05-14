def kmp_search(text, pattern):
    n = len(text)
    m = len(pattern)
    if m == 0:
        return 0  # Empty pattern matches any position

    # Build prefix table (also known as failure function)
    pi = compute_prefix_function(pattern)

    # Searching phase
    q = 0  # Number of characters matched
    for i in range(n):
        while q > 0 and pattern[q] != text[i]:
            q = pi[q - 1]
        if pattern[q] == text[i]:
            q += 1
        if q == m:
            return i - m + 1

    return -1  # Pattern not found

def compute_prefix_function(pattern):
    m = len(pattern)
    pi = [0] * m
    k = 0
    for q in range(1, m):
        while k > 0 and pattern[k] != pattern[q]:
            k = pi[k - 1]
        if pattern[k] == pattern[q]:
            k += 1
        pi[q] = k
    return pi

# Example usage
text = "ABABDABACDABABCABAB"
pattern = "ABABCABAB"
result = kmp_search(text, pattern)
if result != -1:
    print(f"Pattern found at index {result}.")
else:
    print("Pattern not found.")
