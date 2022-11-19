import time
import random

import requests
import pandas as pd

question_list = []
answer_list = []
satisfied_list = []

# question = 'china'
# http = requests.post(
#     "http://www.tuling123.com/openapi/api",
#     data={"key": "745b1100802245ee9cd8262ea95050c5",
#           "info": question})
# answer = http.json()['text']
# print(type(answer))

while True:
	question = input('请输入您的问题(‘退出’退出):')
	http = requests.post(
		"http://www.tuling123.com/openapi/api",
		data={"key": "745b1100802245ee9cd8262ea95050c5",
		      "info": question})
	answer = http.json()['text']
	if question == '退出':
		print('\n已退出！')
		break
	print('机器人的回答:{}'.format(answer))
	satisfied_list.append(random.choice(['非常满意', '满意', '非常不满', '不满意', '一般']))
	question_list.append(question)
	answer_list.append(answer)

chat_dic = {'问题': question_list, '回答': answer_list, '满意度': satisfied_list}
print(question_list, '\n', answer_list, '\n', satisfied_list, '\n', chat_dic)

# --------------------- #

df = pd.DataFrame(chat_dic)
print(df)
df.to_csv('chat_record.csv')
