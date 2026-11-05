# Do your coding here

# Segment 1

# Segment 2

# Segment 3

# Segment 4
#the reason why scores,points&digits flagged/warned because its name the same as inputs
#but ig it's fine ,cuz it just serves as placeholders,doesn't interfere with the code
#also need to wait for LAYERS[] , scores[] ,points and digit
#before this  can work so ye
#the functions:trust scores,average, points , combinations

def calculate_trust_score(scores):
    trust = 0
    for i in range(len(scores)):
        multiply=scores[i]*LAYERS[i][1]
        trust+=multiply
    return round(trust,1)

def calculate_simple_average(scores):
    return round(sum(scores)/len(scores),1)

def make_bar(points):
    num_blocks=points//10
    leftover_blocks=points%10
    bar=num_blocks*'#'
    if leftover_blocks>=5:
        bar+='+'
    return bar

def pin_combinations(digits):
    return 10**digits

#CALCULATION OUTPUT
print(f"TOTAL SCORES : {calculate_trust_score(scores)}")
print(f"TOTAL AVERAGE : {calculate_simple_average(scores)}")
print(f"POINTS (1 '#' equals 10 points) : {make_bar(points)}")
print(f"POSSIBLE COMBINATIONS : {pin_combinations(digits)}")
# Segment 5

# Segment 6
