def stylize_title(document):
    return add_border(center_title(document))


def center_title(document):
    width = 40
    title = document.split("\n")[0]
    centered_title = title.center(width)
    return document.replace(title, centered_title)


def add_border(document):
    title = document.split("\n")[0]
    border = "*" * len(title)
    return document.replace(title, title + "\n" + border)


# Tests


test_cases = [
    (
        """The Importance of FP
Learn how functional programming can change the way you think about code.
Benefits include immutability, simplicity, and composability.""",
        """          The Importance of FP          
****************************************
Learn how functional programming can change the way you think about code.
Benefits include immutability, simplicity, and composability.""",
    ),
    (
        """Short Title
Equally short story""",
        """              Short Title               \n****************************************
Equally short story""",
    ),
    (
        """DocToDoc: A Guide
Understanding the art of document conversion.
We write cool functional code to make it happen.""",
        """           DocToDoc: A Guide            
****************************************
Understanding the art of document conversion.
We write cool functional code to make it happen.""",
    ),
]


def test(input1, expected_output):
    print("---------------------------------")
    print(f"Inputs:")
    print(f" * document: {input1}\n")
    print(f"Expecting:\n{expected_output}\n")

    result = stylize_title(input1)

    print(f"Actual:\n{result}\n")

    if result == expected_output:
        print("Pass")
        return True

    print("Fail")

    return False


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
