import smtplib
from email.message import EmailMessage
import pathlib
from string import Template

#creates an email object from EmailMessage class instance
email = EmailMessage()
email['from'] = 'SenderEmail@YourMailDomain.domain'      #Enter the email account from which you wish to send the emails (ex: abc@gmail.com)
email['to'] = 'ReceiverEmail@domain.com'
email['subject'] = 'Enter Subject here/ or use an f-string'

template_html = Template(pathlib.Path('page.html').read_text())     #pick up an html page to use a template for the email. (optional)

email.set_content(template_html.substitute({'name' : 'Jatin Hooda'}),'html')     #customise the email

#2nd param specifies that it is an html doc. without it, it'll send the html code
#the dictionary used here can aslo be substituted by name = ''. a loop for multiple entries too.

with smtplib.SMTP(host='smtp.mail.com',port=587) as mh:
	mh.ehlo()
	mh.starttls()
	mh.login('SenderEmail@gmail.com','password')      #your email creds here
	mh.send_message(email)
	print('done')
