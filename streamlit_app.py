books = ("헤리포터", "어린왕자", "데미안") 
borrowed = [] 

while len(borrowed) < 3: 
    print("1.헤리포터") 
    print("2.어린왕자") 
    print("3.데미안")

    choice = int(input("책 번호를 입력하세요(0:종료):"))
    
    if choice == 0:
        break
    elif 1 <= choice <= 3:
        # 이미 대출한 책인지 확인하는 조건 추가 (선택 사항)
        if books[choice-1] in borrowed:
            print("이미 대출하신 책입니다.")
        else:
            borrowed.append(books[choice-1])
            print(books[choice-1], "대출완료")
    else:
        print("잘못된 번호입니다.")  # <--- if-elif-else 세트로 묶음

print("\n대출한 책:") 
for book in borrowed: 
    print(book)