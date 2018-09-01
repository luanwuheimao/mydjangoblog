import os
from django.core.mail import send_mail

os.environ['DJANGO_SETTINGS_MODULE'] = 'myblog.settings'

if __name__ == '__main__':

    print("test")
    result = send_mail(
            '来自long的测试邮件',
            '欢迎访问',
            '3212610989@qq.com',
            ['807832316@qq.com'],
            fail_silently=False
        )
    print(result)
