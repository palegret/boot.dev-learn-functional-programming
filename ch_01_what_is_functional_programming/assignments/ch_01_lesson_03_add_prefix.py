def add_prefix(document, documents):
    prefix = f"{len(documents)}. "
    new_doc = prefix + document
    documents = documents + (new_doc,)
    return documents


# Tests


test_cases = [
    (
        ("hello there", "sonny", "how ya doing"),
        ("0. hello there", "1. sonny", "2. how ya doing"),
    ),
    (
        ("go", "python", "java", "javascript"),
        ("0. go", "1. python", "2. java", "3. javascript"),
    ),
    (
        ("boots", "everyone else"),
        ("0. boots", "1. everyone else"),
    ),
]


def test(input1, expected_output):
    print("---------------------------------")
    print(f"Inputs:")
    print(f" * documents: {input1}")
    print(f"Expecting: {expected_output}")

    try:
        documents = ()
        for doc in input1:
            documents = add_prefix(doc, documents)
    except Exception as e:
        documents = f"Error: {e}"

    print(f"Actual: {documents}")

    if documents == expected_output:
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
