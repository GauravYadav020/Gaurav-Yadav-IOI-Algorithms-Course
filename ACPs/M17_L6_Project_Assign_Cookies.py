# Module 17 Lesson 6: After-Class Project
# Project Name: Greedy Satisfaction Index Maximum Element Matcher

def maximize_satisfied_children(greed_factors_list, size_provisions_list):
    greed_factors_list.sort(); size_provisions_list.sort()
    child_ptr = cookie_ptr = 0
    while child_ptr < len(greed_factors_list) and cookie_ptr < len(size_provisions_list):
        if size_provisions_list[cookie_ptr] >= greed_factors_list[child_ptr]: child_ptr += 1
        cookie_ptr += 1
    return child_ptr

if __name__ == "__main__":
    print(f"Maximum allocation count satisfied targets matching rules parameters: {maximize_satisfied_children([1, 2, 3], [1, 1])}")