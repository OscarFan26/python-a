ry = 16.5825
rmb = 0.0603
none = True

while none:
	print('****************')
	print('鎻愮ず锛歕n1.浜烘皯甯佸厬鎹㈡垚鏃� 鍏僜n2.鏃� 鍏冨厬鎹㈡垚浜烘皯甯乗n3.閫� 鍑� 绋� 搴�')
	ask = input('璇疯緭鍏モ啋鈫掆啋')
	if ask == '1':
		a = int(input('鎮ㄨ鍏戞崲澶氬皯浜烘皯甯侊紵'))
		print(a, '鍏冧汉姘戝竵鍙互鍏戞崲', a * ry, '鏃ュ厓銆俓n')
	elif ask == '2':
		b = int(input('鎮ㄨ鍏戞崲澶氬皯鏃ュ厓锛�'))
		print(b, '鏃ュ厓鍙互鍏戞崲', b * rmb, '浜烘皯甯併�俓n')
	elif ask == '3':
		print('\n宸查��鍑虹▼搴忥紒')
		none = False
	else:
		print('\n***************')
		print('*  杈� 鍏� 閿� 璇紒*')
		print("***************\n")
