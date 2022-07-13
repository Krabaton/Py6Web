from abc import abstractmethod, ABC


class Notification(ABC):

    @abstractmethod
    def notify(self, message):
        ...


class Contact:
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone


class Email(Notification):
    def __init__(self, email):
        self.email = email

    def notify(self, message):
        print(f'Send {message} to {self.email}')


class SMS(Notification):
    def __init__(self, phone):
        self.phone = phone

    def notify(self, message):
        print(f'Send {message} to {self.phone}')


class NotificationService:
    def __init__(self, notification: Email | SMS):
        self.notification = notification

    def send(self, message):
        self.notification.notify(message)


if __name__ == '__main__':
    contact = Contact('Andrij', 'adnrij@gmail.com', '+380501234567')

    notification_email = Email(contact.email)
    notification_sms = SMS(contact.phone)

    notification_service = NotificationService(notification_sms)
    notification_service.send('Hello bro!')
