#Panoramix's Prediction
#Brute force solution
#Given and n and m number, we need to know if m is the next prime number
#There will be a counter adding 1 by 1 to n until it gets the next prime number
#if the m number is equal to the next prime it will be printed YES else NO

def solution(n,m):
    while n != m:
        n+=1
        #if its prime and is the m number
        if is_prime(n) and n == m:
            return 'YES'
        elif is_prime(n):
            return 'NO' 
    return 'NO'
           
def is_prime(n):
    counter = 0
    #knowing if a number is prime by counting factors
    for number in range(1, n+1):
        if n % number == 0:
            counter+=1
    if counter == 2:
        return True
    return False
            
def main():
    n , m = input().split()
    print(solution(int(n),int(m)))

if __name__ == "__main__":
    main()