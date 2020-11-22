
def enviar_email():
    server =smtplib.SMT(smtp.gmail.com,587)
    server.ehlo()
    server.starttls()

    server.login("mariela.bidondo.ds@immune.institute","Immune2021")
    subject = "Ha bajado el precio"
    body = "Ya compralo!"
    msg= f"Subject:":{subject}\n\n{body}"

    server.enviar_mail("mgbidondo@gmail.com", msg)

