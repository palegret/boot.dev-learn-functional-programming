def hex_to_rgb(hex_color):
    if (not is_valid_hex_color_string(hex_color)):
        raise ValueError("not a hex color string")
    
    r = int(hex_color[:2], 16)
    g = int(hex_color[2:4], 16)
    b = int(hex_color[4:], 16)

    return r, g, b


def is_valid_hex_color_string(hex_color):
    try:
        return not (
            hex_color == None
            or len(str(hex_color)) < 6
            or not is_hexadecimal(hex_color)
        )
    except Exception:
        return False


def is_hexadecimal(hex_string):
    try:
        int(hex_string, 16)
        return True
    except Exception:
        return False


# Tests


test_cases = [
    (
        "00FFFF",
        (0, 255, 255),
    ),
    (
        "FFFF00",
        (255, 255, 0),
    ),
    (
        "Hello!",
        None,
        "not a hex color string",
    ),
    (
        "42",
        None,
        "not a hex color string",
    ),
    (
        1_000_000,
        None,
        "not a hex color string",
    ),
    (
        "",
        None,
        "not a hex color string",
    ),
    (
        "FF00FF",
        (255, 0, 255),
    ),
    (
        "000000",
        (0, 0, 0),
    ),
    (
        "FFFFFF",
        (255, 255, 255),
    ),
]


def test(input, expected_output, expected_err=None):
    print("---------------------------------")
    print(f"  Inputs: '{input}'")

    try:
        result = hex_to_rgb(input)
    except Exception as e:
        print(f"Expected Error: {expected_err}")
        print(f"  Actual Error: {str(e)}")

        if str(e) != expected_err:
            print("Fail")
            return False

        print("Pass")
        return True

    print(f"Expected: {expected_output}")
    print(f"  Actual: {result}")

    if result != expected_output:
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
