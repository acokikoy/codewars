# D20120 on 2019-04-18
# You are given an array strarr of strings and an integer k. 
# Your task is to return the first longest string consisting of k
# consecutive strings taken in the array.
# Example:
# 
# longest_consec(["zone", "abigail", "theta", "form", "libe", "zas", "theta", "abigail"], 
# 2) --> "abigailtheta"
# 
# n being the length of the string array, if n = 0 or k > n or k <= 0 return "".
# Note
# 
# consecutive strings : follow one after another without an interruption
import unittest

def longest_consec(strarr, k):
    """ 配列内の文字列をk個連結した時に、最初の最長の文字列を返す
    
    Args:
        strarr (list): list of strings
        k (int): 連結数
    
    Returns:
        strings: the first longest string consisting of k
    
    """
    n = len(strarr)
    joinarr = []
    if n == 0 or k > n or k <= 0:
        return ''
    for i in range(n-k+1):
        joinarr.append(''.join(strarr[i:i+k]))
    # print('joinarr: ', joinarr)
    return max(joinarr, key=len)


def test(strq, k, stra):
    print('問題: ', strq)
    print('正解: ', stra)
    result = longest_consec(strq, k)
    if result == stra:
        print('[OK]  ', result)
    else:
        print('[NG]  ', result)
    print('='*20, '\n')


if __name__ == '__main__':
    strq = ["ejjjjmmtthh", "zxxuueeg", "aanlljrrrxx", "dqqqaaabbb", "oocccffuucccjjjkkkjyyyeehh"]
    k = 1
    stra = "oocccffuucccjjjkkkjyyyeehh"
    test(strq, k, stra)
    
    strq = ["itvayloxrp","wkppqsztdkmvcuwvereiupccauycnjutlv","vweqilsfytihvrzlaodfixoyxvyuyvgpck"]
    k = 2
    stra = "wkppqsztdkmvcuwvereiupccauycnjutlvvweqilsfytihvrzlaodfixoyxvyuyvgpck"
    test(strq, k, stra)


    strq = ["it","wkppv","ixoyx", "3452", "zzzzzzzzzzzz"]
    k = 3
    stra = "ixoyx3452zzzzzzzzzzzz"
    test(strq, k, stra)
    
    # def testing(actual, expected):
    #     Test.assert_equals(actual, expected)
    # Test.describe("longest_consec")
    # Test.it("Basic tests")
    # testing(longest_consec(["zone", "abigail", "theta", "form", "libe", "zas"], 2), "abigailtheta")
    # testing(longest_consec(["ejjjjmmtthh", "zxxuueeg", "aanlljrrrxx", "dqqqaaabbb", "oocccffuucccjjjkkkjyyyeehh"], 1), "oocccffuucccjjjkkkjyyyeehh")
    # testing(longest_consec([], 3), "")
    # testing(longest_consec(["itvayloxrp","wkppqsztdkmvcuwvereiupccauycnjutlv","vweqilsfytihvrzlaodfixoyxvyuyvgpck"], 2), "wkppqsztdkmvcuwvereiupccauycnjutlvvweqilsfytihvrzlaodfixoyxvyuyvgpck")
    # testing(longest_consec(["wlwsasphmxx","owiaxujylentrklctozmymu","wpgozvxxiu"], 2), "wlwsasphmxxowiaxujylentrklctozmymu")
    # testing(longest_consec(["zone", "abigail", "theta", "form", "libe", "zas"], -2), "")
    # testing(longest_consec(["it","wkppv","ixoyx", "3452", "zzzzzzzzzzzz"], 3), "ixoyx3452zzzzzzzzzzzz")
    # testing(longest_consec(["it","wkppv","ixoyx", "3452", "zzzzzzzzzzzz"], 15), "")
    # testing(longest_consec(["it","wkppv","ixoyx", "3452", "zzzzzzzzzzzz"], 0), "")

