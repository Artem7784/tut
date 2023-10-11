# def geometric_progression(a, r):
#     while True:
#         yield a
#         a *= r
#
# a = 1
# r = 3
#
# gp_generator = geometric_progression(a, r)
#
# for i in range(9):
#     print(next(gp_generator))


# import pdb
#
# def geometric_progression(a, r):
#     while True:
#         yield a
#         a *= r
#
# a = 1
# r = 2
#
# gp_generator = geometric_progression(a, r)
#
# pdb.set_trace()
#
# for _ in range(5):
#     print(next(gp_generator))


import re

def is_valid_email(email):

    email_pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'

    if re.match(email_pattern, email):
        return True
    else:
        return False

email1 = "example@e_mail.com"

print(is_valid_email(email1))