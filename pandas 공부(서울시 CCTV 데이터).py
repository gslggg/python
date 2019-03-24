#!/usr/bin/env python
# coding: utf-8

# In[14]:


import pandas as pd


# In[15]:


CCTV_Seoul = pd.read_csv('../data/CCTV_in_Seoul.csv', encoding='utf-8')
CCTV_Seoul.head()


# In[16]:


CCTV_Seoul.columns ##열 보여줘


# In[17]:


CCTV_Seoul.columns[0] ##몇번째 열 보여줘


# In[18]:


CCTV_Seoul.rename(columns={CCTV_Seoul.columns[0] : '구별'}, inplace=True)
CCTV_Seoul.head()


# In[19]:


pop_Seoul = pd.read_excel('../data/population_in_Seoul.xls', ##엑셀 파일 읽기
                          header = 2,
                          usecols = 'B, D, G, J, N',
                          encoding='utf-8'
                         )
pop_Seoul.head()


# In[20]:



pop_Seoul.rename(columns={pop_Seoul.columns[0] : '구별',  ##이름 다시 지정
                          pop_Seoul.columns[1] : '인구수', 
                          pop_Seoul.columns[2] : '한국인', 
                          pop_Seoul.columns[3] : '외국인', 
                          pop_Seoul.columns[4] : '고령자'}, inplace=True)
pop_Seoul.head()


# In[21]:


import numpy as np
import scipy as sp ##scipy import 하기


# In[22]:


s = pd.Series([1,2,3,sp.nan,6,8])


# In[23]:


s


# In[24]:


dates = pd.date_range('20130101', periods=6) ##pandas의 날짜형 데이터, period 옵션: 날짜 몇개 가져올지 지정
dates


# In[25]:


df = pd.DataFrame(sp.random.randn(6,4), index=dates, columns=['A','B','C','D']) ##  random.randn: Scipy 에서난수 생성
df


# In[26]:


df.head(3)


# In[27]:


df.index     ##Data Frame의 인덱스 확인


# In[28]:


df.columns     ##Column 확인


# In[29]:


df.values


# In[30]:


df.info()


# In[51]:


df.describe()     ##통계적 개요 확인


# In[52]:


df.sort_values(by='B', ascending=False) ##by로 지정된 컬럼을 기준이로 정렬, ascending은 오름차순(true), 내림차순(false) 옵션


# In[54]:


df


# In[55]:


df['A']


# In[56]:


df[0:3]


# In[57]:


df['20130102':'20130105']


# In[58]:


df.loc[dates[0]] ##특정 날짜의 데이터만 보고 싶을 때 사용 (0은 0번째의 데이터만 보여달라는 뜻)


# In[59]:


df.iloc[3]


# In[61]:


df.iloc[3:5,0:2]


# In[62]:


df.iloc[[1,2,4],[0,2]]


# In[63]:


df.iloc[1:3,:] ##그냥 세미콜론만 입력하면 전체라는 뜻


# In[65]:


df


# In[66]:


df[df.A>0]


# In[67]:


df2 = df.copy()


# In[68]:


df2['E'] = ['one', 'one', 'two', 'three', 'four', 'three']


# In[69]:


df2


# In[71]:


df2['E'].isin(['two','four'])


# In[78]:


CCTV_Seoul.head()


# In[80]:


CCTV_Seoul.sort_values(by='소계' , ascending = True).head(5)


# In[81]:


CCTV_Seoul


# In[84]:


CCTV_Seoul.sort_values(by='소계', ascending=False).head()


# In[31]:


CCTV_Seoul['최근증가율'] = (CCTV_Seoul['2016년'] + CCTV_Seoul['2015년'] +                          CCTV_Seoul['2014년']) / CCTV_Seoul['2013년도 이전']  * 100
CCTV_Seoul.sort_values(by='최근증가율', ascending=False).head(5)


# In[32]:


pop_Seoul.head()


# In[33]:


pop_Seoul.drop([0], inplace=True) ## 0번 행을 통째로 드랍(삭제)
pop_Seoul.head


# In[34]:


pop_Seoul['구별'].unique()     ##unique: 반복된 데이터는 하나로 나타내서 한번 이상 나타난 데이터를 확인


# In[35]:


pop_Seoul[pop_Seoul['구별'].isnull()]    ### NaN 값이 있는 행 확인, 확인되면 drop으로 삭제


# In[36]:


pop_Seoul.sort_values(by='인구수', ascending=False).head()


# In[37]:


pop_Seoul['외국인비율'] = pop_Seoul['외국인'] / pop_Seoul['인구수'] * 100   ## 어떤 열을 생성해서 데이터를 넣을 때 
pop_Seoul['고령자비율'] = pop_Seoul['고령자'] / pop_Seoul['인구수'] * 100
pop_Seoul.head()


# In[38]:


