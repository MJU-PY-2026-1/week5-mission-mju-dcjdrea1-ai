# 파일이름 :60242154_이윤재_misson2
# 작 성 자 :이윤재

age = int(input("나이를 입력하세요 : "))
coupon = input("할인 쿠폰이 있나요? (Y/N) : ")

print("-" * 30)
print("결과 :")

if age < 13 and coupon == 'Y':
    print("🍿 꼬마 VIP 고객님! 팝콘 무료 증정!")

if age >= 65 or coupon == 'Y':
    print("티켓 요금 : 무료입니다.")
else:
    print("티켓 요금 : 15,000원입니다.")