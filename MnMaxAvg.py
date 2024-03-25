"""MinMaxAvg"""
def mnmxavg(scores):
    """OhGod"""
    if not scores:
        return None
    mx_score = scores[0]
    mn_score = scores[0]
    total_score = 0
    for score in scores:
        if score > mx_score:
            mx_score = score
        if score < mn_score:
            mn_score = score
        total_score += score
    avg_score = round(total_score / len(scores), 2)
    return (round(mx_score, 2), round(mn_score, 2), avg_score)
import json
my_list = json.loads(input())
result = mnmxavg(my_list)
print(result)
