num = 10
string = "안녕"

# 변수 Type 출력 하기

print(type(num))    # <class 'int'>
print(type(string))    # <class 'str'>


# 객체의 타입에 따라서 실행문 실행 하기
def getType(obj):
    rnValue = ""
    if isinstance(obj, int) :
        rnValue = "정수"
    elif isinstance(obj, str):
        rnValue = "문자열"
    elif isinstance(obj, float):
        rnValue = "실수"
    return rnValue

string = "안녕"
print(getType(string))  # 문자열

# is 사용
def getTypeIs(obj):
    typeVar = type(obj);
    if typeVar is int :
        return  "정수"
    elif typeVar is str:
        return "문자열"
    elif typeVar is float:
        return"실수"
    else:
        return "정의되지 않은 자료형"

typeVar = 10
print(getTypeIs(typeVar))  # 정수
typeVar = "안녕"
print(getTypeIs(typeVar))  # 문자열
typeVar = ['a', 'b']
print(getTypeIs(typeVar))  # 정의되지 않은 자료형