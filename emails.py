import re
a=int(input('enter the no of emails should be validated:',))
emails=[]
validemails=[]
for i in range(a):
    email=input('enter the email:')
    emails.append(email)
for email in emails:
    m=re.fullmatch('\w[a-zA-Z0-9_.]*@domain[.]com',email)
    if m!=None:
        validemails.append(email)
print(validemails)

