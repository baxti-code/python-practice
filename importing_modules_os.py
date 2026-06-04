"""
LEARNT TODAY
"""
# import os
# os.mkdir()
# os.rmdir()
# os.chdir()
# os.rename("old", "new")
# os.remove("file")
# os.getcwd()
# os.listdir()
# os.path.isfile()
# os.path.isdir()
# os.path.exists("file")
# os.path.getsize("file")
# os.path.join()
# os.path.expanduser("~")
# os.environ.get("HOME")
# os.environ.get("USER")
# os.environ.get("SHELL")
# os.environ.get("PATH")
# os.environ.get("LANG")
# print(os.getcwd())
# print(os.listdir())
# # print(os.mkdir("os_folder"))
# print(os.rmdir("os_folder"))

# print(os.getlogin())
# print(os.environ.get("HOME"))
# print(os.path.expanduser("~"))


# items = os.listdir()
# files =[]
# directories = []
# for item in items:
#     if os.path.isfile(item):
#         files.append(item)
#     elif os.path.isdir(item):
#         directories.append(item)
# print(f"Files : {files}")
# print(f"Directories: {directories}")


# items = os.listdir()

# for item in items:
#     if os.path.isfile(item):
#         size = os.path.getsize(item)
#         print(f"FILE: {item} — {size} bytes")
#     elif os.path.isdir(item):
#         print(f"DIR:  {item}")
# import os

# # Yaratish
# os.mkdir("test_folder")
# print("Yaratildi:", os.listdir())

# # O'chirish
# os.rmdir("test_folder")
# print("O'chirildi:", os.listdir())

# import os

# current = os.getcwd()
# filename = "test.txt"

# full_path = os.path.join(current, filename)
# print(full_path)
# # /Users/baxti/empty_folder/test.txt

# import os

# # avval fayl yaratamiz
# with open("old_name.txt", "w") as f:
#     f.write("Hello!")

# print("Oldin:", os.listdir())

# # nomini o'zgartirамиз
# os.rename("old_name.txt", "new_name.txt")

# print("Keyin:", os.listdir())

# import os

# for root, dirs, files in os.walk("."):
#     print(f"📁 {root}")
#     for file in files:
#         print(f"   📄 {file}")

# import os
# print([x for x in os.walk(".")])

# import os

# for root, dirs, files in os.walk("."):
#     # venv va .git ni o'tkazib yuborish
#     dirs[:] = [d for d in dirs if d not in ("venv", ".git")]
#     print(f"📁 {root}")
#     for file in files:
#         print(f"   📄 {file}")

# import os
# print(os.path.exists("app.py"))

# for key, value in os.environ.items():
#     print(f"{key}: {value}")

# print(os.environ.get("HOME"))