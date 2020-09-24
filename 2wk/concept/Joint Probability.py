import itertools as iter
import fractions as frac

# Joint Probability - 검은 돌 3개와 하얀 돌 5개가 들어있는 주머니가 있다. 검은 돌을 먼저 뽑고, 하얀 돌을 나중에 뽑을 확률은? 

# 바둑돌을 담고있는 주머니를 chain을 통해 결합해 생성하고 List로 변환
pocket = iter.chain(['B', 'B', 'B'], ['W', 'W', 'W', 'W', 'W'])
pocket_list = list(pocket)

# Case 1 - 뺀 돌을 다시 넣지 않는 경우

# 중복을 포함한 모든 경우의 수를 가져옴
case1_comb = list(iter.combinations(pocket_list, 2))

# 가져온 리스트에서 검은 돌을 먼저 뽑고, 하얀 돌을 그 뒤에 뽑은 갯수를 가져옴
case1_num = 0
for i in case1_comb:
    if i == ('B', 'W'):
        case1_num += 1

# Fraction을 이용해 값 출력
case1_fraction = frac.Fraction(case1_num, len(pocket_list) * (len(pocket_list) - 1))
print('Case 1 :', case1_fraction)

# Case 2 - 뺀 돌을 다시 넣을 경우
case2_comb = list(iter.combinations_with_replacement(pocket_list, 2))

# 가져온 리스트에서 검은 돌을 먼저 뽑고, 하얀 돌을 그 뒤에 뽑은 갯수를 가져옴
case2_num = 0
for i in case2_comb:
    if i == ('B', 'W'):
        case2_num += 1

# Fraction을 이용해 값 출력
case2_fraction = frac.Fraction(case1_num, len(pocket_list) ** 2)
print('Case 2 :', case2_fraction)