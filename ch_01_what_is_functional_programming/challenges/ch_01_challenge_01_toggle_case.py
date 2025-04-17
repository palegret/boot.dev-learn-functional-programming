def toggle_case(line):
    if line.istitle():
        return f"{line.upper()}!!!"
    elif line.isupper():
        return line.lower().capitalize().replace("!", "")
    elif len(line) > 0 and line[1:].islower():
        return line.title()
    else:
        return line


# Test cases


test_cases = [
    (
        "live long and prosper",
        "Live Long And Prosper",
    ),
    (
        "...Khan",
        "...KHAN!!!",
    ),
    (
        "BEAM ME UP, BOOTS!", 
        "Beam me up, boots"
    ),
    (
        "",
        "",
    ),
    (
        "I aM a DoCtOr, nOt A fUnCtIoNaL pRoGrAmMeR!!",
        "I aM a DoCtOr, nOt A fUnCtIoNaL pRoGrAmMeR!!",
    ),
    (
        "TO BOLDLY GO WHERE NO BEAR HAS GONE BEFORE!!!!",
        "To boldly go where no bear has gone before",
    ),
    (
        "Illogical",
        "ILLOGICAL!!!",
    ),
]


def test(input, expected_output):
    print("---------------------------------")
    print(f"   Input: {input}")
    print(f"Expected: {expected_output}")

    result = toggle_case(input)

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
