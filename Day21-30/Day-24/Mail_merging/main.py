PLACEHOLDER = "[name]"
# Mail content
with open("./Input/Letters/starting_letter.txt") as file:
    content = file.read()

# Recipent Names
with open("./Input/Names/invited_names.txt") as name:
    content_line_by_line = name.readlines()

for item in content_line_by_line:
    new_str = content.replace(PLACEHOLDER, item.strip())
    print(f'{item.strip()}')
    with open(f'./Output/ReadyToSend/letter_for_{item.strip()}', mode = 'w') as file_w:
        file_w.write(new_str)