from fractions import gcd

# parse string expression of form '1/2+1/2' to nums and dens
def parseInput(exp):
    fractions = exp.split('+')
    frac1 = fractions[0].split('/')
    num1 = frac1[0]
    den1 = frac1[1]
    frac2 = fractions[1].split('/')
    num2 = frac2[0]
    den2 = frac2[1]
    
    return int(num1), int(den1), int(num2), int(den2)

# reduce a fraction to it's simplest form
def reduceFrac(num3, den3):
    # do not reduce fractions equal to 1
    if num3 == den3:
        return num3, den3
    
    commonFactor = gcd(num3, den3)
    reducedNum = num3 / commonFactor
    reducedDen = den3 / commonFactor
    return reducedNum, reducedDen

def reducedFractionSums(expressions):
    reducedFracs = []
    # loop through every provided expression
    for exp in expressions:
        # get nums and dens
        num1, den1, num2, den2, = parseInput(exp)
        
        # calculate least common multiple to be new den using formula:
        # lcm = a * b / gcd(a, b)
        den3 = (den1 * den2) / gcd(den1, den2)
        
        # perform fraction addition with new den
        num3 = (num1 * (den3 / den1)) + (num2 * (den3 / den2))
        
        # reduce final fraction and add to list
        reducedNum, reducedDen = reduceFrac(num3, den3)
        reducedFracs.append(str(reducedNum) + '/' + str(reducedDen))
    return reducedFracs
