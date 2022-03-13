asciiCode = ord("a")    # 문자 a를 ASCII CODE로 변환 
print(asciiCode)        # 변수 asciiCode 값 표시 : 97

char = chr(97)          # ASCII CODE 97을 문자로 변환 하여 char 변수에 저장
print(char)             # char 표시 : a

# hex로 변환 하기 
hexValue = hex(ord('a'))
print(chr(int(hexValue,16)))
print(type(hexValue))         # 0x61
#  byteArray = bytearray.fromhex(hexValue)
#  hexToStr = byteArray.decode()
#  print(hexToStr)         # 0x61
