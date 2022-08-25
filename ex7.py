# Rewrite the grade program from the previous chapter using a function called computegrade that takes
# a  score as a parameter and returns a grade as a string 


def computegrade(score):
    try:
        if float(score) >= 1.0:
            return 'Bad score'
        elif float(score) >= 0.9:
            return 'A'
        elif float(score) >= 0.8:
            return 'B'
        elif float(score) >= 0.7:
            return 'C'
        elif float(score) >= 0.6:
            return 'D'
        elif float(score) < 0.6:
            return 'F'
    except:
        return 'Bad score'
    

score = input('Enter score: ')
print(computegrade(score))
