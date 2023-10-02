"""List of prime numbers generator."""

def primes(number_of_primes):
    if (number_of_primes <= 0) :
        raise ValueError
    list = [2] # this list will grow as we generate more primes in ascending order
    j = 2 # we will use this to generate the primes as we increase j
    # so long as the length of the list of the primes is less than the required number of primes
    while (len(list) < number_of_primes):
        # for every prime currently in the list
        for prime in list:
            # if the number is divisible by any prime in our list, we do not want it
            if j%prime==0:
                break
        else:
            # otherwise this number is not divisible by any of the primes in the list and so it itself must be prime
            list.append(j)
        j += 1 # increment j
    return list