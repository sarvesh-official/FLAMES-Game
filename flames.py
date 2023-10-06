def calculate_flames(name1, name2):
    # Convert names to uppercase and remove spaces
    name1 = name1.upper().replace(" ", "")
    name2 = name2.upper().replace(" ", "")

    char_count = {}

    for char in name1:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    for char in name2:
        if char in char_count:
            char_count[char] -= 1
        else:
            char_count[char] = -1

    total_count = 0
    for count in char_count.values():
        total_count += abs(count)

    result_order = ["F", "L", "A", "M", "E", "S"]

    index = 0
    while len(result_order) > 1:
        index = (index + total_count - 1) % len(result_order)
        result_order.pop(index)

    return result_order[0]

name1 = input("Enter the first name: ")
name2 = input("Enter the second name: ")

result = calculate_flames(name1, name2)
print(f"The relationship between {name1} and {name2} is: {result}")


