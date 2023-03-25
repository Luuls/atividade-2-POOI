# https://www.beecrowd.com.br/judge/pt/problems/view/2408

scores = list(map(int, input().split()))

scores.remove(max(scores))
scores.remove(min(scores))

print(scores[0])
