# -*- coding: utf-8 -*-
"""
Created on Thu Mar 12 19:52:30 2020

@author: Dick
"""

class CellPhone(object):
    """
    price: int
    camera_count: int
    screen_size: float
    """   
    
    def __init__(self, price, camera_count, screen_size):
        self.price = price
        self.camera_count = camera_count
        self.screen_size = screen_size
    
    @classmethod
    def special_feature(cls):
        pass
    
class GooglePhone(CellPhone):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
    def special_feature(cls, num_list, reverse=True):
        """
        num_list : a list only contains int
        reverse: if True, sort returned list in descending order and vice versa
        Return a list only contains elements in num_list which is bigger than 10 and even
        """
        _sorted_list = [_element for _element in num_list if _element % 2 ==0 and _element > 10]
        _sorted_list.sort(reverse=reverse)
        return _sorted_list
    
class TaiwanPhone(CellPhone):
    from functools import lru_cache
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
    @classmethod
    @lru_cache()    
    def fibonacci(cls, num):
        """
        num: int
        Return fibonacci result
        eg. fibonacci(4)=3, fibonacci(5)=5, fibonacci(6)=8
        ref: https://zh.wikipedia.org/wiki/%E6%96%90%E6%B3%A2%E9%82%A3%E5%A5%91%E6%95%B0%E5%88%97
        """
        if num < 2:
            return num
        return cls.fibonacci(num-2) + cls.fibonacci(num-1)
    
    @classmethod
    def fetch_digits(cls, num):
        """
        num: int
        return a list contains digits of input num
        eg. fetch_digits(302) will return [2, 0, 3]
        """
        _list = list() 
        i = 0
        while num:
            i = num % 10
            num = num // 10
            _list.append(i)
        return _list
    
    @classmethod
    @lru_cache()     
    def factorial(cls, n):
        """
        n: int
        return factorial of n
        eg. factorial(6) will return 6!, which is 
        """
        if n == 1 or n == 0:
            return 1
        else:
            return n * cls.factorial(n-1)
    
    @lru_cache()
    def special_feature(cls, num):
        """
        num: int
        Return result use fibonacci's return values and computes its permutation        
        eg. 取fibonacci最後二位(十位為 x、個位為 y)數字進行 p x 取 y (排序組合) 計算
        exception
            1. fibonacci 不足10位數
            2. y > x
        """
        _fibonacci = cls.fibonacci(num)
        _digit_list = cls.fetch_digits(_fibonacci)
        if len(_digit_list) < 2:
            raise ValueError("因為需要取十位數與個位數計算排列數值, 輸入的fibonacci項數請至少大於7")
        elif _digit_list[0] > _digit_list[1]:
            raise ValueError("fibonacci項數計算結果, 個位數: {} 大於十位數: {}, 不符合組合從n個元素中取出k個元素, k(十位數)必須大於等於n(個位數)".format(_digit_list[0],
                                                                                                 _digit_list[1]))
        else:
            _result = (cls.factorial(_digit_list[1]) / cls.factorial(_digit_list[1] - _digit_list[0]))
        return _result