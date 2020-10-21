# if wolf item in list is at index -1, return pls go away
# else return sheep warning
# figure out which number wolf is and return warning to the sheep next to it.

def warn_the_sheep(queue):


    if "wolf" in queue[-1]:
        return "Pls go away and stop eating my sheep"
    else:
        n = queue.index("wolf")
        print(n)
    
        a = list(range(1, len(queue)))
        print(a)
        flipped = a[::-1]

        
        return "Oi! Sheep number " + str(flipped[n]) + "! You are about to be eaten by a wolf!"

# [sheep, sheep, sheep, sheep, sheep, wolf, sheep, sheep]      (YOU ARE HERE AT THE FRONT OF THE QUEUE)
#    7      6      5      4      3      2      21      10

['sheep', 'sheep', 'sheep', 'sheep', 'sheep', 'wolf', 'sheep', 'sheep']
['sheep', 'sheep', 'wolf', 'sheep', 'sheep', 'sheep', 'sheep', 'sheep'] 

