牌箱=['紅心2', '黑桃2', '梅花3', '紅心3', '方塊4', '黑桃4', '紅心7', '紅心8', '紅心9']
同花張數= 5
牌箱深度=len(牌箱)

def 抓同花(手上的牌, 第幾抽):

	if 第幾抽 == 牌箱深度:
		 if len(手上的牌) == 同花張數 and 手上的牌[0][:2]==手上的牌[1][:2]==手上的牌[2][:2]==手上的牌[3][:2]==手上的牌[4][0:2]: 
		 		print("抓同花=", 手上的牌) # bug 同花順
		 return # 上帝指示

	抓同花(手上的牌, 第幾抽+1) # 不掀開即為不抓
	
	掀開的牌=牌箱[第幾抽]
	拷貝那份=手上的牌.copy()
	拷貝那份.append(掀開的牌) # 加進手上的牌
	手上的牌=拷貝那份
	抓同花(手上的牌, 第幾抽+1)
#######################
def 排除元素(原容器, 該排除的元素):
	新容器 = []
	for 元素 in 原容器: 
		if 元素 not in 該排除的元素: 新容器.append(元素)
	return 新容器
#######################
抓同花([], 0)

# 輸出:
# 抓同花=['紅心2', '紅心3', '紅心7', '紅心8', '紅心9']
