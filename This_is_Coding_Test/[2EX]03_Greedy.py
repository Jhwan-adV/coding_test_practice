# 1번 - 모험가 길드
# 공포도가 X 이상인 모험가는 X명 이상으로 구성된 그룹에 참여할 때, 여행을 떠날 수 있는 그룹 수의 최댓값

# 풀이 - 정렬 후 값이 큰 순서대로 원소를 제거해 나감
def max_parties(n=10):
    import random
    members = [random.randint(1,n/3) for i in range(n)] # 테스트를 위해 랜덤 범위 제한
    members.sort()
    count = 0 # 그룹 갯수

    while len(members) != 0:
        max_fear = members[-1] # 공포 수치가 Slicing 인덱스 역할 수행
        print(members, count)

        if len(members) >= max_fear:
            members = members[:-max_fear]
            count += 1
        else:
            break

    return count


print(max_parties(30))


# 2번 - 곱하기 혹은 더하기
# 주어진 수 문자열에서 곱하기와 더하기로 만들 수 있는 가장 큰 수 구하기
# 풀이 - 0을 만났을 떄 처리 방법에 따라!