import re

phone_num_regex = re.compile(r"(\d{3})-\d{3}-\d{4}")

mo = phone_num_regex.search("My phone number is 816-613-2449")

print("Phone number found: " + mo.group())
print(mo.group(1))