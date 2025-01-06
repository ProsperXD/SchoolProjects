text = """
This is test to check emails blabla wait is this how you do this module? im confused


...

test@email.com

...

tw@example.com

...
"""

sample_emails = ['test@email.com', 'tw@example.com']

email_list = []

words = text.split()

for word in words:
    if '@' in word:
        email = word.strip(".,?!:;")
        email_list.append(email)

unique_emails = list(set(email_list))

print("Unique Email Addresses:")
for email in unique_emails:
    print(email)

input_email = input("Enter an email address to check: ")

if input_email in unique_emails:
    print(f"{input_email} is in the list of unique email addresses.")
else:
    print(f"{input_email} is not in the list of unique email addresses.")
