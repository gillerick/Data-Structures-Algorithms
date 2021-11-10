# Problem link: https://www.hackerrank.com/challenges/counting-valleys/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=warmup&h_r=next-challenge&h_v=zen
def counting_valleys(n, steps):
    altitude = valleys = 0

    for step in steps:
        altitude += 1 if step == 'U' else -1
        if altitude == 0 and step == 'U':
            valleys += 1

    return valleys


if __name__ == '__main__':
    steps = int(input().strip())
    path = input()
    result = counting_valleys(steps, path)
    print(result)
