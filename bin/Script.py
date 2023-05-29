import os

folder_path = os.getcwd()

files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f)) and '.' not in f]

for file_name in files:
    file_path = os.path.join(folder_path, file_name)

    with open(file_path, 'rb') as file:
        content = bytearray(file.read())

    if content[0xDC] == 0x0D:
        content[0xDC] = 0x05
        print(f"Modified {file_name}: Quest to PCVR conversion complete")
    elif content[0xDC] == 0x05:
        content[0xDC] = 0x0D
        print(f"Modified {file_name}: PCVR to Quest conversion complete")

    with open(file_path, 'wb') as file:
        file.write(content)

input("\nConversion process complete. Press Enter to exit.")
