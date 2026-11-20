element = [26, 21, 33, 41, 20, 11]


def large_elt():
    global element
    large = max(element)
    for i in element:
        if i == large:
            element.remove(large)
    # print(element)
    lar = max(element)
    return lar


b = large_elt()
print("Second largest element:", b)
