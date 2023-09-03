def oxford_comma(items):
    if len(items) >= 3:
        items[-1] = f"and {items[-1]}"
    return ', '.join(items)

# Example usage:
items = ["apple", "banana", "cherry"]
result = oxford_comma(items)
print(result)