df1 = pd.DataFrame({'A': ['A0', 'A1', 'A2', 'A3'], 
                    'B': ['B0', 'B1', 'B2', 'B3'],
                    'C': ['C0', 'C1', 'C2', 'C3'],
                    'D': ['D0', 'D1', 'D2', 'D3']},
                   index=[0, 1, 2, 3])

df2 = pd.DataFrame({'A': ['A4', 'A5', 'A6', 'A7'],
                    'B': ['B4', 'B5', 'B6', 'B7'],
                    'C': ['C4', 'C5', 'C6', 'C7'],
                    'D': ['D4', 'D5', 'D6', 'D7']},
                   index=[4, 5, 6, 7])

df3 = pd.DataFrame({'A': ['A8', 'A9', 'A10', 'A11'],
                    'B': ['B8', 'B9', 'B10', 'B11'],
                    'C': ['C8', 'C9', 'C10', 'C11'],
                    'D': ['D8', 'D9', 'D10', 'D11']},
                   index=[8, 9, 10, 11])


# In[103]:


df1


# In[104]:


df2


# In[105]:


df3


# In[109]:


result = pd.concat([df1, df2, df3])           ## concat : 데이터를 단순히 열방향으로 합치기
result


# In[110]:


result = pd.concat([df1, df2, df3], keys = ['x','y','z'])   ### Keys : 이거로 합쳐진 것들을 구분, 다중 인덱스가 되어 levels을 형성함
result


# In[111]:


result.index


# In[113]:


result.index.get_level_values(0)   ## 다중 인덱스 중 0번째 레벨의 인덱스들 


# In[114]:


result.index.get_level_values(1)   ## 다중 인덱스 중 1 레벨의 인덱스들


# In[116]:


df4 = pd.DataFrame({'B': ['B2', 'B3', 'B6', 'B7'], 
                    'D': ['D2', 'D3', 'D6', 'D7'],
                    'F': ['F2', 'F3', 'F6', 'F7']},
                   index=[2, 3, 6, 7])

result = pd.concat([df1, df4], axis=1)


# In[117]:


result   ## 결과를 보면 값을 가질 수 없는 곳에 NaN이 저장됨, 값을 가질 수 없는 곳이란 인덱스 기준으로 없는 곳에는 값이 없음


# In[118]:


result = pd.concat([df1, df4], axis=1, join='inner')    ## 값이 없는 곳은 드랍하는 옵션이 join의 'inner'
result


# In[119]:


result = pd.concat([df1, df4], ignore_index=True)
result


# In[120]:


left = pd.DataFrame({'key': ['K0', 'K4', 'K2', 'K3'],
                     'A': ['A0', 'A1', 'A2', 'A3'],
                     'B': ['B0', 'B1', 'B2', 'B3']})

right = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3'],
                      'C': ['C0', 'C1', 'C2', 'C3'],
                      'D': ['D0', 'D1', 'D2', 'D3']})


# In[121]:


left


# In[122]:


right


# In[123]:


pd.merge(left, right, on='key')  ##공통된 key에 대해서만 합침


# In[125]:


pd.merge(left, right, how='left', on='key')  ## 합치는 두 데이터 중 하나만 기준으로 합칠 수도 있음. 
                                            ##이때 기준이 되는 데이터는 데이터가 다 나오고 안되는 데이터는 NaN 값이 나올 수도 있음


# In[126]:


pd.merge(left, right, how='outer', on='key')   ## 그냥 있는대로 다 합침. 데이터가 NaN이건 아니건 다 합침 (합집합)


# In[127]:


pd.merge(left, right, how='inner', on='key')   ## 교집합 형태로 합침


# In[39]:


data_result = pd.merge(CCTV_Seoul, pop_Seoul, on='구별')  ##구별을 기준으로 합침
data_result.head()


# In[40]:


del data_result['2013년도 이전']
del data_result['2014년']
del data_result['2015년']
del data_result['2016년']
data_result.head()


# In[41]:


data_result.set_index('구별', inplace=True)
data_result.head()


# In[43]:


import scipy as sp
import numpy as np


# In[44]:


sp.corrcoef(data_result['고령자비율'],data_result['소계'])


# In[45]:


sp.corrcoef(data_result['외국인비율'],data_result['소계'])


# In[46]:


sp.corrcoef(data_result['인구수'],data_result['소계'])


# In[47]:


data_result.sort_values(by='소계', ascending=False).head(5)


# In[49]:


data_result.sort_values(by='인구수', ascending=False).head()


# In[67]:


import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[68]:


plt.figure
plt.plot([1,2,3,4,5,6,7,8,9,8,7,6,5,4,3,2,1,0])
plt.show()


# In[69]:


t = sp.arange(0,12,0.01)
y = sp.sin(t)


# In[70]:


plt.figure(figsize=(10,6))


# In[71]:


import scipy as sp
t = sp.arange(0,12,0.01)   ## 0부터 12까지 0.01 간격으로 데이터 생성 : t는 단순히 값 하나가 아니라 1200개 정도의 값을 가진 일종의 배열 
y = sp.sin(t)              ## 이걸 반복문 없이 한 줄로 처리


