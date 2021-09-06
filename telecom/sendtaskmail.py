from django.conf import settings
from django.core.mail import send_mail
from django.utils.html import strip_tags


def handle_task_mail(isps, task, mail_content, debug=settings.DEBUG):
    recipients = isps.to
    recipient_list = list(map(str.strip, recipients.split(';')))
    email_subject = '[是方電訊] -- Please add new BGP entry for our customer - ' + task.origin_as
    email_content = strip_tags(mail_content)

    if debug:
        print("Sending a Email to ", recipient_list)
        print("Email:\n")
        print(email_subject)
    send_mail(
        email_subject,
        email_content,
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=recipient_list,
        html_message=mail_content,
        fail_silently=False,
    )
