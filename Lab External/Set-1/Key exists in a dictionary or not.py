my_dict = {
    "name": "John",
    "age": 30,
    "city": "New York"
}
key = input("Enter the key to check: ")
if key in my_dict:
    print("Key exists in the dictionary.")
else:
    print("Key does not exist in the dictionary.")
