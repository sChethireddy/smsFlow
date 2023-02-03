'''
Created on 17-Oct-2022

@author: saipr
'''

import random
import string


class Email:
    
    @staticmethod
    def gen_random_string(length):
        return ''.join(
            random.choices(
                string.ascii_lowercase + string.digits,
                k=length
        )
    )