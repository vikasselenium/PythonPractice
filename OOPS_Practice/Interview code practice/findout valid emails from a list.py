import re

# List of emails as a single string inside a list
emails = ["  John.Doe@example.com, JANE_doe@EXAMPLE.com  ,admin@company.org,invalid-email@, @missinguser.com"]

# Convert list to string and remove spaces
email_str = emails[0].replace(" ", "")
#email_str=email_str.replace(",","")
#print(email_str)

s_emails=email_str.split(",")
print(s_emails)

for email in s_emails:
      email_words=email.split('@')
      if len(email_words[0]) > 0 and len(email_words[1]) > 0:
          # print("part1:", email_words[0])
          # print("part2", email_words[1])
          print("Valid email ",email)
      











# # Find all matches
# matches = re.findall(pattern, email_str)
#
# # Print the matched emails
# print("Matched emails:")
# print(matches)
#