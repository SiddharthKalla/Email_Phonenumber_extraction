import re, pyperclip

#create regex for phone number(for numbers like: 415-324-9999)
phoneregex = re.compile(r'''
(
((\d\d\d)|(\(\d\d\d\d\)))?   #area code(optional)
(\s|-)                       #first seperator
\d\d\d                       #first 3 digits
-                            #seperator
\d\d\d\d                     #last 4 digits
(((ext(\.)?\s|x)             #extension word-part(opyional)
 (\d{2,5})))?                #extension number-part
)
''',re.VERBOSE)

# create a regex for email addresses(for addresses like: xyz@xyz.xyz)
emailregex = re.compile(r'''
[a-zA-Z0-9_.+]+     #name part
@                   # @ symbol
[a-zA-Z0-9_.+]+     #domain name part

''',re.VERBOSE)

# get the text off the clipboard
text = pyperclip.paste()

#extract the emails and phone numbers from the text
extractedphone = phoneregex.findall(text)
extractedemail = emailregex.findall(text)

allphonenumber = []
for phonenumber in extractedphone:
    allphonenumber.append(phonenumber[0])

#copy all the extracted emails/phone numbers to the clipboard
results = '\n'.join(allphonenumber) + '\n' + '\n'.join(extractedemail)
pyperclip.copy(results)
