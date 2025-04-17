def get_median_font_size(font_sizes):
    """
    def get_median_font_size(font_sizes):
        if len(font_sizes) == 0:
            return None
        return sorted(font_sizes)[(len(font_sizes) - 1) // 2]
    """

    len_font_sizes = len(font_sizes)

    if len_font_sizes == 0:
        return None

    ordered_font_sizes = sorted(font_sizes)
    median_index = len(ordered_font_sizes) // 2

    if len_font_sizes % 2 == 0:
        median_font_size = min(ordered_font_sizes[median_index], ordered_font_sizes[median_index - 1])
    else:
        median_font_size = ordered_font_sizes[median_index]

    return median_font_size


# Tests


test_cases = [
    ([4, 3, 2, 1, 5], 3),
    ([20, 14, 16], 16),
    ([9, 11, 16, 20], 11),
    ([8, 8, 8], 8),
    ([30, 18, 14, 22], 18),
    ([6, 24, 6, 6, 24, 24, 2, 1, 3], 6),
    ([], None),
]


def test(input, expected_output):
    print("---------------------------------")
    print(f"Input: {input}")
    print(f"Expected: {expected_output}")

    input_copy = input.copy()
    result = get_median_font_size(input)

    print(f"Actual: {result}")

    if result != expected_output:
        print("Fail")
        return False
    
    if input != input_copy:
        print(f"Expected font_sizes: {input_copy}")
        print(f"Actual font_sizes: {input}")
        print("font_sizes was modified")
        print("Fail")
        return False

    print("Pass")

    return True


def main():
    passed = 0
    failed = 0

    for test_case in test_cases:
        correct = test(*test_case)

        if correct:
            passed += 1
        else:
            failed += 1

    if failed == 0:
        print("============= PASS ==============")
    else:
        print("============= FAIL ==============")

    print(f"{passed} passed, {failed} failed")


if __name__ == "__main__":
    main()
