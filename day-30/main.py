# file not found

# try:
#     file = open("a_file.txt")
#     a_dict = {"key": "value"}
#     print(a_dict["key"])
# except FileNotFoundError:
#     file = open("a_file.txt", "w")
#     file.write("sth")
# except KeyError as error_message:
#     print(f"The key {error_message} does not exist")
# else:
#     content = file.read()
#     print(content)
# finally:
#     raise TypeError("I made it up")

height = float(input("Height: "))
weight = int(input("Weight: "))

if height > 3:
    raise ValueError("Height should not be over 3 meters.")

bmi = weight / height ** 2
print(bmi)
