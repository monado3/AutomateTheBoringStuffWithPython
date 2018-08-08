import re
from typing import List

text: str = '''Contact Us

No Starch Press, Inc.
245 8th Street
San Francisco, CA 94103 USA
Phone: 800.420.7240 or +1 415.863.9900 (9 a.m. to 5 p.m., M-F, PST)
Fax: +1 415.863.9950

Reach Us by Email

General inquiries: info@nostarch.com
Media requests: media@nostarch.com
Academic requests: academic@nostarch.com (Please see this page for academic review requests)
Help with your order: info@nostarch.com
Reach Us on Social Media
Twitter
Facebook'''

phoneRegex = re.compile(r'''(
(\d{3}|\(\d{3}\))?             #市外局番
(\s|-|\.)?                     #区切り
(\d{3})                        #数字3桁
(\s|-|\.)?                     #区切り
(\d{4})
(\s*(ext|x|ext.)\s*(\d{2,5}))? #内線番号
)''', re.VERBOSE)

emailRegex = re.compile(r'''(
[a-zA-Z0-9._%+-]+ #username
@
[a-zA-Z0-9.-]+    #domain name
(\.[a-zA-Z]{2,4}) #dot-something
)''', re.VERBOSE)

matches: List[str] = []
for groups in phoneRegex.findall(text):
    phoneNum = '-'.join([groups[1], groups[3], groups[5]])
    if groups[8] != '':
        phoneNum += ' x' + groups[8]
    matches.append(phoneNum)
for groups in emailRegex.findall(text):
    matches.append(groups[0])

if len(matches) > 0:
    print('\n'.join(matches))
else:
    print('No phone numbers or email addresses found.')
