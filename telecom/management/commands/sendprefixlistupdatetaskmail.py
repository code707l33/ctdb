from django.conf import settings
from django.core.mail import send_mail
from django.core.management.base import BaseCommand

from telecom.models import PrefixListUpdateTask


class Command(BaseCommand):
    help = 'Commands of send prefixlistupdatetask Email.'

    def handle(self, *args, **options):
        prefixlistupdatetask = PrefixListUpdateTask.objects.get(id=id)
        self.handle_mail(prefixlistupdatetask)

    # TODO:如何取得寄件資料(mail addr.)，不再同一個表格內
    def handle_mail(self, prefixlistupdatetask, debug=settings.DEBUG):
        seperator = ';'
        recipients = prefixlistupdatetask.recipients[:-1] if prefixlistupdatetask.recipients[-1:] == seperator else prefixlistupdatetask.recipients
        recipient_list = list(map(str.strip, recipients.split(';')))
        if debug:
            print("Sending a Email to ", recipient_list)
            print("Email:\n")
            print(prefixlistupdatetask.email_subject)
            print(prefixlistupdatetask.email_content)
        send_mail(
            subject=prefixlistupdatetask.email_subject,
            message=prefixlistupdatetask.email_content,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=recipient_list,
            fail_silently=False,
        )
