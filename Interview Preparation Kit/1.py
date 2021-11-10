# There is a large pile of socks that must be paired by color. Given an array of integers representing the color of
# each sock, determine how many pairs of socks with matching colors there are.
# Link: https://www.hackerrank.com/challenges/sock-merchant/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=warmup

def sockMerchant(n, ar):
    count = 0
    array_set = set(ar)
    for i in array_set:
        count += ar.count(i)//2
    return count


if __name__ == '__main__':
    n = int(input().strip())

    ar = list(map(int, input().rstrip().split()))
    print(sockMerchant(n, ar))
