import smtplib

port = 1025


def send_email(sender, receiver, message):
    with smtplib.SMTP('localhost', port) as server:
        server.sendmail(sender, receiver, message)


# python -m smtpd -c DebuggingServer -n localhost:1025
if __name__ == '__main__':
    send_email('test@test.com', 'test@api.com', 'Test message')
