# 문자열 변수에 할당
name = "홍길동"
print(name)

# 여러 줄에 문자열 표시 
story = """심청은 가난한 봉사 심학규의 딸로 태어나서 일찍 어머니를 여의고, 
 눈먼 아버지의 보살핌으로 자란 뒤에 아버지를 지성으로 모셨다."""

print(story)
print(story[0])

#문장안에 큰 따옴표 작은 따옴표 사용 하기
story = """홀길동이 말했다. "아버님 전 이만 더나겠습니다." """
story1 = "홀길동이 말했다. \"아버님 전 이만 더나겠습니다.\""
print(story)
print(story1)

#문자열은 배열 입니다.
story = """홍길동이 말했다. "아버님 전 이만 더나겠습니다.\""""
print(story[0])             # 첫번재 문자  : 홍
print(story[len(story)-1])  # 마지막 문자  : "


fruit = "사과는 과일입니다."
print(fruit[:2])            # 처음 부터 특정 위치 까지 : 사과
print(fruit[4:])            # 특정 위치 부터 끝까지 : 과일입니다.
print(fruit[4:6])           # 특정 범위  : 과일
print(fruit[-4:-2])         # - 사용한 특정 범위 : 입니

strA = "나의 이릉은"
strB = "홍길동"
strC = strA + strB          # 문자열 합치기
print(strC)                 # 결과 : 나의 이릉은홍길동
print("=" * 30)             # = 문자 30개 표시
strC = strA + " " + strB    # 문자열 합치면서 중간에 공백 넣기
print(strC)                 # 결과 : 나의 이릉은 홍길동
strC = "저" + strA[1:] + " " +  strB
print(strC)                 # 결과 : 저의 이릉은 홍길동

today = "오늘은 {}년 {}월 {}일 입니다."
todayStr = today.format(2022, 12, 24)
print(todayStr)             # 오늘은 2022년 12월 24일 입니다.

today = "오늘은 {1}년 {2}월 {3}일 사과 금액은 {0}입니다."
todayStr = today.format(30000, 2022, 12, 24)
print(todayStr)             # 오늘은 2022년 12월 24일 사과 금액은 30000입니다.



yyyyStr = "오늘은 %d년 입니다." %2022  # 한개 사용
print(yyyyStr)                        # 결과 : 오늘은 2022년 입니다.
todayStr = "오늘은 %d년 %d월 %d일 입니다." %(2022,12,12)    # 여러개 사용
print(todayStr)                       # 결과 : 오늘은 2022년 12월 12일 입니다.
todayStr = "오늘은 습도는 %d%%" %20    # %% 사용 하여 표시
print(todayStr)                       # 결과 : 오늘은 습도는 %20

# 앞에 공백 주기
todayStr = "오늘은 습도는 %10d%%" %20  # %와 포맷코드 사이에 10 공백 ( 왼쪽 )
print(todayStr)                       # 경과 : 오늘은 습도는         20%

# 뒤에 공백 주기
todayStr = "오늘은 습도는 %-10d%%" %20 # %와 포맷코드 사이에 10 공백 ( 오른쪽 )
print(todayStr)                       # 경과 : 오늘은 습도는         20%

# 소수점 주기
todayStr = "오늘은 습도는 %.2f%%" %20 # %와 포맷코드 사이에 값.소수점자리수
print(todayStr)                       # 경과 : 오늘은 습도는 20.00%



asciiCode01 = ord('a')
print(asciiCode01)

str = "a"
print(type(str))
strToBytes = str.encode()    # 문자열을 Byte로 변환 
print(type(strToBytes))
print(strToBytes)
asciiCode02 = ord(strToBytes)
print(asciiCode02)

print("===================")
str = "안녕"
strToBytes = str.encode(encoding="utf-8")    # 문자열을 Byte로 변환 
print(strToBytes)
aa = strToBytes.decode()
print(aa)


print("*" * 30)
# 앞에 공백 주기
today = "오늘은 {1:>10}년 {2}월 {3}일 사과 금액은 {0}입니다." # :>10 10칸 앞에 공백
todayStr = today.format(30000, 2022, 12, 24)
print(todayStr)  # 오늘은       2022년 12월 24일 사과 금액은 30000입니다.

# 뒤에 공백 주기
today = "오늘은 {1:<10}년 {2}월 {3}일 사과 금액은 {0}입니다." # :<10 10칸 앞에 공백
todayStr = today.format(30000, 2022, 12, 24)
print(todayStr)  # 오늘은 2022      년 12월 24일 사과 금액은 30000입니다.

# 중간에 문자 표시
today = "오늘은 {1:^10}년 {2}월 {3}일 사과 금액은 {0}입니다." # :^10 칸 중간에 표시
todayStr = today.format(30000, 2022, 12, 24)
print(todayStr)  # 오늘은    2022   년 12월 24일 사과 금액은 30000입니다.

# 공백에 다른 문자 표시
today = "오늘은 {1:!^10}년 {2}월 {3}일 사과 금액은 {0}입니다." # :!^10 공백에 ! 표시
todayStr = today.format(30000, 2022, 12, 24)
print(todayStr)  # 오늘은 !!!2022!!!년 12월 24일 사과 금액은 30000입니다

# { } 표시
today = "오늘은 {{{1}}}년 {2}월 {3}일 사과 금액은 {0}입니다." # {{ }} 로 표사
todayStr = today.format(30000, 2022, 12, 24)
print(todayStr)  # 오늘은 !!!2022!!!년 12월 24일 사과 금액은 30000입니다