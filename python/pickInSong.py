曾經的多情=['周渝民', '汪小菲', '具俊曄', '小S'] # 名字互斥 不重複
此生緣份數= 2 # 一心多用的上限 想起的畫面與輪廓

# 情境: 大S 擔心逛百貨公司遇到舊男友
# 過去情景像電影 輕輕浮在眼前
# 自己呼叫自己 程式是立體的 高度資料相依

def 讓我遇見你(此刻的多情, 再起一段緣): # 此刻的多情 當容器

	if 再起一段緣 == len(曾經的多情):
		if len(此刻的多情) == 此生緣份數: # 達到設定的緣份數
			print("回想起跟 " + str(此刻的多情) + " 的那些過往")
			
		return # 多情惹煩惱 上帝說不要想太多

	讓我遇見你(此刻的多情, 再起一段緣+1) # 是否記住他? 淡忘他
	
	拷貝的多情=此刻的多情.copy()
	那個人=曾經的多情[再起一段緣]
	拷貝的多情.append(那個人) # 放進記憶空間 容器
	讓我遇見你(拷貝的多情, 再起一段緣+1) # 是否記住他? 記住他
	
#########################
讓我遇見你([], 0)

# 輸出此刻的多情(記憶空間內)的那些畫面與輪廓:
# 回想起跟 ['具俊曄', '小S'] 的那些過往
# 回想起跟 ['汪小菲', '小S'] 的那些過往
# 回想起跟 ['汪小菲', '具俊曄'] 的那些過往
# 回想起跟 ['周渝民', '小S'] 的那些過往
# 回想起跟 ['周渝民', '具俊曄'] 的那些過往
# 回想起跟 ['周渝民', '汪小菲'] 的那些過往