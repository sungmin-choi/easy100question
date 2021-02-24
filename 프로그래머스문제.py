# 메뉴 리뉴얼

from collections import Counter
from itertools import combinations
orders = ["XYZ", "XWY", "WXA"]
course = [2, 3, 4]


# def solution(orders, course):
#     answer = []
#     for k in course:
#         candidates = []
#         for menu_li in orders:
#             for li in combinations(menu_li, k):
#                 res = ''.join(sorted(li))
#                 candidates.append(res)
#         sorted_candidates = Counter(candidates).most_common()
#         answer += [menu for menu, cnt in sorted_candidates if cnt >
#                    1 and cnt == sorted_candidates[0][1]]
#     return sorted(answer)

def solution(orders, course):
    answer = []
    for c in course:
        array2 = []
        array3 = []
        array4 = []
        for order in orders:
            for li in combinations(order, c):
                li = list(li)
                li.sort()
                res = "".join(li)
                array2.append(res)
        for menu in array2:
            count = 0
            if menu not in array3:
                array3.append(menu)
                count = array2.count(menu)
                array4.append((count, menu))
        array4.sort(key=lambda x: -x[0])
        print(array4)
        if array4:
            maxcount = array4[0][0]
        for i in range(len(array4)):
            if maxcount >= 2 and maxcount == array4[i][0]:
                answer.append(array4[i][1])
            else:
                break

    answer.sort()
    return answer


print(solution(orders, course))
