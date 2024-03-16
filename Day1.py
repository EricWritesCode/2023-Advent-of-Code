import re


def main():
    with open("Day1-Data.txt", "r") as file:
        data = file.readlines()

    final_total: int = 0
    line_count: int = 0

    for item in data:
        line_count += 1
        # Find all number characters in the line
        line_nums: list[str] = re.findall(r"\d", item)
        # Grab first and last numbers found (the same if only one number exists)
        line_total: int = int(line_nums[0] + line_nums[len(line_nums) - 1])

        final_total += line_total

        # Debug
        print(f"[{line_count}] {item}: {line_nums} Total: {line_total}")
        print(f"New total: {final_total}")

    print(f"Final total: {final_total}")


main()
