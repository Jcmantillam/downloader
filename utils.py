# coding:utf-8
from functools import wraps
import time
 
# 20 páginas
urls = [
    'https://wj-platform.s3-us-west-2.amazonaws.com/posts/CYMnD6YOjtm/1.jpg',
    'https://wj-platform.s3-us-west-2.amazonaws.com/posts/CYLyXZXgBQK/1.jpg',
    'https://wj-platform.s3-us-west-2.amazonaws.com/posts/CYLN2dUD7Ra/1.jpg',
    'https://wj-platform.s3-us-west-2.amazonaws.com/posts/CYLNszytvY_/1.jpg',
    'https://wj-platform.s3-us-west-2.amazonaws.com/posts/CYLNqTGKCT5/1.jpg',
    'https://wj-platform.s3-us-west-2.amazonaws.com/posts/CYLNjWgK66y/1.jpg',
    'https://wj-platform.s3-us-west-2.amazonaws.com/posts/CYLNYwlM3oi/1.jpg',
    'https://wj-platform.s3-us-west-2.amazonaws.com/posts/CYLNQ5MocR5/1.jpg',
    'https://wj-platform.s3-us-west-2.amazonaws.com/posts/CYLNLAHMgyY/1.jpg',
    'https://wj-platform.s3-us-west-2.amazonaws.com/posts/CYLM_82oQvw/1.jpg',
    'https://wj-platform.s3-us-west-2.amazonaws.com/posts/CYLM45fI0Q-/1.jpg',
    'https://wj-platform.s3-us-west-2.amazonaws.com/posts/CYLM11do6ZZ/1.jpg',
    'https://wj-platform.s3-us-west-2.amazonaws.com/posts/CYLMpjWvmwd/1.jpg',
    'https://wj-platform.s3-us-west-2.amazonaws.com/posts/CYMhzJ-O-ux/1.jpg',
    'https://wj-platform.s3-us-west-2.amazonaws.com/posts/CYMnD6YOjtm/1.jpg',
    'https://wj-platform.s3-us-west-2.amazonaws.com/posts/CYLPJ-kMFe1/1.jpg',
    'https://wj-platform.s3-us-west-2.amazonaws.com/posts/CYMehU-F2tK/1.jpg',
    'https://wj-platform.s3-us-west-2.amazonaws.com/posts/CYNZhAPMl72/1.jpg',
    'https://wj-platform.s3-us-west-2.amazonaws.com/posts/CYM0fXZJB9U/1.jpg',
    'https://wj-platform.s3-us-west-2.amazonaws.com/posts/CYM1Inxq0ct/1.jpg',
    'https://wj-platform.s3-us-west-2.amazonaws.com/posts/CYMgnETKpZt/1.jpg',
    'https://wj-platform.s3-us-west-2.amazonaws.com/posts/CYLhLuWolxW/1.jpg',
    'https://wj-platform.s3-us-west-2.amazonaws.com/posts/CYMpMHBpfZy/1.jpg',
    'https://wj-platform.s3-us-west-2.amazonaws.com/posts/CYMehU-F2tK/1.jpg',
    'https://wj-platform.s3-us-west-2.amazonaws.com/posts/CYMRg_kKmUt/1.jpg',
    'https://wj-platform.s3-us-west-2.amazonaws.com/posts/CYLPJ-kMFe1/1.jpg',
    'https://wj-platform.s3-us-west-2.amazonaws.com/posts/CYMUuR6Nmp_/1.jpg',
    'https://wj-platform.s3-us-west-2.amazonaws.com/posts/CYMJYDDLcQC/1.jpg',
    'https://wj-platform.s3-us-west-2.amazonaws.com/posts/CYMDms6tiKN/1.jpg',
    'https://wj-platform.s3-us-west-2.amazonaws.com/posts/CYNI5Zyu5LK/1.jpg',
    'https://wj-platform.s3-us-west-2.amazonaws.com/posts/CYMSzm3rlvG/1.jpg',
    'https://wj-platform.s3-us-west-2.amazonaws.com/posts/CYLO4X4M0su/1.jpg',
    'https://wj-platform.s3-us-west-2.amazonaws.com/posts/CYMCvCYrRi5/1.jpg',
    'https://wj-platform.s3-us-west-2.amazonaws.com/posts/CYL1-3HLe7x/1.jpg',
    'https://wj-platform.s3-us-west-2.amazonaws.com/posts/CYMnD6YOjtm/1.jpg',
    'https://wj-platform.s3-us-west-2.amazonaws.com/posts/CYMehU-F2tK/1.jpg',
    'https://wj-platform.s3-us-west-2.amazonaws.com/posts/CYMYH3VJUQm/1.jpg',
    'https://wj-platform.s3-us-west-2.amazonaws.com/posts/CYNKTCvFN9d/1.jpg',
    'https://wj-platform.s3-us-west-2.amazonaws.com/posts/CYNKPGNlQBg/1.jpg',
    'https://wj-platform.s3-us-west-2.amazonaws.com/posts/CYNKLeqli2i/1.jpg',
    'https://wj-platform.s3-us-west-2.amazonaws.com/posts/CYMROmjgQ-H/1.jpg',
    'https://wj-platform.s3-us-west-2.amazonaws.com/posts/CYMe_iful8C/1.jpg',
    'https://wj-platform.s3-us-west-2.amazonaws.com/posts/CYMivSTrxby/1.jpg',
    'https://wj-platform.s3-us-west-2.amazonaws.com/posts/CYNYSpLB0aJ/1.jpg',
    'https://wj-platform.s3-us-west-2.amazonaws.com/posts/CYMNPe_IGMH/1.jpg',
    'https://wj-platform.s3-us-west-2.amazonaws.com/posts/CYLO2TKsOC2/1.jpg',
    'https://wj-platform.s3-us-west-2.amazonaws.com/posts/CYMt6E1PhCM/1.jpg',
    'https://wj-platform.s3-us-west-2.amazonaws.com/posts/CYMz-3pp3Cv/1.jpg',
    'https://wj-platform.s3-us-west-2.amazonaws.com/posts/CYLPHpUum0T/1.jpg',
    'https://wj-platform.s3-us-west-2.amazonaws.com/posts/CYM9jc8pNIQ/1.jpg',
    'https://wj-platform.s3-us-west-2.amazonaws.com/posts/CYNG922JKmq/1.jpg',
    'https://wj-platform.s3-us-west-2.amazonaws.com/posts/CYNAcK1JKya/1.jpg',
    'https://wj-platform.s3-us-west-2.amazonaws.com/posts/CYMUaFeLdgH/1.jpg',
    'https://wj-platform.s3-us-west-2.amazonaws.com/posts/CYMNlkoLOp7/1.jpg',
    'https://wj-platform.s3-us-west-2.amazonaws.com/posts/CYMjc4Ur8Gc/1.jpg',
    'https://wj-platform.s3-us-west-2.amazonaws.com/posts/CYMUjKFrsJt/1.jpg',
    'https://wj-platform.s3-us-west-2.amazonaws.com/posts/CYM9jc8pNIQ/1.jpg',
    'https://wj-platform.s3-us-west-2.amazonaws.com/posts/CYMt6E1PhCM/1.jpg',
    'https://wj-platform.s3-us-west-2.amazonaws.com/posts/CYLzY22rsgy/1.jpg',
    'https://wj-platform.s3-us-west-2.amazonaws.com/posts/CYLtZ_Or075/1.jpg',
    'https://wj-platform.s3-us-west-2.amazonaws.com/posts/CYMSzm3rlvG/1.jpg',
    'https://wj-platform.s3-us-west-2.amazonaws.com/posts/CYLO4X4M0su/1.jpg',
    'https://wj-platform.s3-us-west-2.amazonaws.com/posts/CYNjqnuM6KL/1.jpg',
    'https://wj-platform.s3-us-west-2.amazonaws.com/posts/CYNjo3fsKye/1.jpg',
    'https://wj-platform.s3-us-west-2.amazonaws.com/posts/CYNN4YNhyeB/1.jpg',
    'https://wj-platform.s3-us-west-2.amazonaws.com/posts/CYNNeLvsDd2/1.jpg',
    'https://wj-platform.s3-us-west-2.amazonaws.com/posts/CYNNEIzMsfN/1.jpg',
    'https://wj-platform.s3-us-west-2.amazonaws.com/posts/CYMmhbGJfCL/1.jpg',
    'https://wj-platform.s3-us-west-2.amazonaws.com/posts/CYNFSJVtQZd/1.jpg',
    'https://wj-platform.s3-us-west-2.amazonaws.com/posts/CYL8mGCMOTv/1.jpg',
    'https://wj-platform.s3-us-west-2.amazonaws.com/posts/CYLN2dUD7Ra/1.jpg',
    'https://wj-platform.s3-us-west-2.amazonaws.com/posts/CYLNszytvY_/1.jpg',
    'https://wj-platform.s3-us-west-2.amazonaws.com/posts/CYLNqTGKCT5/1.jpg',
    'https://wj-platform.s3-us-west-2.amazonaws.com/posts/CYLNjWgK66y/1.jpg',
    'https://wj-platform.s3-us-west-2.amazonaws.com/posts/CYLNYwlM3oi/1.jpg',
    'https://wj-platform.s3-us-west-2.amazonaws.com/posts/CYLNQ5MocR5/1.jpg',
    'https://wj-platform.s3-us-west-2.amazonaws.com/posts/CYLNLAHMgyY/1.jpg',
    'https://wj-platform.s3-us-west-2.amazonaws.com/posts/CYLM_82oQvw/1.jpg',
    'https://wj-platform.s3-us-west-2.amazonaws.com/posts/CYLM45fI0Q-/1.jpg',
    'https://wj-platform.s3-us-west-2.amazonaws.com/posts/CYLM11do6ZZ/1.jpg',
    'https://wj-platform.s3-us-west-2.amazonaws.com/posts/CYLMpjWvmwd/1.jpg',
    'https://wj-platform.s3-us-west-2.amazonaws.com/posts/CYNPCc6uLu2/1.jpg',
    'https://wj-platform.s3-us-west-2.amazonaws.com/posts/CYM1g12ObBg/1.jpg',
    'https://wj-platform.s3-us-west-2.amazonaws.com/posts/CYMn-Lmu4-v/1.jpg',
    'https://wj-platform.s3-us-west-2.amazonaws.com/posts/CYMdyfKOPJi/1.jpg',
    'https://wj-platform.s3-us-west-2.amazonaws.com/posts/CYNV2xAlx90/1.jpg',
    'https://wj-platform.s3-us-west-2.amazonaws.com/posts/CYNBSwCNo7d/1.jpg',
    'https://wj-platform.s3-us-west-2.amazonaws.com/posts/CYM6ewkJIeY/1.jpg',
    'https://wj-platform.s3-us-west-2.amazonaws.com/posts/CYMsxDgLFAT/1.jpg',
    'https://wj-platform.s3-us-west-2.amazonaws.com/posts/CYMfAq6sNgj/1.jpg',
    'https://wj-platform.s3-us-west-2.amazonaws.com/posts/CYMRR-IvTp-/1.jpg',
    'https://wj-platform.s3-us-west-2.amazonaws.com/posts/CYL10BSJfto/1.jpg',
    'https://wj-platform.s3-us-west-2.amazonaws.com/posts/CYLMhdZse61/1.jpg',
    'https://wj-platform.s3-us-west-2.amazonaws.com/posts/CYNC-rFhHhn/1.jpg',
    'https://wj-platform.s3-us-west-2.amazonaws.com/posts/CYMuj5fBVK1/1.jpg',
    'https://wj-platform.s3-us-west-2.amazonaws.com/posts/CYMYU_8qKR6/1.jpg',
    'https://wj-platform.s3-us-west-2.amazonaws.com/posts/CYMDo59ql2E/1.jpg',
    'https://wj-platform.s3-us-west-2.amazonaws.com/posts/CYLpg4Kqrst/1.jpg',
    'https://wj-platform.s3-us-west-2.amazonaws.com/posts/CYMe72rN7Cp/1.jpg',
    'https://wj-platform.s3-us-west-2.amazonaws.com/posts/CYLoANqsCZd/1.jpg',
]

 
def fn_timer(function):
    '''
         Decorador de sincronización de funciones
         : función param: objeto función
         : retorno: decorador
    '''
    @wraps(function)
    def function_timer(*args,**kwargs):
        t0 = time.time()
        result = function(*args,**kwargs) 
        t1 = time.time()
        print ('[finished function:{func_name} in {time:.2f}s]'.format(func_name = function.__name__,time = t1 - t0))
        return result
    return function_timer
 
 # Prueba
@fn_timer
def add(x,y):
    time.sleep(1.22)
    return x + y
 
if __name__ == '__main__':
    sum = add(1,2)
    print (sum)
