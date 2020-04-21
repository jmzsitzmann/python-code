
def mySqrt(x, guess):
    nextguess = 0.5 * (x/guess + guess)
   
    while abs(nextguess - guess) > .1:
        guess = nextguess
        nextguess = 0.5 * (x/guess + guess)
    return nextguess
    
print(mySqrt(212.0, 17.0))