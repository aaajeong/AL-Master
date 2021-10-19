'''
6장 정렬 실전문제4 - 두 배열의 원소 교체
난이도: 하, 풀이시간: 20분, 시간제한: 2초, 메모리제한: 128MB 기출: 국제 알고리즘 대회

문제설명
N개의 원소로 구성된 0두개의 배열 A,B가 있다. 배열의 원소는 모두 자연수이다.
최대 K번의 바꿔치기 연산을 수행할 수 있는데, 바꿔치기 연산이란 배열 A에 있는 원소 하나와 배열 B에 있는 원소 하나를 골라서 두 원소를 서로 바꾸는 것을 말한다.
최종 목표는 배열 A의 모든 원소의 합이 최대가 되도록 하는 것이다.
N,K 배열 A,B의 정보가 주어졌을 때, 최대 k번의 바꿔치기 연산을 수행하여 만들 수 있는 배열 A의 모든 원소의 합의 최댓값을 출력하는 프로그램을 작성하시오.

입력조건
첫번 째 줄에 N과 K가 공백으로 구분되어 입력된다.(1<=N<=100000, 0<=K<=N )
두번 째 줄에 배열 A의 원소들이 공백으로 구분되어서 입력된다. 모든 원소는 10,000,000보다 작은 자연수이다.
세번 째 줄에 배열 B의 원소들이 공백으로 구분되어서 입력된다. 모든 원소는 10,000,000보다 작은 자연수이다.

출력조건
최대 K번 바꿔치기 연산을 수행하여 만들 수 있는 배열의 모든 원소의 합의 최댓값을 출력한다.

문제 풀이 아이디어
A는 오름차순, B는 내림차순으로 정렬
원소들을 k번 비교하는데, B의 원소가 A의 원소보다 크면 교체
작거나 같으면 종료
A의 원소들을 모두 합한 값을 출력
'''
#이 문제에서는 두 배열의 원소가 최대 100,000개까지 입력될 수 있으므로 O(NlogN)을 보장하는 정렬 알고리즘을 이용해야한다.

n, k = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))

a.sort() # 오름차순 정렬
b.sort(reverse=True) # 내림차순 정렬

for i in range(k):
    if a[i] < b[i]:
        a[i], b[i] = b[i], a[i]
    else:
        break

print(sum(a))

# 5 3
# 1 2 5 4 3
# 5 5 6 6 5
# 26