from django.db import models
import datetime


# Create your models here.
class Parsing(models.Model):
    # pk PK + autoincrement not null
    ip = models.CharField(
        verbose_name='IP',
        max_length=15
    )
    browser = models.CharField(
        verbose_name='Browser',
        max_length=10,
        null=True,
        blank=True
    )
    date = models.DateTimeField(
        verbose_name="Date",
        auto_now=False,
        auto_now_add=False
    )

    def __str__(self):
        return self.ip

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
        # if brow_line != ('Safari' or 'Firefox' or 'Chrome'):
        #     brow_line == 'None'

        date_str = line.split(']')[0]
        date_n = date_str.rsplit('[')[-1]
        date_tot = date_n.split(' ')[0]
        date_obj = datetime.datetime.strptime(date_tot, '%d/%b/%Y:%H:%M:%S').strftime('%Y-%m-%d %H:%M:%S')

        parsing = Parsing(ip = ip_line, browser = brow_line, date = date_obj)
        # parsing_browser = Parsing_browser(browser = brow_line)
        # parsing_date = Parsing_date(date = date_obj)
        # parsing_string = Parsing_string(string = string_line)
        parsing.save()
        # parsing_browser.save()
        # parsing_date.save()
        # parsing_string.save()