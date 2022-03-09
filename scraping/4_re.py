import re

# 네자리 문자, abcd, desk, book
# ca?e -> care, cave, case, cafe
# caae, cabe, cace, cade, ...

p = re.compile("ca.e")
# . (ca.e): 하나의 문자를 의미 > care, cafe, case caffe
# ^ (^de): 문자열의 시작
# $ (se$): 문자열의 끝


def print_match(m):
    if m:
        print("m.group():", m.group())
        print("m.string", m.string)
        print("m.start(", m.start())
        print("m.end():", m.end())
        print("m.span", m.span())

    else:
        print("매칭되지 않음")


m = p.match("careless")
print_match(m)

# -> 주어진 문자열의 처음부터 일치하는지 확인


m = p.search("good care")
print_match(m)

# -> 주어진 문자열 중에 일치하는게 있는지 확인

lst = p.findall("good care cafe")
print(lst)

# -> 일치하는 모든 것을 리스트 형태로 반환
