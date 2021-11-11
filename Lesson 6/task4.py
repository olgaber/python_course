"""Жду от вас письмо! (слайды 15-19). Воспользуйтесь менеджером контекста
(with … as) (слайд 19)
** Добавьте тему письма, используя модуль email"""

import smtplib
from email.message import EmailMessage

msg = EmailMessage()
msg.set_content('I did it!')

msg['Subject'] = 'Subject'
msg['From'] = "olga.berv@gmail.com"
msg['To'] = "olga.berv@gmail.com"

# Send the message via SMTP server.
with (smtplib.SMTP_SSL('smtp.gmail.com', 465)) as server:
    server.login("olga.berv@gmail.com", "*********")
    server.send_message(msg)
    server.quit()

