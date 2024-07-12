# -------------------------------------------------------------
# 클래스(Class)
# -객체지향언어 (OOP)에서 데이터를 정의하는 자료형
# - 데이터를 정의할 수 있는 데이터가 가진 속성과 기능을 명시
# - 구성요소 : 속성/attribute/field + 기능/method
# -------------------------------------------------------------
# 클래스정의 : 햄버거를 나타내는 클래스
# 클래스이름 : 버거
# 클레스속성 : 번, 패티, 야채 , 종류
# 클래스기능 : 햄버거 설명 기능
# -------------------------------------------------------------

class Bugger:

    kind ='맥도날드'
    
    # 힙 영역에 객체 생성 시 속성값 저장 기능
    def __init__(self,bread,patty,veg):
        self.bread = bread
        self.patty = patty
        self.veg = veg
        #self.kind = kind

    # 기능 즉 메서드
    def printInfo(self):
        print(f'빵 종 류  : {self.bread}')
        print(f'패    티  : {self.patty}')
        print(f'야    채  : {self.veg}')
        print(f'브 랜 드  : {self.kind}')

## 객체 생성 ---------------------------------------------------
# 불고기 버거 객체 생성
bugger1 = Bugger('브리오슈','불고기','양상추 양파 토마토')

# 치즈 버거 객체 생성
bugger2 = Bugger('참깨빵','순쇠고기','치즈 양상추 양파 토마토')

## 버거 정보 확인
bugger1.printInfo()
print()
bugger2.printInfo()
