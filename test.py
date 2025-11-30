TEST = [{"a": "1"}, {"b": "2"}, {"c": "3"}]


def testWhile():
    index = 0

    while index < len(TEST):
        current_item = TEST[index]
        expected_value = list(current_item.values())[0]
        expected_keys = list(current_item.keys())[0]

        print(f"CURRENT_ITEM ::=> {current_item}")
        print(f"CURRENT_VALUE ::=> {expected_value}")
        print(f"CURRENT_KEYS ::=> {expected_keys}")

        correctNb = input("Give me the correct number: ")

        if correctNb == expected_value:
            print("\nCorrect!")
            index += 1
        else:
            print("Not correct!")

    print("All correct!")


testWhile()
