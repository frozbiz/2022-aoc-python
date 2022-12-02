
from pathlib import Path

day1_dir = Path(__file__).resolve().parent

file_path = day1_dir / "1-input.txt"

largest_so_far = []
num_elves = 0

def insert_ordered(ordered_list, value, max_position):
    ix = min(len(ordered_list), max_position)
    while ix > 0 and value > ordered_list[ix-1]:
        ix -= 1
    if ix < 3:
        ordered_list.insert(ix, value)


with file_path.open() as file:
    current_elf_total = 0
    for line in file:
        line = line.strip()
        if len(line) == 0 and current_elf_total > 0:
            num_elves += 1
            insert_ordered(largest_so_far, current_elf_total, 3)
            current_elf_total = 0
        else:
            value = int(line)
            current_elf_total += value

    # Handle the case where the file doesn't end in an empty line
    if current_elf_total > 0:
        num_elves += 1
        insert_ordered(largest_so_far, current_elf_total, 3)


top_three = largest_so_far[:3]
print(f"{top_three}, {sum(top_three)}")
print(f"{num_elves} elves, list_len:{len(largest_so_far)}")