# In[72]:


plt.figure(figsize=(10,6))
plt.plot(t,y)
plt.show()


# In[74]:


plt.figure(figsize=(10,6))
plt.plot(t,y)
plt.grid()
plt.xlabel('time')        ## 축에 라벨링 하기
plt.ylabel('Amplitude')
plt.title('Example of sinewave')   ## 그래프에 제목 붙이기
plt.show


# In[75]:


plt.figure(figsize=(10,6))    ## 한 화면에 두 개 만들기
plt.plot(t,sp.sin(t))
plt.plot(t, sp.cos(t))
plt.grid()
plt.xlabel('time')
plt.ylabel('Amplitude')
plt.title('Example of sinewave')
plt.show


# In[76]:


plt.figure(figsize=(10,6))    ## 한 화면에 두 개 만들기
plt.plot(t,sp.sin(t) , label='sin')
plt.plot(t, sp.cos(t), label = 'cos')
plt.grid()
plt.legend()         ## 범례 붙이는 옵션
plt.xlabel('time')
plt.ylabel('Amplitude')
plt.title('Example of sinewave')
plt.show


# In[77]:


s1 = sp.random.normal(loc=0, scale=1, size=1000)
s2 = sp.random.normal(loc=5, scale=0.5, size=1000)
s3 = sp.random.normal(loc=10, scale=2, size=1000)


# In[78]:


plt.figure(figsize=(10,6))
plt.plot(s1, label='s1')
plt.plot(s2, label='s2')
plt.plot(s3, label='s3')
plt.legend()
plt.show()


# In[79]:


plt.figure(figsize=(10,6))
plt.boxplot((s1,s2,s3))
plt.show()


# In[80]:


import platform

from matplotlib import font_manager, rc
plt.rcParams['axes.unicode_minus'] = False

if platform.system() == 'Darwin':
    rc('font', family='AppleGothic')
elif platform.system() == 'Windows':
    path = "c:/Windows/Fonts/malgun.ttf"
    font_name = font_manager.FontProperties(fname=path).get_name()
    rc('font', family=font_name)
else:
    print('Unknown system... sorry~~~~')


# In[81]:


data_result.head()


# In[85]:


data_result['소계'].plot(kind='barh', grid=True, figsize=(10,10))
plt.show()


# In[90]:


data_result['소계'].sort_values().plot(kind='barh', grid=True, figsize=(10,10))
plt.show()


# In[100]:


data_result['CCTV비율'] = data_result['소계'] / data_result['인구수'] * 100

data_result['CCTV비율'].sort_values().plot(kind='barh', 
                                         grid=True, figsize=(10,10))
plt.show()


# In[103]:


plt.figure(figsize=(6,6))
plt.scatter(data_result['인구수'], data_result['소계'], s=50)  ## s : 마커의 크기 옵션
plt.xlabel('인구수')
plt.ylabel('CCTV')
plt.grid()
plt.show()


# In[104]:


fp1 = sp.polyfit(data_result['인구수'], data_result['소계'], 1)
fp1


# In[105]:


f1 = sp.poly1d(fp1)
fx = sp.linspace(100000, 700000, 100)


# In[108]:


plt.figure(figsize=(10,10))
plt.scatter(data_result['인구수'], data_result['소계'], s=50)
plt.plot(fx, f1(fx), ls='dashed', lw=3, color='g')    ## 위에서 생성한 polyfit 직선을 그려줌
plt.xlabel('인구수')
plt.ylabel('CCTV')
plt.grid()
plt.show()


# In[111]:


fp1 = sp.polyfit(data_result['인구수'], data_result['소계'], 1)

f1 = sp.poly1d(fp1)
fx = sp.linspace(100000,700000, 100)

data_result['오차'] = sp.absolute(data_result['소계'] - f1(data_result['인구수']))  ## sp에는 absolute가 절대값 기능

df_sort = data_result.sort_values(by='오차', ascending=False)

df_sort.head()


# In[114]:


plt.figure(figsize=(14,10))
plt.scatter(data_result['인구수'], data_result['소계'],
           c=data_result['오차'], s=50)
plt.plot(fx, f1(fx), ls='dashed', lw=3, color='g')

for n in range(10):
    plt.text(df_sort['인구수'][n]*1.02, df_sort['소계'][n]*0.98,
            df_sort.index[n], fontsize=15)
    
plt.xlabel('인구수')
plt.ylabel('인구당비율')

plt.colorbar()
plt.grid()
plt.show()


# In[115]:


plt.figure(figsize=(14,10))
plt.scatter(data_result['인구수'], data_result['소계'],
           c=data_result['오차'], s=50)
plt.plot(fx, f1(fx), ls='dashed', lw=3, color='g')

    
plt.xlabel('인구수')
plt.ylabel('인구당비율')

plt.colorbar()
plt.grid()
plt.show()


# In[ ]:




