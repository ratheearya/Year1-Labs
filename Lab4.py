def simple_lock(x1, x2, x3, y1, y2, y3):
    count = 0
    if(abs(x1 - y1) <= 4):
        count += abs(x1-y1)
    elif(abs(x1 - y1) > 4):
        count += (9 - (abs(x1-y1)))
    if(abs(x2 - y2) <= 4):
        count += abs(x2-y2)
    elif(abs(x2 - y2) > 4):
        count += (9 - (abs(x2-y2)))
    if(abs(x3 - y3) <= 4):
        count += abs(x3-y3)
    elif(abs(x3 - y3) > 4):
        count += (9 - (abs(x3-y3)))
    return count

def combo_lock(current, unlock):
    count = 0
    current_string = str(current)
    unlock_string = str(unlock)
    for i in range(len(current_string)):
        count += simple_lock(int(current_string[i]),1,1,int(unlock_string[i]),1,1)
    return count

def is_prime(x):
    i = 1
    counter = 0
    if(x <= 0):
        return False
    while (i != x+1):
        if (x % i == 0):
            counter += 1
        i += 1
    if(counter == 2):
        return True
    else:
        return False
    return False


def next_prime(n):
    n += 1
    while (not is_prime(n)):
        n+= 1
    return n

def is_perfect(n):
    count = 1
    total = 0
    if(n <= 0):
        return False
    else:
        while(count != n):
            if(n % count == 0):
                total += count
            count += 1
    if(n == total):
        return True
    else:
        return False


def next_perfect(n):
    n += 1
    while(is_perfect(n) == False):
        n += 1
    return n

def is_power(number, base):
    base1 = base
    while (number >= base1):
        if(number == base1):
            return True
        else:
            base1 = base1 * base
    return False

def gcd(a, b):
    if (b == 0):
        return a
    return gcd(b, a % b)


def coprime(x, y):
    if(gcd(x,y) == 1):
        return True
    else:
        return False
    return False


def phi(n):
    count = 0
    for i in range (n):
        if (coprime(i,n)):
            count += 1
    return count


def sqrt( a,  x,  epsilon):
    while(float(abs(x - a / x)) >= epsilon):
        x = (x + a / x) / 2
    return x


if __name__ == "__main__":
    print("simple_lock(1,1,1,2,3,2):", simple_lock(1,1,1,2,3,2))
    print("combo_lock(1151, 7122):", combo_lock(1151, 7122))
    print("is_prime(37):", is_prime(7))
    print("next_prime(37):", next_prime(37))
    print("is_perfect(28):", is_perfect(28))
    print("next_perfect(37):", next_perfect(37))
    print("is_power(1024, 2):", is_power(1024, 2))
    print("gcd(12, 8):", gcd(12, 8))
    print("coprime(12, 7):", coprime(12, 7))
    print("phi(17):", phi(17))
    print("sqrt(3, 1, 0.0000001):", sqrt(3, 1, 0.0000001))
