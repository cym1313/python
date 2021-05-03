import pickle
# 이름과 전화번호를 입력받아서 반환한다.

def get_contact():
    name =input("이름: ")
    number =input("전화번호:")
    return name, number			# 튜플로 반환한다.

# 메뉴를 화면에 출력한다.
def display_menu() :
   print("1. 연락처 추가")
   print("2. 연락처 삭제")
   print("3. 연락처 검색")
   print("4. 연락처 출력")
   print("5. 파일저장")
   print("6. 파일출력")
   print("7. 종료")
   select = int(input("메뉴 항목을 선택하시오: "))
   return select

def main():
   address_book ={"abc":123123} 				# 공백 딕셔너리를 생성한다.
   while True :
       user = display_menu();
       if user ==1 :
          name, number = get_contact()
          address_book[name]= number		# name과 number를 추가한다.
       elif user ==2 :
          name, number = get_contact()
          address_book.pop(name)		# name을 키로 가지고 항목을 삭제한다.
       elif user ==3 :
            name =input("이름: ")
            print(name, "의 전화번호:", address_book[name])			# 도전 문제 참조
       elif user ==4 :
           for key in sorted(address_book):
               print(key,"의 전화번호:", address_book[key])
       elif user == 5 :
           with open("./phtondate.bin", "wb") as f:
               pickle.dump(address_book,f,pickle.HIGHEST_PROTOCOL)
       elif user == 6 :
           with open("./phtondate.bin", "rb") as f:
               address_book = pickle.load(f)
       else :
            break

main()
