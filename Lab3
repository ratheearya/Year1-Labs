
def pointInRect (x, y, rx, ry, rw, rh):
    if x >= rx and x < rx+rw and y<= ry and y>ry-rh:
        return True
    else:
        return False

#Test the top left and bottom right points to get the entire triangle. No need to rewrite since we already have a function to test points
def rectInRect(x1, y1, w1, h1, x2, y2, w2, h2):
    if pointInRect(x1,y1,x2,y2,w2,h2) and pointInRect(x1+w1,y1-h1,x2,y2,w2,h2): 
        return True
    else:
        return False

# Make sure at least one of the points touches the rectangle, so use or and reuse function again
def overlap(x1, y1, w1, h1, x2, y2, w2, h2):
    if pointInRect(x1,y1,x2,y2,w2,h2) or pointInRect(x1+w1,y1-h1,x2,y2,w2,h2) or pointInRect(x1+w1,y1,x2,y2,w2,h2) or pointInRect(x1,y1-h1,x2,y2,w2,h2):
        return True
    else:
        return False

# Code is correct, but can use in[] to make code more concise
def canDonateBlood(donor, recipient):
    if recipient == "A":
        if donor == "A" or donor == "O":
            return True
        else:
             return False
    elif recipient == "B":
        if donor == "B" or donor == "O":
            return True
        else:
             return False
    elif recipient == "AB":
        if donor == "A" or donor == "B" or donor == "AB" or donor == "O":
            return True
        else:
             return False
    elif recipient == "O":
        if donor == "O":
            return True
        else:
            return False
    else:
        print ("Invalid bloodtype")
def wages(hours, rate):
    if hours <= 40:
        return hours * rate
    elif hours > 40:
        return (rate * 40) + (1.5 * rate * (hours - 40))
def leap(year):
    if(year % 4 == 0):
        if(year % 100 != 0):
            return True
        elif(year % 400 == 0):
                return True
        else:
            return False
    else:
         return False
def daysInMonth(month, year):
    if(month == 2):
        if(leap(year)):
            return 29
        else:
            return 28
    else:
        if month in [4,6,9,11]:
            return 30
        else:
            return 31

if __name__ == "__main__":

    print ("Testing ground")
