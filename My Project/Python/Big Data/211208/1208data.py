#!/usr/bin/env python
# coding: utf-8

# # <Step1. 탐색> : 데이터의 기초 정보 살펴보기

# # . csv
# 행이 ',' 콤마로 구분된 파일
# # . tsv
# 행이 '   ' tab로 구분된 파일
# # excel(.xlsx) 파일은 내보내기 후 csv 또는 tsv 로 전환

# # 데이터의 외형적 분석
# 1. 데이터의 출처
# 2. 데이터의 크기
# 3. 데이터의 구성요소
# 
# 샘플링 (sampleing) 어떤 자료로 부터 값을 추출하는 것

# # [Chipotle 데이터셋의 기본 정보]

# In[12]:


# pandas 모듈 임포트
import pandas as pd

# read_csv() 함수로 데이터를 Dataframe 형태로 불러옵니다.
# pd.read_csv("파일경로를 포함한 파일명", sep="구분자")
# 로데이터를 상대 경로로 불러오기
file_path = '../data/chipotle.tsv'
chipo = pd.read_csv(file_path, sep='\t')

print(chipo.shape)
print("------------------------------------")
print(chipo.info())


# chipo 라는 Dataframe에서 순서대로 10개의 row 데이터를 보여줍니다.
# head() 함수에 인수를 생략하면 기본 5개의 데이터를 보여줌

# In[13]:


chipo.head(10)


# In[147]:


chipo.tail(10)


# In[18]:


# columns() 함수로 컴럼의 정보를 보여줌
print(chipo.columns)
print("-------------------------")
print(chipo.index)


# [Chipotle 데이터셋의 수치적 특징 파악]

# quantity와 item_price의 요약 통계

# describe() 함수로 요약 통계량 출력하기

# In[20]:


# order_id는 숫자와 의미를 가지지 않기 때문에 str로 변환
chipo['order_id'] = chipo['order_id'].astype(str)
# chipo dataframe에서 수치형 피처들의 요약 통계량을 확인
chipo.describe()


# unique 함수로 범주형 피처의 개수 출력하기

# In[21]:


# order_id의 개수를 출력
len(chipo['order_id'].unique())


# In[56]:


# item_name의 개수를 출력
len(chipo['item_name'].unique())


# In[57]:


# 가장 많이 주문한 item : top 10을 출력합니다.
item_count = chipo['item_name'].value_counts()[:10]
for idx, (val, cnt) in enumerate(item_count.iteritems(),1):
    print("Top" , idx , ":", val, cnt)


# [item당 주문 개수와 총량 구하기]

# In[58]:


# 아이템별 주문 개수를 출력합니다.
order_count = chipo.groupby('item_name')['order_id'].count()
order_count[:10] # 아이템별 주문 개수를 출력


# In[59]:


# 아이템별 주문 총량을 계산합니다.
item_quantity = chipo.groupby('item_name')['quantity'].sum()
item_quantity[:10] # 아이템별 주문 총량을 출력


# # 시각화로 분석 결과 살펴보기

# In[81]:


# %matplotlib inline
import numpy as np
import matplotlib.pyplot as plt

# 아이템별 주문의 총량을 막대 그래프로 시각화
item_name_list = item_quantity.index.tolist()

# numpy.arange(시작, 끝, 간격) 으로 배열 만들기
x_pos = np.arange(len(item_name_list))
order_cnt = item_quantity.values.tolist()

# bar()는 막대 그래프를 출력 하는 함수
plt.bar(x_pos, order_cnt, align='center')
plt.ylabel('ordered_item_count')
plt.title('Distribution of all orderd item')

plt.show()


# 아이템의 주문 개수를 출력

# In[144]:


oo = order_count.index.tolist()
# oo
x_pos = np.arange(len(oo))
tt = order_count.values.tolist()
plt.bar(x_pos, tt, align='center')
plt.ylabel('order_count')
plt.title('Distribution of count item')
plt.show()


# item_pruce 피처 살펴보기

# In[143]:


# scatter piot
plt.scatter(x_pos, tt, label="count", c ="black", marker=5 )
plt.xlabel('count')
plt.ylabel('order_count')
plt.title('Distribution of count item')
plt.legend(loc='upper right')
plt.show()


# In[141]:


# scatter piot
plt.scatter(x_pos, tt, label="count")
plt.xlabel('count')
plt.ylabel('order_count')
plt.title('distribution of count item')
plt.legend(loc='best')
plt.show()


# In[145]:


chipo.info()
print('---------')
chipo['item_price'].head()


# In[133]:


chipo['item_name'].value_counts()[:10]


# In[134]:


chipo['item_name'].unique().tolist()[:10]


# In[158]:


import numpy as np
import matplotlib.pyplot as plt

data = np.random.random((8, 8))
plt.imshow(data, cmap='cool', interpolation='nearest')
plt.show()


# In[ ]:




