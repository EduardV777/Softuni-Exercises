snowballs = int(input())
output = ""
highestValue = 0

while snowballs:
    weight = int(input())
    timeToHit = int(input())
    quality = int(input())
#each snowball's value is calculated by the following formula- (snowball_weight / snowball_time) ** snowball_quality
    val = (weight / timeToHit) ** quality

    if val > highestValue:
        highestValue = int(val)
        output = f"{weight} : {timeToHit} = {highestValue} ({quality})"

    snowballs -= 1

print(output)