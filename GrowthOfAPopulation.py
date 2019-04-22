# Growth of a Population
# https://www.codewars.com/kata/563b662a59afc2b5120000c6/
def nb_year(p0, percent, aug, p):
    pn = p0
    year = 0
    while pn < p:
        year += 1
        pn = pn *(1+percent/100) + aug
    
    return year
    
print(nb_year(1500, 5, 100, 5000))
