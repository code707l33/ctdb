from django.conf import settings
from django.core.mail import send_mail
from django.utils.html import strip_tags


def handle_task_mail(isp, task, mail_content, debug=settings.DEBUG):
    seperator = ';'
    recipients = isp.to[:-1] if isp.to[-1:] == seperator else isp.to
    recipient_list = list(map(str.strip, recipients.split(';')))

    recipients_cc = isp.cc[:-1] if isp.cc[-1:] == seperator else isp.cc
    recipient_cc_list = list(map(str.strip, recipients_cc.split(';')))

    recipients_bcc = isp.bcc[:-1] if isp.bcc[-1:] == seperator else isp.bcc
    recipient_bcc_list = list(map(str.strip, recipients_bcc.split(';')))

    if task.eng_mail_type:
        email_subject = '[CHIEF TELECOM] -- Please add new BGP entry for our customer - ' + task.origin_as
    else:
        email_subject = '[是方電訊] -- Please add new BGP entry for our customer - ' + task.origin_as
    email_content = strip_tags(mail_content)

    if debug:
        print("Sending a Email to ", recipient_list)
        print("Sending a Email cc to ", recipient_cc_list)
        print("Email:")
        print(email_subject)
    send_mail(
        email_subject,
        email_content,
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=recipient_list,
        bcc=recipient_bcc_list,
        cc=recipient_cc_list,
        html_message=mail_content,
        fail_silently=False,
    )
