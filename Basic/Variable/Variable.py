x = 3       # 변수 x에 정수 3을 저장 합니다.
x = "문장"  # 변수 x에 문자열을 저장 합니다.

print(x)    # 변수 x를 출력 합니다.

"""
유효한 변수 이릉 
"""
myHomeAddress = "서울시 송파구 ...."
my_home_address = "서울시 송파구 ...."
_myHomeAddress = "서울시 송파구 ...."

# 여러 변수에 대한 많은 값 할당 
post, address,  price = "130-330", "서울시 송파구... ", 100000
print(post)
print(address)
print(price)

# 여러 변수에 대한 하나의 값
x = y = z = 0
print(x)
print(y)
print(z)


"""
변수에 데이터를 할때 특정 자료형으로 Casting
"""
x = str(10)
x = int(10)
x = float(10)
