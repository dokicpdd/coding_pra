def unique(e_list):
    result=set()
    for email in e_list:
        final_email=get_format(email)
        result.add(final_email)
    return len(result)

def get_format(email):
    i=email.index('@')
    pre=email[0:i]
    last=email[i:]
    pre=pre.replace('.','')
    if '+'in pre:
        j=pre.index('+')
        pre=pre[0:j]
    return pre+last

l=['test.email+alex@leetcode.com',
'test.e.mail+bob.cathy@leetcode.com',
'testemail+david@lee.tcode.com']
print(unique(l))
