# -*- coding: utf-8 -*-
# @Author: chenbin
# @Date:   2018-06-06 11:21:58
# @Last Modified by:   chenbin
# @Last Modified time: 2018-06-08 18:05:13
from frontauth.configs import PASSWORD_SALT
import hashlib

def make_password(password,salt=None):
	if password is None:
		return None
	if not salt:
		salt = PASSWORD_SALT
	password = str(password)
	md5 = hashlib.md5()
	temp = salt + password
	md5.update(temp.encode('utf-8'))
	return md5.hexdigest()


# def make_password(password, salt=None, hasher='default'):
#     """
#     Turn a plain-text password into a hash for database storage

#     Same as encode() but generates a new random salt.
#     If password is None then a concatenation of
#     UNUSABLE_PASSWORD_PREFIX and a random string will be returned
#     which disallows logins. Additional random string reduces chances
#     of gaining access to staff or superuser accounts.
#     See ticket #20079 for more info.
#     """
#     if password is None:
#         return UNUSABLE_PASSWORD_PREFIX + get_random_string(UNUSABLE_PASSWORD_SUFFIX_LENGTH)
#     hasher = get_hasher(hasher)

#     if not salt:
#         salt = hasher.salt()

#     return hasher.encode(password, salt)