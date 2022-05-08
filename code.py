import itertools
def solve2():
    letters = ('t','w','o','f','u','r')
    digits = range(10)
    for perm in itertools.permutations(digits, len(letters)):
        sol = dict(zip(letters, perm))
        if sol['t'] == 0:
            continue
        two =  100 * sol['t'] + 10 * sol['w'] + sol['o']
        two1 =  100 * sol['t'] + 10 * sol['w'] + sol['o']
        four =  1000 * sol['f'] + 100 * sol['o'] + 10 * sol['u'] + sol['r']
        if two+two1==four:
          print("two+two=four")
          return two,two1,four
print(solve2())
