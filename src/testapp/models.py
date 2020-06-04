from django.db import models
import datetime


# Create your models here.
class Parsing_ip(models.Model):
    # pk PK + autoincrement not null
    ip = models.CharField(
        verbose_name='IP',
        max_length=15
    )

    def __str__(self):
        return self.ip

class Parsing_browser(models.Model):
    browser = models.CharField(
        verbose_name='Browser',
        max_length=10,
        null=True,
        blank=True
    )

    def __str__(self):
        return self.browser

class Parsing_date(models.Model):
    date = models.DateTimeField(
        verbose_name="Date",
        auto_now=False,
        auto_now_add=False
    )

    def __str__(self):
        return str(self.date)

# class Parsing_string(models.Model):
    # string = models.TextField(
    #     verbose_name='String',
    #     null=True,
    #     blank=True
    # )
    
    # def __str__(self):
    #     return self.string

with open('Apache_log.txt', 'r') as fp:
    line = fp.readline()
    for line in fp:
        string_line = line

        ip_line = line.split(" ")[0]

        select = line.rsplit(' ')[-1]
        brow_line = select.split('/')[0]

        date_str = line.split(']')[0]
        date_n = date_str.rsplit('[')[-1]
        date_tot = date_n.split(' ')[0]
        date_obj = datetime.datetime.strptime(date_tot, '%d/%b/%Y:%H:%M:%S').strftime('%Y-%m-%d %H:%M:%S')

        parsing_ip = Parsing_ip(ip = ip_line)
        parsing_browser = Parsing_browser(browser = brow_line)
        parsing_date = Parsing_date(date = date_obj)
        # parsing_string = Parsing_string(string = string_line)
        parsing_ip.save()
        parsing_browser.save()
        parsing_date.save()
        # parsing_string.save()