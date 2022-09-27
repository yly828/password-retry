#while True:
	#mode = input('請輸入遊戲模式： ')
	#if mode == 'q': #quiet
		#break
	#elif mode == '1':
		#print('啟動模式1')
	#elif mode == '2':
		#print('起動模式2')
	#else:
		#print('錯誤只能輸入q or 1 or 2')

password = 'a123456'
i = 3
while i > 0:
    usercode = input('請輸入密碼： ')
    i = i - 1
    if usercode == password:
    	print('登入成功！')
    	break
    elif i > 0:
    	print('錯誤 你還剩', i, '次機會')
 

    	

















