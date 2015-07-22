import smtplib

smtpUser = 'my email'
smtpPass = 'my password'

toAdd = 'recipient email'
fromAdd = smtpUser

subject = 'subject line'
header = 'To: ' + toAdd + '\n' + fromAdd + '\n' + 'Subject: ' + subject
body = 'message'

print header + '\n' + body

s = smtplib.SMTP('smtp.gmail.com',587)

s.ehlo()
s.starttls()
s.ehlo()

s.login(smtpUser, smtpPass)
s.sendmail(fromAdd, toAdd, header + '\n\n' + body)

s.quit()
