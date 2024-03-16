import re


def main():
    with open("Day1-Data.txt", "r") as file:
        data: list[str] = file.readlines()

    final_total: int = 0
    line_count: int = 0

    # Build a list of valid numbers to search for
    valid_numbers: list[str] = [str(num) for num in range(1, 10)] + [
        "one",
        "two",
        "three",
        "four",
        "five",
        "six",
        "seven",
        "eight",
        "nine",
    ]
    # Dict for converting from words to numerals
    conversion_list: dict[str, str] = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
    }

    for item in data:
        line_count += 1
        line_set = set()
        final_values: list = []

        for num in valid_numbers:
            # Check line for number
            index = item.find(num)
            if index != -1:
                line_set.add(f"{index}|{num}")
            # Check in reverse
            rindex = item.rfind(num)
            if rindex != -1:
                line_set.add(f"{rindex}|{num}")

        # Break up the set into index/value pairs and convert word numbers to ints
        for entry in line_set:
            i_v_pair = str(entry).split("|")
            if i_v_pair[1] in conversion_list:
                i_v_pair[1] = str(conversion_list.get(i_v_pair[1]))
            int_index = int(i_v_pair[0])
            final_values.append([int_index, i_v_pair[1]])

        # Sort final values by index
        final_values = sorted(final_values)

        first: str = final_values[0][1]
        last: str = final_values[len(final_values) - 1][1]

        row_value = first + last
        final_total += int(row_value)

        print(f"[{line_count}] {item}: {line_set} ({final_values}) Row: {row_value}")
        print(f"New total: {final_total}")

    print(f"Final total: {final_total}")


main()
