

# # 구현 1-1). 상하좌우 - L, R, U, D 조합이 주어졌을 떄 목적지를 구하시오
# def get_destination(m=12, array=['L', 'L', 'R', 'R', 'D', 'D', 'R', 'U']):
#     x, y = [1, 1]
#     for a in array:
#         if a == 'L' and x != 1:
#             x -= 1
#         elif a == 'R' and x != m:
#             x += 1
#         elif a == 'U' and y != 1:
#             y -= 1
#         elif a == 'D' and y != m:
#             y += 1
#
#     return x, y
#
#
# print(get_destination())
#
#
# # 구현 1-2). 시각
# def get_threes(hour=2):
#     count = 0
#     for i in range(hour):
#         for j in range(60): # minute
#             for k in range(60): # second
#                 if '3' in str(i) + str(j) + str(k):
#                     count += 1
#     return count
#
#
# print(get_threes())
#
#
# # 구현 2. 왕실의 나이트 - 나이트의 위치가 주어졌을 때 움직일 수 있는 위치 구하기
# def available_positions(x=1, y=2):
#     moves = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (-1, 2), (1, -2), (-1, -2)]
#     candidates = [(x+i, y+j) for i, j in moves if (x+i > 0) and (y+j > 0)]
#
#     return len(candidates)
#
#
# print(available_positions())

# 구현 3. 게임 개발
n, m = 3, 5
d = [[0] * m for _ in range(n)]
print(d)
