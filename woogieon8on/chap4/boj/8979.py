N, K = map(int, input().split())

medals = []
for i in range(N):
  medals.append(list(map(int, input().split()))) # 국가-메달 리스트 입력받기

medals.sort() # 국가 순서로 정렬

kCountry, kGold, kSilver, kBronze = medals[K-1] # K번째 국가 메달 리스트
rank = 1

for country, gold, silver, bronze in medals :
  if country == K :
    continue
  # K번째 국가보다 잘한 국가 발견하면 등수 + 1
  if gold > kGold or gold == kGold and silver > kSilver or gold == kGold and silver == kSilver and bronze > kBronze :
    rank += 1

print(rank)