# D20122on2019-04-20
# Simple Encryption #1 - Alternating Split
# https://www.codewars.com/kata/57814d79a56c88e3e0000786/train/python

def decrypt(encrypted_text, n):
    """ decrypting the encrypted string.  
    
    Args:
        encrypted_text (str): 暗号化文字列
        n (int): 繰り返し処理回数
    
    Returns:
        decrypted text (str)  
    """
    if n <= 0:
        return encrypted_text

    if encrypted_text:
        q, mod = divmod(len(encrypted_text), 2)
        for i in range(n):
            text = ''
            strodd = encrypted_text[q:]
            streven = encrypted_text[0:q]
            for so, se in zip(strodd, streven):
                text += so + se

            if mod: #奇数の時は最後の一文字が余る
                text += strodd[-1]
            encrypted_text = text
    
    return encrypted_text

def encrypt(text, n):
    """ building the encrypted string.  
    
    Args:
        text (str): 元の文字列
        n (int): 繰り返し処理回数
    
    Returns:
        encrypted text (str)   
    """
    if n <= 0:
        return text

    if text:
        for i in range(n):
            text = text[1::2] + text[0::2]

    return text