'''
알고리즘 유형별 기출문제 11장 그리디 - 2.곱하기 혹은 더하기
난이도: 하, 풀이시간: 30분, 시간제한: 1초, 메모리제한: 128MB  기출: Facebook 인터뷰

문제설명
각 자리가 숫자 0부터 9로만 이루어진 문자열 S
왼쪽부터 오른쪽으로 하나씩 모든 숫자를 확인하면 숫자사이에 X혹은 + 연산자를 넣어
만들어질 수 있는 가장 큰 수를 구하는 프로그램
모든 연산은 왼쪽에서 부터 순서대로 이루어진다.

입력조건: 첫째 줄에 여러개의 숫자로 구성된 하나의 문자열 S (1<=S의 길이<=20)

출력조건: 첫째 줄에 만들어질 수 있는 가장 큰 수를 출력

문제 풀이 아이디어
보통은 X가 더 숫자를 크게 만드는데
작아지거나 차이가 없는경우가 있다. → 0 혹은 1 일때만 예외로 + 처리를 해준다.
2 이상이면 곱하기를해준다.
'''
s = input() # 문자열로 입력 받음
result = int(s[0]) # 계산 결과, 슬라이싱, int()로 형 변환을 해줌

for i in range(1, len(s)): # 한 글자씩 확인
    num = int(s[i])
    if num <= 1 or result <= 1: # result와 숫자가 모두 1이하일 때
        result += num
    else:
        result *= num

print(result)