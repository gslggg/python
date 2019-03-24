

```python
import pandas as pd
```


```python
CCTV_Seoul = pd.read_csv('../data/CCTV_in_Seoul.csv', encoding='utf-8')
CCTV_Seoul.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>기관명</th>
      <th>소계</th>
      <th>2013년도 이전</th>
      <th>2014년</th>
      <th>2015년</th>
      <th>2016년</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>강남구</td>
      <td>3238</td>
      <td>1292</td>
      <td>430</td>
      <td>584</td>
      <td>932</td>
    </tr>
    <tr>
      <th>1</th>
      <td>강동구</td>
      <td>1010</td>
      <td>379</td>
      <td>99</td>
      <td>155</td>
      <td>377</td>
    </tr>
    <tr>
      <th>2</th>
      <td>강북구</td>
      <td>831</td>
      <td>369</td>
      <td>120</td>
      <td>138</td>
      <td>204</td>
    </tr>
    <tr>
      <th>3</th>
      <td>강서구</td>
      <td>911</td>
      <td>388</td>
      <td>258</td>
      <td>184</td>
      <td>81</td>
    </tr>
    <tr>
      <th>4</th>
      <td>관악구</td>
      <td>2109</td>
      <td>846</td>
      <td>260</td>
      <td>390</td>
      <td>613</td>
    </tr>
  </tbody>
</table>
</div>




```python
CCTV_Seoul.columns ##열 보여줘
```




    Index(['기관명', '소계', '2013년도 이전', '2014년', '2015년', '2016년'], dtype='object')




```python
CCTV_Seoul.columns[0] ##몇번째 열 보여줘
```




    '기관명'




```python
CCTV_Seoul.rename(columns={CCTV_Seoul.columns[0] : '구별'}, inplace=True)
CCTV_Seoul.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>구별</th>
      <th>소계</th>
      <th>2013년도 이전</th>
      <th>2014년</th>
      <th>2015년</th>
      <th>2016년</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>강남구</td>
      <td>3238</td>
      <td>1292</td>
      <td>430</td>
      <td>584</td>
      <td>932</td>
    </tr>
    <tr>
      <th>1</th>
      <td>강동구</td>
      <td>1010</td>
      <td>379</td>
      <td>99</td>
      <td>155</td>
      <td>377</td>
    </tr>
    <tr>
      <th>2</th>
      <td>강북구</td>
      <td>831</td>
      <td>369</td>
      <td>120</td>
      <td>138</td>
      <td>204</td>
    </tr>
    <tr>
      <th>3</th>
      <td>강서구</td>
      <td>911</td>
      <td>388</td>
      <td>258</td>
      <td>184</td>
      <td>81</td>
    </tr>
    <tr>
      <th>4</th>
      <td>관악구</td>
      <td>2109</td>
      <td>846</td>
      <td>260</td>
      <td>390</td>
      <td>613</td>
    </tr>
  </tbody>
</table>
</div>




```python
pop_Seoul = pd.read_excel('../data/population_in_Seoul.xls', ##엑셀 파일 읽기
                          header = 2,
                          usecols = 'B, D, G, J, N',
                          encoding='utf-8'
                         )
pop_Seoul.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>자치구</th>
      <th>계</th>
      <th>계.1</th>
      <th>계.2</th>
      <th>65세이상고령자</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>합계</td>
      <td>10049607</td>
      <td>9765623</td>
      <td>283984</td>
      <td>1416131</td>
    </tr>
    <tr>
      <th>1</th>
      <td>종로구</td>
      <td>163026</td>
      <td>153065</td>
      <td>9961</td>
      <td>26742</td>
    </tr>
    <tr>
      <th>2</th>
      <td>중구</td>
      <td>135633</td>
      <td>125725</td>
      <td>9908</td>
      <td>22005</td>
    </tr>
    <tr>
      <th>3</th>
      <td>용산구</td>
      <td>245090</td>
      <td>228999</td>
      <td>16091</td>
      <td>37640</td>
    </tr>
    <tr>
      <th>4</th>
      <td>성동구</td>
      <td>316463</td>
      <td>308221</td>
      <td>8242</td>
      <td>42767</td>
    </tr>
  </tbody>
</table>
</div>




```python

pop_Seoul.rename(columns={pop_Seoul.columns[0] : '구별',  ##이름 다시 지정
                          pop_Seoul.columns[1] : '인구수', 
                          pop_Seoul.columns[2] : '한국인', 
                          pop_Seoul.columns[3] : '외국인', 
                          pop_Seoul.columns[4] : '고령자'}, inplace=True)
pop_Seoul.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>구별</th>
      <th>인구수</th>
      <th>한국인</th>
      <th>외국인</th>
      <th>고령자</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>합계</td>
      <td>10049607</td>
      <td>9765623</td>
      <td>283984</td>
      <td>1416131</td>
    </tr>
    <tr>
      <th>1</th>
      <td>종로구</td>
      <td>163026</td>
      <td>153065</td>
      <td>9961</td>
      <td>26742</td>
    </tr>
    <tr>
      <th>2</th>
      <td>중구</td>
      <td>135633</td>
      <td>125725</td>
      <td>9908</td>
      <td>22005</td>
    </tr>
    <tr>
      <th>3</th>
      <td>용산구</td>
      <td>245090</td>
      <td>228999</td>
      <td>16091</td>
      <td>37640</td>
    </tr>
    <tr>
      <th>4</th>
      <td>성동구</td>
      <td>316463</td>
      <td>308221</td>
      <td>8242</td>
      <td>42767</td>
    </tr>
  </tbody>
</table>
</div>




```python
import numpy as np
import scipy as sp ##scipy import 하기
```


```python
s = pd.Series([1,2,3,sp.nan,6,8])
```


```python
s
```




    0    1.0
    1    2.0
    2    3.0
    3    NaN
    4    6.0
    5    8.0
    dtype: float64




```python
dates = pd.date_range('20130101', periods=6) ##pandas의 날짜형 데이터, period 옵션: 날짜 몇개 가져올지 지정
dates

```




    DatetimeIndex(['2013-01-01', '2013-01-02', '2013-01-03', '2013-01-04',
                   '2013-01-05', '2013-01-06'],
                  dtype='datetime64[ns]', freq='D')




```python
df = pd.DataFrame(sp.random.randn(6,4), index=dates, columns=['A','B','C','D']) ##  random.randn: Scipy 에서난수 생성
df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>A</th>
      <th>B</th>
      <th>C</th>
      <th>D</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2013-01-01</th>
      <td>0.817893</td>
      <td>0.872940</td>
      <td>1.193569</td>
      <td>-0.653204</td>
    </tr>
    <tr>
      <th>2013-01-02</th>
      <td>0.246680</td>
      <td>0.000871</td>
      <td>-0.217152</td>
      <td>-0.284268</td>
    </tr>
    <tr>
      <th>2013-01-03</th>
      <td>0.297496</td>
      <td>0.272275</td>
      <td>1.558567</td>
      <td>1.387684</td>
    </tr>
    <tr>
      <th>2013-01-04</th>
      <td>-0.255195</td>
      <td>-0.124405</td>
      <td>-1.380512</td>
      <td>-0.282155</td>
    </tr>
    <tr>
      <th>2013-01-05</th>
      <td>-1.414675</td>
      <td>-0.515134</td>
      <td>-1.192528</td>
      <td>-0.479870</td>
    </tr>
    <tr>
      <th>2013-01-06</th>
      <td>0.211673</td>
      <td>-0.445355</td>
      <td>-0.461643</td>
      <td>0.563072</td>
    </tr>
  </tbody>
</table>
</div>




```python
df.head(3)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>A</th>
      <th>B</th>
      <th>C</th>
      <th>D</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2013-01-01</th>
      <td>0.817893</td>
      <td>0.872940</td>
      <td>1.193569</td>
      <td>-0.653204</td>
    </tr>
    <tr>
      <th>2013-01-02</th>
      <td>0.246680</td>
      <td>0.000871</td>
      <td>-0.217152</td>
      <td>-0.284268</td>
    </tr>
    <tr>
      <th>2013-01-03</th>
      <td>0.297496</td>
      <td>0.272275</td>
      <td>1.558567</td>
      <td>1.387684</td>
    </tr>
  </tbody>
</table>
</div>




```python
df.index     ##Data Frame의 인덱스 확인
```




    DatetimeIndex(['2013-01-01', '2013-01-02', '2013-01-03', '2013-01-04',
                   '2013-01-05', '2013-01-06'],
                  dtype='datetime64[ns]', freq='D')




```python
df.columns     ##Column 확인
```




    Index(['A', 'B', 'C', 'D'], dtype='object')




```python
df.values
```




    array([[ 8.17892593e-01,  8.72939733e-01,  1.19356893e+00,
            -6.53204466e-01],
           [ 2.46680134e-01,  8.70815575e-04, -2.17151798e-01,
            -2.84267811e-01],
           [ 2.97496008e-01,  2.72274513e-01,  1.55856747e+00,
             1.38768378e+00],
           [-2.55195340e-01, -1.24404874e-01, -1.38051216e+00,
            -2.82155276e-01],
           [-1.41467495e+00, -5.15134054e-01, -1.19252798e+00,
            -4.79869996e-01],
           [ 2.11673490e-01, -4.45355009e-01, -4.61643173e-01,
             5.63071757e-01]])




```python
df.info()
```

    <class 'pandas.core.frame.DataFrame'>
    DatetimeIndex: 6 entries, 2013-01-01 to 2013-01-06
    Freq: D
    Data columns (total 4 columns):
    A    6 non-null float64
    B    6 non-null float64
    C    6 non-null float64
    D    6 non-null float64
    dtypes: float64(4)
    memory usage: 240.0 bytes
    


```python
df.describe()     ##통계적 개요 확인
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>A</th>
      <th>B</th>
      <th>C</th>
      <th>D</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>count</th>
      <td>6.000000</td>
      <td>6.000000</td>
      <td>6.000000</td>
      <td>6.000000</td>
    </tr>
    <tr>
      <th>mean</th>
      <td>0.470984</td>
      <td>0.078153</td>
      <td>-0.252168</td>
      <td>0.374038</td>
    </tr>
    <tr>
      <th>std</th>
      <td>0.738086</td>
      <td>1.006135</td>
      <td>0.831355</td>
      <td>1.588745</td>
    </tr>
    <tr>
      <th>min</th>
      <td>-0.230660</td>
      <td>-0.807354</td>
      <td>-1.325596</td>
      <td>-1.284254</td>
    </tr>
    <tr>
      <th>25%</th>
      <td>-0.126937</td>
      <td>-0.675948</td>
      <td>-0.963495</td>
      <td>-0.717208</td>
    </tr>
    <tr>
      <th>50%</th>
      <td>0.256326</td>
      <td>-0.311023</td>
      <td>0.022726</td>
      <td>0.315595</td>
    </tr>
    <tr>
      <th>75%</th>
      <td>1.127846</td>
      <td>0.928103</td>
      <td>0.365845</td>
      <td>0.672789</td>
    </tr>
    <tr>
      <th>max</th>
      <td>1.380251</td>
      <td>1.354760</td>
      <td>0.579153</td>
      <td>3.166914</td>
    </tr>
  </tbody>
</table>
</div>




```python
df.sort_values(by='B', ascending=False) ##by로 지정된 컬럼을 기준이로 정렬, ascending은 오름차순(true), 내림차순(false) 옵션
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>A</th>
      <th>B</th>
      <th>C</th>
      <th>D</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2013-01-04</th>
      <td>1.296971</td>
      <td>1.354760</td>
      <td>-1.207004</td>
      <td>0.030650</td>
    </tr>
    <tr>
      <th>2013-01-02</th>
      <td>-0.107818</td>
      <td>1.337022</td>
      <td>-1.325596</td>
      <td>-0.966494</td>
    </tr>
    <tr>
      <th>2013-01-01</th>
      <td>0.620470</td>
      <td>-0.298651</td>
      <td>0.579153</td>
      <td>0.696872</td>
    </tr>
    <tr>
      <th>2013-01-03</th>
      <td>-0.133310</td>
      <td>-0.323395</td>
      <td>0.394985</td>
      <td>-1.284254</td>
    </tr>
    <tr>
      <th>2013-01-06</th>
      <td>1.380251</td>
      <td>-0.793465</td>
      <td>-0.232971</td>
      <td>3.166914</td>
    </tr>
    <tr>
      <th>2013-01-05</th>
      <td>-0.230660</td>
      <td>-0.807354</td>
      <td>0.278423</td>
      <td>0.600540</td>
    </tr>
  </tbody>
</table>
</div>




```python
df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>A</th>
      <th>B</th>
      <th>C</th>
      <th>D</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2013-01-01</th>
      <td>0.620470</td>
      <td>-0.298651</td>
      <td>0.579153</td>
      <td>0.696872</td>
    </tr>
    <tr>
      <th>2013-01-02</th>
      <td>-0.107818</td>
      <td>1.337022</td>
      <td>-1.325596</td>
      <td>-0.966494</td>
    </tr>
    <tr>
      <th>2013-01-03</th>
      <td>-0.133310</td>
      <td>-0.323395</td>
      <td>0.394985</td>
      <td>-1.284254</td>
    </tr>
    <tr>
      <th>2013-01-04</th>
      <td>1.296971</td>
      <td>1.354760</td>
      <td>-1.207004</td>
      <td>0.030650</td>
    </tr>
    <tr>
      <th>2013-01-05</th>
      <td>-0.230660</td>
      <td>-0.807354</td>
      <td>0.278423</td>
      <td>0.600540</td>
    </tr>
    <tr>
      <th>2013-01-06</th>
      <td>1.380251</td>
      <td>-0.793465</td>
      <td>-0.232971</td>
      <td>3.166914</td>
    </tr>
  </tbody>
</table>
</div>




```python
df['A']
```




    2013-01-01    0.620470
    2013-01-02   -0.107818
    2013-01-03   -0.133310
    2013-01-04    1.296971
    2013-01-05   -0.230660
    2013-01-06    1.380251
    Freq: D, Name: A, dtype: float64




```python
df[0:3]
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>A</th>
      <th>B</th>
      <th>C</th>
      <th>D</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2013-01-01</th>
      <td>0.620470</td>
      <td>-0.298651</td>
      <td>0.579153</td>
      <td>0.696872</td>
    </tr>
    <tr>
      <th>2013-01-02</th>
      <td>-0.107818</td>
      <td>1.337022</td>
      <td>-1.325596</td>
      <td>-0.966494</td>
    </tr>
    <tr>
      <th>2013-01-03</th>
      <td>-0.133310</td>
      <td>-0.323395</td>
      <td>0.394985</td>
      <td>-1.284254</td>
    </tr>
  </tbody>
</table>
</div>




```python
df['20130102':'20130105']
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>A</th>
      <th>B</th>
      <th>C</th>
      <th>D</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2013-01-02</th>
      <td>-0.107818</td>
      <td>1.337022</td>
      <td>-1.325596</td>
      <td>-0.966494</td>
    </tr>
    <tr>
      <th>2013-01-03</th>
      <td>-0.133310</td>
      <td>-0.323395</td>
      <td>0.394985</td>
      <td>-1.284254</td>
    </tr>
    <tr>
      <th>2013-01-04</th>
      <td>1.296971</td>
      <td>1.354760</td>
      <td>-1.207004</td>
      <td>0.030650</td>
    </tr>
    <tr>
      <th>2013-01-05</th>
      <td>-0.230660</td>
      <td>-0.807354</td>
      <td>0.278423</td>
      <td>0.600540</td>
    </tr>
  </tbody>
</table>
</div>




```python
df.loc[dates[0]] ##특정 날짜의 데이터만 보고 싶을 때 사용 (0은 0번째의 데이터만 보여달라는 뜻)
```




    A    0.620470
    B   -0.298651
    C    0.579153
    D    0.696872
    Name: 2013-01-01 00:00:00, dtype: float64




```python
df.iloc[3]
```




    A    1.296971
    B    1.354760
    C   -1.207004
    D    0.030650
    Name: 2013-01-04 00:00:00, dtype: float64




```python
df.iloc[3:5,0:2]
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>A</th>
      <th>B</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2013-01-04</th>
      <td>1.296971</td>
      <td>1.354760</td>
    </tr>
    <tr>
      <th>2013-01-05</th>
      <td>-0.230660</td>
      <td>-0.807354</td>
    </tr>
  </tbody>
</table>
</div>




```python
df.iloc[[1,2,4],[0,2]]
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>A</th>
      <th>C</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2013-01-02</th>
      <td>-0.107818</td>
      <td>-1.325596</td>
    </tr>
    <tr>
      <th>2013-01-03</th>
      <td>-0.133310</td>
      <td>0.394985</td>
    </tr>
    <tr>
      <th>2013-01-05</th>
      <td>-0.230660</td>
      <td>0.278423</td>
    </tr>
  </tbody>
</table>
</div>




```python
df.iloc[1:3,:] ##그냥 세미콜론만 입력하면 전체라는 뜻
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>A</th>
      <th>B</th>
      <th>C</th>
      <th>D</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2013-01-02</th>
      <td>-0.107818</td>
      <td>1.337022</td>
      <td>-1.325596</td>
      <td>-0.966494</td>
    </tr>
    <tr>
      <th>2013-01-03</th>
      <td>-0.133310</td>
      <td>-0.323395</td>
      <td>0.394985</td>
      <td>-1.284254</td>
    </tr>
  </tbody>
</table>
</div>




```python
df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>A</th>
      <th>B</th>
      <th>C</th>
      <th>D</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2013-01-01</th>
      <td>0.620470</td>
      <td>-0.298651</td>
      <td>0.579153</td>
      <td>0.696872</td>
    </tr>
    <tr>
      <th>2013-01-02</th>
      <td>-0.107818</td>
      <td>1.337022</td>
      <td>-1.325596</td>
      <td>-0.966494</td>
    </tr>
    <tr>
      <th>2013-01-03</th>
      <td>-0.133310</td>
      <td>-0.323395</td>
      <td>0.394985</td>
      <td>-1.284254</td>
    </tr>
    <tr>
      <th>2013-01-04</th>
      <td>1.296971</td>
      <td>1.354760</td>
      <td>-1.207004</td>
      <td>0.030650</td>
    </tr>
    <tr>
      <th>2013-01-05</th>
      <td>-0.230660</td>
      <td>-0.807354</td>
      <td>0.278423</td>
      <td>0.600540</td>
    </tr>
    <tr>
      <th>2013-01-06</th>
      <td>1.380251</td>
      <td>-0.793465</td>
      <td>-0.232971</td>
      <td>3.166914</td>
    </tr>
  </tbody>
</table>
</div>




```python
df[df.A>0]
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>A</th>
      <th>B</th>
      <th>C</th>
      <th>D</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2013-01-01</th>
      <td>0.620470</td>
      <td>-0.298651</td>
      <td>0.579153</td>
      <td>0.696872</td>
    </tr>
    <tr>
      <th>2013-01-04</th>
      <td>1.296971</td>
      <td>1.354760</td>
      <td>-1.207004</td>
      <td>0.030650</td>
    </tr>
    <tr>
      <th>2013-01-06</th>
      <td>1.380251</td>
      <td>-0.793465</td>
      <td>-0.232971</td>
      <td>3.166914</td>
    </tr>
  </tbody>
</table>
</div>




```python
df2 = df.copy()
```


```python
df2['E'] = ['one', 'one', 'two', 'three', 'four', 'three']
```


```python
df2
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>A</th>
      <th>B</th>
      <th>C</th>
      <th>D</th>
      <th>E</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2013-01-01</th>
      <td>0.620470</td>
      <td>-0.298651</td>
      <td>0.579153</td>
      <td>0.696872</td>
      <td>one</td>
    </tr>
    <tr>
      <th>2013-01-02</th>
      <td>-0.107818</td>
      <td>1.337022</td>
      <td>-1.325596</td>
      <td>-0.966494</td>
      <td>one</td>
    </tr>
    <tr>
      <th>2013-01-03</th>
      <td>-0.133310</td>
      <td>-0.323395</td>
      <td>0.394985</td>
      <td>-1.284254</td>
      <td>two</td>
    </tr>
    <tr>
      <th>2013-01-04</th>
      <td>1.296971</td>
      <td>1.354760</td>
      <td>-1.207004</td>
      <td>0.030650</td>
      <td>three</td>
    </tr>
    <tr>
      <th>2013-01-05</th>
      <td>-0.230660</td>
      <td>-0.807354</td>
      <td>0.278423</td>
      <td>0.600540</td>
      <td>four</td>
    </tr>
    <tr>
      <th>2013-01-06</th>
      <td>1.380251</td>
      <td>-0.793465</td>
      <td>-0.232971</td>
      <td>3.166914</td>
      <td>three</td>
    </tr>
  </tbody>
</table>
</div>




```python
df2['E'].isin(['two','four'])
```




    2013-01-01    False
    2013-01-02    False
    2013-01-03     True
    2013-01-04    False
    2013-01-05     True
    2013-01-06    False
    Freq: D, Name: E, dtype: bool




```python
CCTV_Seoul.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>구별</th>
      <th>소계</th>
      <th>2013년도 이전</th>
      <th>2014년</th>
      <th>2015년</th>
      <th>2016년</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>강남구</td>
      <td>3238</td>
      <td>1292</td>
      <td>430</td>
      <td>584</td>
      <td>932</td>
    </tr>
    <tr>
      <th>1</th>
      <td>강동구</td>
      <td>1010</td>
      <td>379</td>
      <td>99</td>
      <td>155</td>
      <td>377</td>
    </tr>
    <tr>
      <th>2</th>
      <td>강북구</td>
      <td>831</td>
      <td>369</td>
      <td>120</td>
      <td>138</td>
      <td>204</td>
    </tr>
    <tr>
      <th>3</th>
      <td>강서구</td>
      <td>911</td>
      <td>388</td>
      <td>258</td>
      <td>184</td>
      <td>81</td>
    </tr>
    <tr>
      <th>4</th>
      <td>관악구</td>
      <td>2109</td>
      <td>846</td>
      <td>260</td>
      <td>390</td>
      <td>613</td>
    </tr>
  </tbody>
</table>
</div>




```python
CCTV_Seoul.sort_values(by='소계' , ascending = True).head(5)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>구별</th>
      <th>소계</th>
      <th>2013년도 이전</th>
      <th>2014년</th>
      <th>2015년</th>
      <th>2016년</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>9</th>
      <td>도봉구</td>
      <td>825</td>
      <td>238</td>
      <td>159</td>
      <td>42</td>
      <td>386</td>
    </tr>
    <tr>
      <th>2</th>
      <td>강북구</td>
      <td>831</td>
      <td>369</td>
      <td>120</td>
      <td>138</td>
      <td>204</td>
    </tr>
    <tr>
      <th>5</th>
      <td>광진구</td>
      <td>878</td>
      <td>573</td>
      <td>78</td>
      <td>53</td>
      <td>174</td>
    </tr>
    <tr>
      <th>3</th>
      <td>강서구</td>
      <td>911</td>
      <td>388</td>
      <td>258</td>
      <td>184</td>
      <td>81</td>
    </tr>
    <tr>
      <th>24</th>
      <td>중랑구</td>
      <td>916</td>
      <td>509</td>
      <td>121</td>
      <td>177</td>
      <td>109</td>
    </tr>
  </tbody>
</table>
</div>




```python
CCTV_Seoul
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>구별</th>
      <th>소계</th>
      <th>2013년도 이전</th>
      <th>2014년</th>
      <th>2015년</th>
      <th>2016년</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>강남구</td>
      <td>3238</td>
      <td>1292</td>
      <td>430</td>
      <td>584</td>
      <td>932</td>
    </tr>
    <tr>
      <th>1</th>
      <td>강동구</td>
      <td>1010</td>
      <td>379</td>
      <td>99</td>
      <td>155</td>
      <td>377</td>
    </tr>
    <tr>
      <th>2</th>
      <td>강북구</td>
      <td>831</td>
      <td>369</td>
      <td>120</td>
      <td>138</td>
      <td>204</td>
    </tr>
    <tr>
      <th>3</th>
      <td>강서구</td>
      <td>911</td>
      <td>388</td>
      <td>258</td>
      <td>184</td>
      <td>81</td>
    </tr>
    <tr>
      <th>4</th>
      <td>관악구</td>
      <td>2109</td>
      <td>846</td>
      <td>260</td>
      <td>390</td>
      <td>613</td>
    </tr>
    <tr>
      <th>5</th>
      <td>광진구</td>
      <td>878</td>
      <td>573</td>
      <td>78</td>
      <td>53</td>
      <td>174</td>
    </tr>
    <tr>
      <th>6</th>
      <td>구로구</td>
      <td>1884</td>
      <td>1142</td>
      <td>173</td>
      <td>246</td>
      <td>323</td>
    </tr>
    <tr>
      <th>7</th>
      <td>금천구</td>
      <td>1348</td>
      <td>674</td>
      <td>51</td>
      <td>269</td>
      <td>354</td>
    </tr>
    <tr>
      <th>8</th>
      <td>노원구</td>
      <td>1566</td>
      <td>542</td>
      <td>57</td>
      <td>451</td>
      <td>516</td>
    </tr>
    <tr>
      <th>9</th>
      <td>도봉구</td>
      <td>825</td>
      <td>238</td>
      <td>159</td>
      <td>42</td>
      <td>386</td>
    </tr>
    <tr>
      <th>10</th>
      <td>동대문구</td>
      <td>1870</td>
      <td>1070</td>
      <td>23</td>
      <td>198</td>
      <td>579</td>
    </tr>
    <tr>
      <th>11</th>
      <td>동작구</td>
      <td>1302</td>
      <td>544</td>
      <td>341</td>
      <td>103</td>
      <td>314</td>
    </tr>
    <tr>
      <th>12</th>
      <td>마포구</td>
      <td>980</td>
      <td>314</td>
      <td>118</td>
      <td>169</td>
      <td>379</td>
    </tr>
    <tr>
      <th>13</th>
      <td>서대문구</td>
      <td>1254</td>
      <td>844</td>
      <td>50</td>
      <td>68</td>
      <td>292</td>
    </tr>
    <tr>
      <th>14</th>
      <td>서초구</td>
      <td>2297</td>
      <td>1406</td>
      <td>157</td>
      <td>336</td>
      <td>398</td>
    </tr>
    <tr>
      <th>15</th>
      <td>성동구</td>
      <td>1327</td>
      <td>730</td>
      <td>91</td>
      <td>241</td>
      <td>265</td>
    </tr>
    <tr>
      <th>16</th>
      <td>성북구</td>
      <td>1651</td>
      <td>1009</td>
      <td>78</td>
      <td>360</td>
      <td>204</td>
    </tr>
    <tr>
      <th>17</th>
      <td>송파구</td>
      <td>1081</td>
      <td>529</td>
      <td>21</td>
      <td>68</td>
      <td>463</td>
    </tr>
    <tr>
      <th>18</th>
      <td>양천구</td>
      <td>2482</td>
      <td>1843</td>
      <td>142</td>
      <td>30</td>
      <td>467</td>
    </tr>
    <tr>
      <th>19</th>
      <td>영등포구</td>
      <td>1277</td>
      <td>495</td>
      <td>214</td>
      <td>195</td>
      <td>373</td>
    </tr>
    <tr>
      <th>20</th>
      <td>용산구</td>
      <td>2096</td>
      <td>1368</td>
      <td>218</td>
      <td>112</td>
      <td>398</td>
    </tr>
    <tr>
      <th>21</th>
      <td>은평구</td>
      <td>2108</td>
      <td>1138</td>
      <td>224</td>
      <td>278</td>
      <td>468</td>
    </tr>
    <tr>
      <th>22</th>
      <td>종로구</td>
      <td>1619</td>
      <td>464</td>
      <td>314</td>
      <td>211</td>
      <td>630</td>
    </tr>
    <tr>
      <th>23</th>
      <td>중구</td>
      <td>1023</td>
      <td>413</td>
      <td>190</td>
      <td>72</td>
      <td>348</td>
    </tr>
    <tr>
      <th>24</th>
      <td>중랑구</td>
      <td>916</td>
      <td>509</td>
      <td>121</td>
      <td>177</td>
      <td>109</td>
    </tr>
  </tbody>
</table>
</div>




```python
CCTV_Seoul.sort_values(by='소계', ascending=False).head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>구별</th>
      <th>소계</th>
      <th>2013년도 이전</th>
      <th>2014년</th>
      <th>2015년</th>
      <th>2016년</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>강남구</td>
      <td>3238</td>
      <td>1292</td>
      <td>430</td>
      <td>584</td>
      <td>932</td>
    </tr>
    <tr>
      <th>18</th>
      <td>양천구</td>
      <td>2482</td>
      <td>1843</td>
      <td>142</td>
      <td>30</td>
      <td>467</td>
    </tr>
    <tr>
      <th>14</th>
      <td>서초구</td>
      <td>2297</td>
      <td>1406</td>
      <td>157</td>
      <td>336</td>
      <td>398</td>
    </tr>
    <tr>
      <th>4</th>
      <td>관악구</td>
      <td>2109</td>
      <td>846</td>
      <td>260</td>
      <td>390</td>
      <td>613</td>
    </tr>
    <tr>
      <th>21</th>
      <td>은평구</td>
      <td>2108</td>
      <td>1138</td>
      <td>224</td>
      <td>278</td>
      <td>468</td>
    </tr>
  </tbody>
</table>
</div>




```python
CCTV_Seoul['최근증가율'] = (CCTV_Seoul['2016년'] + CCTV_Seoul['2015년'] + \
                         CCTV_Seoul['2014년']) / CCTV_Seoul['2013년도 이전']  * 100
CCTV_Seoul.sort_values(by='최근증가율', ascending=False).head(5)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>구별</th>
      <th>소계</th>
      <th>2013년도 이전</th>
      <th>2014년</th>
      <th>2015년</th>
      <th>2016년</th>
      <th>최근증가율</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>22</th>
      <td>종로구</td>
      <td>1619</td>
      <td>464</td>
      <td>314</td>
      <td>211</td>
      <td>630</td>
      <td>248.922414</td>
    </tr>
    <tr>
      <th>9</th>
      <td>도봉구</td>
      <td>825</td>
      <td>238</td>
      <td>159</td>
      <td>42</td>
      <td>386</td>
      <td>246.638655</td>
    </tr>
    <tr>
      <th>12</th>
      <td>마포구</td>
      <td>980</td>
      <td>314</td>
      <td>118</td>
      <td>169</td>
      <td>379</td>
      <td>212.101911</td>
    </tr>
    <tr>
      <th>8</th>
      <td>노원구</td>
      <td>1566</td>
      <td>542</td>
      <td>57</td>
      <td>451</td>
      <td>516</td>
      <td>188.929889</td>
    </tr>
    <tr>
      <th>1</th>
      <td>강동구</td>
      <td>1010</td>
      <td>379</td>
      <td>99</td>
      <td>155</td>
      <td>377</td>
      <td>166.490765</td>
    </tr>
  </tbody>
</table>
</div>




```python
pop_Seoul.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>구별</th>
      <th>인구수</th>
      <th>한국인</th>
      <th>외국인</th>
      <th>고령자</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>합계</td>
      <td>10049607</td>
      <td>9765623</td>
      <td>283984</td>
      <td>1416131</td>
    </tr>
    <tr>
      <th>1</th>
      <td>종로구</td>
      <td>163026</td>
      <td>153065</td>
      <td>9961</td>
      <td>26742</td>
    </tr>
    <tr>
      <th>2</th>
      <td>중구</td>
      <td>135633</td>
      <td>125725</td>
      <td>9908</td>
      <td>22005</td>
    </tr>
    <tr>
      <th>3</th>
      <td>용산구</td>
      <td>245090</td>
      <td>228999</td>
      <td>16091</td>
      <td>37640</td>
    </tr>
    <tr>
      <th>4</th>
      <td>성동구</td>
      <td>316463</td>
      <td>308221</td>
      <td>8242</td>
      <td>42767</td>
    </tr>
  </tbody>
</table>
</div>




```python
pop_Seoul.drop([0], inplace=True) ## 0번 행을 통째로 드랍(삭제)
pop_Seoul.head
```




    <bound method NDFrame.head of       구별     인구수     한국인    외국인    고령자
    1    종로구  163026  153065   9961  26742
    2     중구  135633  125725   9908  22005
    3    용산구  245090  228999  16091  37640
    4    성동구  316463  308221   8242  42767
    5    광진구  371063  355559  15504  45619
    6   동대문구  364338  348052  16286  57165
    7    중랑구  408147  403209   4938  61830
    8    성북구  447687  435868  11819  67782
    9    강북구  322915  319164   3751  58196
    10   도봉구  341649  339413   2236  55964
    11   노원구  548160  543752   4408  77096
    12   은평구  487666  483197   4469  77420
    13  서대문구  323080  310313  12767  50456
    14   마포구  386359  375077  11282  50833
    15   양천구  468145  464185   3960  58045
    16   강서구  603611  596949   6662  79660
    17   구로구  438486  404497  33989  61801
    18   금천구  254021  233917  20104  35739
    19  영등포구  403600  367778  35822  55673
    20   동작구  409385  396203  13182  59479
    21   관악구  520040  501957  18083  72249
    22   서초구  438163  433951   4212  54751
    23   강남구  547453  542364   5089  67085
    24   송파구  673507  666635   6872  81364
    25   강동구  431920  427573   4347  58770>




```python
pop_Seoul['구별'].unique()     ##unique: 반복된 데이터는 하나로 나타내서 한번 이상 나타난 데이터를 확인
```




    array(['종로구', '중구', '용산구', '성동구', '광진구', '동대문구', '중랑구', '성북구', '강북구',
           '도봉구', '노원구', '은평구', '서대문구', '마포구', '양천구', '강서구', '구로구', '금천구',
           '영등포구', '동작구', '관악구', '서초구', '강남구', '송파구', '강동구'], dtype=object)




```python
pop_Seoul[pop_Seoul['구별'].isnull()]    ### NaN 값이 있는 행 확인, 확인되면 drop으로 삭제
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>구별</th>
      <th>인구수</th>
      <th>한국인</th>
      <th>외국인</th>
      <th>고령자</th>
    </tr>
  </thead>
  <tbody>
  </tbody>
</table>
</div>




```python
pop_Seoul.sort_values(by='인구수', ascending=False).head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>구별</th>
      <th>인구수</th>
      <th>한국인</th>
      <th>외국인</th>
      <th>고령자</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>24</th>
      <td>송파구</td>
      <td>673507</td>
      <td>666635</td>
      <td>6872</td>
      <td>81364</td>
    </tr>
    <tr>
      <th>16</th>
      <td>강서구</td>
      <td>603611</td>
      <td>596949</td>
      <td>6662</td>
      <td>79660</td>
    </tr>
    <tr>
      <th>11</th>
      <td>노원구</td>
      <td>548160</td>
      <td>543752</td>
      <td>4408</td>
      <td>77096</td>
    </tr>
    <tr>
      <th>23</th>
      <td>강남구</td>
      <td>547453</td>
      <td>542364</td>
      <td>5089</td>
      <td>67085</td>
    </tr>
    <tr>
      <th>21</th>
      <td>관악구</td>
      <td>520040</td>
      <td>501957</td>
      <td>18083</td>
      <td>72249</td>
    </tr>
  </tbody>
</table>
</div>




```python
pop_Seoul['외국인비율'] = pop_Seoul['외국인'] / pop_Seoul['인구수'] * 100   ## 어떤 열을 생성해서 데이터를 넣을 때 
pop_Seoul['고령자비율'] = pop_Seoul['고령자'] / pop_Seoul['인구수'] * 100
pop_Seoul.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>구별</th>
      <th>인구수</th>
      <th>한국인</th>
      <th>외국인</th>
      <th>고령자</th>
      <th>외국인비율</th>
      <th>고령자비율</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1</th>
      <td>종로구</td>
      <td>163026</td>
      <td>153065</td>
      <td>9961</td>
      <td>26742</td>
      <td>6.110068</td>
      <td>16.403518</td>
    </tr>
    <tr>
      <th>2</th>
      <td>중구</td>
      <td>135633</td>
      <td>125725</td>
      <td>9908</td>
      <td>22005</td>
      <td>7.305007</td>
      <td>16.223928</td>
    </tr>
    <tr>
      <th>3</th>
      <td>용산구</td>
      <td>245090</td>
      <td>228999</td>
      <td>16091</td>
      <td>37640</td>
      <td>6.565343</td>
      <td>15.357624</td>
    </tr>
    <tr>
      <th>4</th>
      <td>성동구</td>
      <td>316463</td>
      <td>308221</td>
      <td>8242</td>
      <td>42767</td>
      <td>2.604412</td>
      <td>13.514060</td>
    </tr>
    <tr>
      <th>5</th>
      <td>광진구</td>
      <td>371063</td>
      <td>355559</td>
      <td>15504</td>
      <td>45619</td>
      <td>4.178266</td>
      <td>12.294139</td>
    </tr>
  </tbody>
</table>
</div>




```python
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
```


```python
df1
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>A</th>
      <th>B</th>
      <th>C</th>
      <th>D</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>A0</td>
      <td>B0</td>
      <td>C0</td>
      <td>D0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>A1</td>
      <td>B1</td>
      <td>C1</td>
      <td>D1</td>
    </tr>
    <tr>
      <th>2</th>
      <td>A2</td>
      <td>B2</td>
      <td>C2</td>
      <td>D2</td>
    </tr>
    <tr>
      <th>3</th>
      <td>A3</td>
      <td>B3</td>
      <td>C3</td>
      <td>D3</td>
    </tr>
  </tbody>
</table>
</div>




```python
df2
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>A</th>
      <th>B</th>
      <th>C</th>
      <th>D</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>4</th>
      <td>A4</td>
      <td>B4</td>
      <td>C4</td>
      <td>D4</td>
    </tr>
    <tr>
      <th>5</th>
      <td>A5</td>
      <td>B5</td>
      <td>C5</td>
      <td>D5</td>
    </tr>
    <tr>
      <th>6</th>
      <td>A6</td>
      <td>B6</td>
      <td>C6</td>
      <td>D6</td>
    </tr>
    <tr>
      <th>7</th>
      <td>A7</td>
      <td>B7</td>
      <td>C7</td>
      <td>D7</td>
    </tr>
  </tbody>
</table>
</div>




```python
df3
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>A</th>
      <th>B</th>
      <th>C</th>
      <th>D</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>8</th>
      <td>A8</td>
      <td>B8</td>
      <td>C8</td>
      <td>D8</td>
    </tr>
    <tr>
      <th>9</th>
      <td>A9</td>
      <td>B9</td>
      <td>C9</td>
      <td>D9</td>
    </tr>
    <tr>
      <th>10</th>
      <td>A10</td>
      <td>B10</td>
      <td>C10</td>
      <td>D10</td>
    </tr>
    <tr>
      <th>11</th>
      <td>A11</td>
      <td>B11</td>
      <td>C11</td>
      <td>D11</td>
    </tr>
  </tbody>
</table>
</div>




```python
result = pd.concat([df1, df2, df3])           ## concat : 데이터를 단순히 열방향으로 합치기
result
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>A</th>
      <th>B</th>
      <th>C</th>
      <th>D</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>A0</td>
      <td>B0</td>
      <td>C0</td>
      <td>D0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>A1</td>
      <td>B1</td>
      <td>C1</td>
      <td>D1</td>
    </tr>
    <tr>
      <th>2</th>
      <td>A2</td>
      <td>B2</td>
      <td>C2</td>
      <td>D2</td>
    </tr>
    <tr>
      <th>3</th>
      <td>A3</td>
      <td>B3</td>
      <td>C3</td>
      <td>D3</td>
    </tr>
    <tr>
      <th>4</th>
      <td>A4</td>
      <td>B4</td>
      <td>C4</td>
      <td>D4</td>
    </tr>
    <tr>
      <th>5</th>
      <td>A5</td>
      <td>B5</td>
      <td>C5</td>
      <td>D5</td>
    </tr>
    <tr>
      <th>6</th>
      <td>A6</td>
      <td>B6</td>
      <td>C6</td>
      <td>D6</td>
    </tr>
    <tr>
      <th>7</th>
      <td>A7</td>
      <td>B7</td>
      <td>C7</td>
      <td>D7</td>
    </tr>
    <tr>
      <th>8</th>
      <td>A8</td>
      <td>B8</td>
      <td>C8</td>
      <td>D8</td>
    </tr>
    <tr>
      <th>9</th>
      <td>A9</td>
      <td>B9</td>
      <td>C9</td>
      <td>D9</td>
    </tr>
    <tr>
      <th>10</th>
      <td>A10</td>
      <td>B10</td>
      <td>C10</td>
      <td>D10</td>
    </tr>
    <tr>
      <th>11</th>
      <td>A11</td>
      <td>B11</td>
      <td>C11</td>
      <td>D11</td>
    </tr>
  </tbody>
</table>
</div>




```python
result = pd.concat([df1, df2, df3], keys = ['x','y','z'])   ### Keys : 이거로 합쳐진 것들을 구분, 다중 인덱스가 되어 levels을 형성함
result
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th></th>
      <th>A</th>
      <th>B</th>
      <th>C</th>
      <th>D</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th rowspan="4" valign="top">x</th>
      <th>0</th>
      <td>A0</td>
      <td>B0</td>
      <td>C0</td>
      <td>D0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>A1</td>
      <td>B1</td>
      <td>C1</td>
      <td>D1</td>
    </tr>
    <tr>
      <th>2</th>
      <td>A2</td>
      <td>B2</td>
      <td>C2</td>
      <td>D2</td>
    </tr>
    <tr>
      <th>3</th>
      <td>A3</td>
      <td>B3</td>
      <td>C3</td>
      <td>D3</td>
    </tr>
    <tr>
      <th rowspan="4" valign="top">y</th>
      <th>4</th>
      <td>A4</td>
      <td>B4</td>
      <td>C4</td>
      <td>D4</td>
    </tr>
    <tr>
      <th>5</th>
      <td>A5</td>
      <td>B5</td>
      <td>C5</td>
      <td>D5</td>
    </tr>
    <tr>
      <th>6</th>
      <td>A6</td>
      <td>B6</td>
      <td>C6</td>
      <td>D6</td>
    </tr>
    <tr>
      <th>7</th>
      <td>A7</td>
      <td>B7</td>
      <td>C7</td>
      <td>D7</td>
    </tr>
    <tr>
      <th rowspan="4" valign="top">z</th>
      <th>8</th>
      <td>A8</td>
      <td>B8</td>
      <td>C8</td>
      <td>D8</td>
    </tr>
    <tr>
      <th>9</th>
      <td>A9</td>
      <td>B9</td>
      <td>C9</td>
      <td>D9</td>
    </tr>
    <tr>
      <th>10</th>
      <td>A10</td>
      <td>B10</td>
      <td>C10</td>
      <td>D10</td>
    </tr>
    <tr>
      <th>11</th>
      <td>A11</td>
      <td>B11</td>
      <td>C11</td>
      <td>D11</td>
    </tr>
  </tbody>
</table>
</div>




```python
result.index
```




    MultiIndex(levels=[['x', 'y', 'z'], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]],
               labels=[[0, 0, 0, 0, 1, 1, 1, 1, 2, 2, 2, 2], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]])




```python
result.index.get_level_values(0)   ## 다중 인덱스 중 0번째 레벨의 인덱스들 
```




    Index(['x', 'x', 'x', 'x', 'y', 'y', 'y', 'y', 'z', 'z', 'z', 'z'], dtype='object')




```python
result.index.get_level_values(1)   ## 다중 인덱스 중 1 레벨의 인덱스들
```




    Int64Index([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], dtype='int64')




```python
df4 = pd.DataFrame({'B': ['B2', 'B3', 'B6', 'B7'], 
                    'D': ['D2', 'D3', 'D6', 'D7'],
                    'F': ['F2', 'F3', 'F6', 'F7']},
                   index=[2, 3, 6, 7])

result = pd.concat([df1, df4], axis=1)
```


```python
result   ## 결과를 보면 값을 가질 수 없는 곳에 NaN이 저장됨, 값을 가질 수 없는 곳이란 인덱스 기준으로 없는 곳에는 값이 없음
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>A</th>
      <th>B</th>
      <th>C</th>
      <th>D</th>
      <th>B</th>
      <th>D</th>
      <th>F</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>A0</td>
      <td>B0</td>
      <td>C0</td>
      <td>D0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1</th>
      <td>A1</td>
      <td>B1</td>
      <td>C1</td>
      <td>D1</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2</th>
      <td>A2</td>
      <td>B2</td>
      <td>C2</td>
      <td>D2</td>
      <td>B2</td>
      <td>D2</td>
      <td>F2</td>
    </tr>
    <tr>
      <th>3</th>
      <td>A3</td>
      <td>B3</td>
      <td>C3</td>
      <td>D3</td>
      <td>B3</td>
      <td>D3</td>
      <td>F3</td>
    </tr>
    <tr>
      <th>6</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>B6</td>
      <td>D6</td>
      <td>F6</td>
    </tr>
    <tr>
      <th>7</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>B7</td>
      <td>D7</td>
      <td>F7</td>
    </tr>
  </tbody>
</table>
</div>




```python
result = pd.concat([df1, df4], axis=1, join='inner')    ## 값이 없는 곳은 드랍하는 옵션이 join의 'inner'
result
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>A</th>
      <th>B</th>
      <th>C</th>
      <th>D</th>
      <th>B</th>
      <th>D</th>
      <th>F</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2</th>
      <td>A2</td>
      <td>B2</td>
      <td>C2</td>
      <td>D2</td>
      <td>B2</td>
      <td>D2</td>
      <td>F2</td>
    </tr>
    <tr>
      <th>3</th>
      <td>A3</td>
      <td>B3</td>
      <td>C3</td>
      <td>D3</td>
      <td>B3</td>
      <td>D3</td>
      <td>F3</td>
    </tr>
  </tbody>
</table>
</div>




```python
result = pd.concat([df1, df4], ignore_index=True)
result
```

    C:\Users\SunrokKwon\Anaconda3\lib\site-packages\ipykernel_launcher.py:1: FutureWarning: Sorting because non-concatenation axis is not aligned. A future version
    of pandas will change to not sort by default.
    
    To accept the future behavior, pass 'sort=False'.
    
    To retain the current behavior and silence the warning, pass 'sort=True'.
    
      """Entry point for launching an IPython kernel.
    




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>A</th>
      <th>B</th>
      <th>C</th>
      <th>D</th>
      <th>F</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>A0</td>
      <td>B0</td>
      <td>C0</td>
      <td>D0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1</th>
      <td>A1</td>
      <td>B1</td>
      <td>C1</td>
      <td>D1</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2</th>
      <td>A2</td>
      <td>B2</td>
      <td>C2</td>
      <td>D2</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>3</th>
      <td>A3</td>
      <td>B3</td>
      <td>C3</td>
      <td>D3</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>4</th>
      <td>NaN</td>
      <td>B2</td>
      <td>NaN</td>
      <td>D2</td>
      <td>F2</td>
    </tr>
    <tr>
      <th>5</th>
      <td>NaN</td>
      <td>B3</td>
      <td>NaN</td>
      <td>D3</td>
      <td>F3</td>
    </tr>
    <tr>
      <th>6</th>
      <td>NaN</td>
      <td>B6</td>
      <td>NaN</td>
      <td>D6</td>
      <td>F6</td>
    </tr>
    <tr>
      <th>7</th>
      <td>NaN</td>
      <td>B7</td>
      <td>NaN</td>
      <td>D7</td>
      <td>F7</td>
    </tr>
  </tbody>
</table>
</div>




```python
left = pd.DataFrame({'key': ['K0', 'K4', 'K2', 'K3'],
                     'A': ['A0', 'A1', 'A2', 'A3'],
                     'B': ['B0', 'B1', 'B2', 'B3']})

right = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3'],
                      'C': ['C0', 'C1', 'C2', 'C3'],
                      'D': ['D0', 'D1', 'D2', 'D3']})
```


```python
left
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>key</th>
      <th>A</th>
      <th>B</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>K0</td>
      <td>A0</td>
      <td>B0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>K4</td>
      <td>A1</td>
      <td>B1</td>
    </tr>
    <tr>
      <th>2</th>
      <td>K2</td>
      <td>A2</td>
      <td>B2</td>
    </tr>
    <tr>
      <th>3</th>
      <td>K3</td>
      <td>A3</td>
      <td>B3</td>
    </tr>
  </tbody>
</table>
</div>




```python
right
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>key</th>
      <th>C</th>
      <th>D</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>K0</td>
      <td>C0</td>
      <td>D0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>K1</td>
      <td>C1</td>
      <td>D1</td>
    </tr>
    <tr>
      <th>2</th>
      <td>K2</td>
      <td>C2</td>
      <td>D2</td>
    </tr>
    <tr>
      <th>3</th>
      <td>K3</td>
      <td>C3</td>
      <td>D3</td>
    </tr>
  </tbody>
</table>
</div>




```python
pd.merge(left, right, on='key')  ##공통된 key에 대해서만 합침
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>key</th>
      <th>A</th>
      <th>B</th>
      <th>C</th>
      <th>D</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>K0</td>
      <td>A0</td>
      <td>B0</td>
      <td>C0</td>
      <td>D0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>K2</td>
      <td>A2</td>
      <td>B2</td>
      <td>C2</td>
      <td>D2</td>
    </tr>
    <tr>
      <th>2</th>
      <td>K3</td>
      <td>A3</td>
      <td>B3</td>
      <td>C3</td>
      <td>D3</td>
    </tr>
  </tbody>
</table>
</div>




```python
pd.merge(left, right, how='left', on='key')  ## 합치는 두 데이터 중 하나만 기준으로 합칠 수도 있음. 
                                            ##이때 기준이 되는 데이터는 데이터가 다 나오고 안되는 데이터는 NaN 값이 나올 수도 있음
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>key</th>
      <th>A</th>
      <th>B</th>
      <th>C</th>
      <th>D</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>K0</td>
      <td>A0</td>
      <td>B0</td>
      <td>C0</td>
      <td>D0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>K4</td>
      <td>A1</td>
      <td>B1</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2</th>
      <td>K2</td>
      <td>A2</td>
      <td>B2</td>
      <td>C2</td>
      <td>D2</td>
    </tr>
    <tr>
      <th>3</th>
      <td>K3</td>
      <td>A3</td>
      <td>B3</td>
      <td>C3</td>
      <td>D3</td>
    </tr>
  </tbody>
</table>
</div>




```python
pd.merge(left, right, how='outer', on='key')   ## 그냥 있는대로 다 합침. 데이터가 NaN이건 아니건 다 합침 (합집합)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>key</th>
      <th>A</th>
      <th>B</th>
      <th>C</th>
      <th>D</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>K0</td>
      <td>A0</td>
      <td>B0</td>
      <td>C0</td>
      <td>D0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>K4</td>
      <td>A1</td>
      <td>B1</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2</th>
      <td>K2</td>
      <td>A2</td>
      <td>B2</td>
      <td>C2</td>
      <td>D2</td>
    </tr>
    <tr>
      <th>3</th>
      <td>K3</td>
      <td>A3</td>
      <td>B3</td>
      <td>C3</td>
      <td>D3</td>
    </tr>
    <tr>
      <th>4</th>
      <td>K1</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>C1</td>
      <td>D1</td>
    </tr>
  </tbody>
</table>
</div>




```python
pd.merge(left, right, how='inner', on='key')   ## 교집합 형태로 합침
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>key</th>
      <th>A</th>
      <th>B</th>
      <th>C</th>
      <th>D</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>K0</td>
      <td>A0</td>
      <td>B0</td>
      <td>C0</td>
      <td>D0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>K2</td>
      <td>A2</td>
      <td>B2</td>
      <td>C2</td>
      <td>D2</td>
    </tr>
    <tr>
      <th>2</th>
      <td>K3</td>
      <td>A3</td>
      <td>B3</td>
      <td>C3</td>
      <td>D3</td>
    </tr>
  </tbody>
</table>
</div>




```python
data_result = pd.merge(CCTV_Seoul, pop_Seoul, on='구별')  ##구별을 기준으로 합침
data_result.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>구별</th>
      <th>소계</th>
      <th>2013년도 이전</th>
      <th>2014년</th>
      <th>2015년</th>
      <th>2016년</th>
      <th>최근증가율</th>
      <th>인구수</th>
      <th>한국인</th>
      <th>외국인</th>
      <th>고령자</th>
      <th>외국인비율</th>
      <th>고령자비율</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>강남구</td>
      <td>3238</td>
      <td>1292</td>
      <td>430</td>
      <td>584</td>
      <td>932</td>
      <td>150.619195</td>
      <td>547453</td>
      <td>542364</td>
      <td>5089</td>
      <td>67085</td>
      <td>0.929578</td>
      <td>12.254020</td>
    </tr>
    <tr>
      <th>1</th>
      <td>강동구</td>
      <td>1010</td>
      <td>379</td>
      <td>99</td>
      <td>155</td>
      <td>377</td>
      <td>166.490765</td>
      <td>431920</td>
      <td>427573</td>
      <td>4347</td>
      <td>58770</td>
      <td>1.006436</td>
      <td>13.606686</td>
    </tr>
    <tr>
      <th>2</th>
      <td>강북구</td>
      <td>831</td>
      <td>369</td>
      <td>120</td>
      <td>138</td>
      <td>204</td>
      <td>125.203252</td>
      <td>322915</td>
      <td>319164</td>
      <td>3751</td>
      <td>58196</td>
      <td>1.161606</td>
      <td>18.022080</td>
    </tr>
    <tr>
      <th>3</th>
      <td>강서구</td>
      <td>911</td>
      <td>388</td>
      <td>258</td>
      <td>184</td>
      <td>81</td>
      <td>134.793814</td>
      <td>603611</td>
      <td>596949</td>
      <td>6662</td>
      <td>79660</td>
      <td>1.103691</td>
      <td>13.197241</td>
    </tr>
    <tr>
      <th>4</th>
      <td>관악구</td>
      <td>2109</td>
      <td>846</td>
      <td>260</td>
      <td>390</td>
      <td>613</td>
      <td>149.290780</td>
      <td>520040</td>
      <td>501957</td>
      <td>18083</td>
      <td>72249</td>
      <td>3.477233</td>
      <td>13.892970</td>
    </tr>
  </tbody>
</table>
</div>




```python
del data_result['2013년도 이전']
del data_result['2014년']
del data_result['2015년']
del data_result['2016년']
data_result.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>구별</th>
      <th>소계</th>
      <th>최근증가율</th>
      <th>인구수</th>
      <th>한국인</th>
      <th>외국인</th>
      <th>고령자</th>
      <th>외국인비율</th>
      <th>고령자비율</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>강남구</td>
      <td>3238</td>
      <td>150.619195</td>
      <td>547453</td>
      <td>542364</td>
      <td>5089</td>
      <td>67085</td>
      <td>0.929578</td>
      <td>12.254020</td>
    </tr>
    <tr>
      <th>1</th>
      <td>강동구</td>
      <td>1010</td>
      <td>166.490765</td>
      <td>431920</td>
      <td>427573</td>
      <td>4347</td>
      <td>58770</td>
      <td>1.006436</td>
      <td>13.606686</td>
    </tr>
    <tr>
      <th>2</th>
      <td>강북구</td>
      <td>831</td>
      <td>125.203252</td>
      <td>322915</td>
      <td>319164</td>
      <td>3751</td>
      <td>58196</td>
      <td>1.161606</td>
      <td>18.022080</td>
    </tr>
    <tr>
      <th>3</th>
      <td>강서구</td>
      <td>911</td>
      <td>134.793814</td>
      <td>603611</td>
      <td>596949</td>
      <td>6662</td>
      <td>79660</td>
      <td>1.103691</td>
      <td>13.197241</td>
    </tr>
    <tr>
      <th>4</th>
      <td>관악구</td>
      <td>2109</td>
      <td>149.290780</td>
      <td>520040</td>
      <td>501957</td>
      <td>18083</td>
      <td>72249</td>
      <td>3.477233</td>
      <td>13.892970</td>
    </tr>
  </tbody>
</table>
</div>




```python
data_result.set_index('구별', inplace=True)
data_result.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>소계</th>
      <th>최근증가율</th>
      <th>인구수</th>
      <th>한국인</th>
      <th>외국인</th>
      <th>고령자</th>
      <th>외국인비율</th>
      <th>고령자비율</th>
    </tr>
    <tr>
      <th>구별</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>강남구</th>
      <td>3238</td>
      <td>150.619195</td>
      <td>547453</td>
      <td>542364</td>
      <td>5089</td>
      <td>67085</td>
      <td>0.929578</td>
      <td>12.254020</td>
    </tr>
    <tr>
      <th>강동구</th>
      <td>1010</td>
      <td>166.490765</td>
      <td>431920</td>
      <td>427573</td>
      <td>4347</td>
      <td>58770</td>
      <td>1.006436</td>
      <td>13.606686</td>
    </tr>
    <tr>
      <th>강북구</th>
      <td>831</td>
      <td>125.203252</td>
      <td>322915</td>
      <td>319164</td>
      <td>3751</td>
      <td>58196</td>
      <td>1.161606</td>
      <td>18.022080</td>
    </tr>
    <tr>
      <th>강서구</th>
      <td>911</td>
      <td>134.793814</td>
      <td>603611</td>
      <td>596949</td>
      <td>6662</td>
      <td>79660</td>
      <td>1.103691</td>
      <td>13.197241</td>
    </tr>
    <tr>
      <th>관악구</th>
      <td>2109</td>
      <td>149.290780</td>
      <td>520040</td>
      <td>501957</td>
      <td>18083</td>
      <td>72249</td>
      <td>3.477233</td>
      <td>13.892970</td>
    </tr>
  </tbody>
</table>
</div>




```python
import scipy as sp
import numpy as np
```


```python
sp.corrcoef(data_result['고령자비율'],data_result['소계'])
```




    array([[ 1.        , -0.27474224],
           [-0.27474224,  1.        ]])




```python
sp.corrcoef(data_result['외국인비율'],data_result['소계'])
```




    array([[ 1.        , -0.05057013],
           [-0.05057013,  1.        ]])




```python
sp.corrcoef(data_result['인구수'],data_result['소계'])
```




    array([[1.        , 0.22152789],
           [0.22152789, 1.        ]])




```python
data_result.sort_values(by='소계', ascending=False).head(5)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>소계</th>
      <th>최근증가율</th>
      <th>인구수</th>
      <th>한국인</th>
      <th>외국인</th>
      <th>고령자</th>
      <th>외국인비율</th>
      <th>고령자비율</th>
    </tr>
    <tr>
      <th>구별</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>강남구</th>
      <td>3238</td>
      <td>150.619195</td>
      <td>547453</td>
      <td>542364</td>
      <td>5089</td>
      <td>67085</td>
      <td>0.929578</td>
      <td>12.254020</td>
    </tr>
    <tr>
      <th>양천구</th>
      <td>2482</td>
      <td>34.671731</td>
      <td>468145</td>
      <td>464185</td>
      <td>3960</td>
      <td>58045</td>
      <td>0.845892</td>
      <td>12.398936</td>
    </tr>
    <tr>
      <th>서초구</th>
      <td>2297</td>
      <td>63.371266</td>
      <td>438163</td>
      <td>433951</td>
      <td>4212</td>
      <td>54751</td>
      <td>0.961286</td>
      <td>12.495578</td>
    </tr>
    <tr>
      <th>관악구</th>
      <td>2109</td>
      <td>149.290780</td>
      <td>520040</td>
      <td>501957</td>
      <td>18083</td>
      <td>72249</td>
      <td>3.477233</td>
      <td>13.892970</td>
    </tr>
    <tr>
      <th>은평구</th>
      <td>2108</td>
      <td>85.237258</td>
      <td>487666</td>
      <td>483197</td>
      <td>4469</td>
      <td>77420</td>
      <td>0.916406</td>
      <td>15.875620</td>
    </tr>
  </tbody>
</table>
</div>




```python
data_result.sort_values(by='인구수', ascending=False).head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>소계</th>
      <th>최근증가율</th>
      <th>인구수</th>
      <th>한국인</th>
      <th>외국인</th>
      <th>고령자</th>
      <th>외국인비율</th>
      <th>고령자비율</th>
    </tr>
    <tr>
      <th>구별</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>송파구</th>
      <td>1081</td>
      <td>104.347826</td>
      <td>673507</td>
      <td>666635</td>
      <td>6872</td>
      <td>81364</td>
      <td>1.020331</td>
      <td>12.080647</td>
    </tr>
    <tr>
      <th>강서구</th>
      <td>911</td>
      <td>134.793814</td>
      <td>603611</td>
      <td>596949</td>
      <td>6662</td>
      <td>79660</td>
      <td>1.103691</td>
      <td>13.197241</td>
    </tr>
    <tr>
      <th>노원구</th>
      <td>1566</td>
      <td>188.929889</td>
      <td>548160</td>
      <td>543752</td>
      <td>4408</td>
      <td>77096</td>
      <td>0.804145</td>
      <td>14.064507</td>
    </tr>
    <tr>
      <th>강남구</th>
      <td>3238</td>
      <td>150.619195</td>
      <td>547453</td>
      <td>542364</td>
      <td>5089</td>
      <td>67085</td>
      <td>0.929578</td>
      <td>12.254020</td>
    </tr>
    <tr>
      <th>관악구</th>
      <td>2109</td>
      <td>149.290780</td>
      <td>520040</td>
      <td>501957</td>
      <td>18083</td>
      <td>72249</td>
      <td>3.477233</td>
      <td>13.892970</td>
    </tr>
  </tbody>
</table>
</div>




```python
import matplotlib.pyplot as plt
%matplotlib inline       
```


```python
plt.figure
plt.plot([1,2,3,4,5,6,7,8,9,8,7,6,5,4,3,2,1,0])
plt.show()
```


![png](output_75_0.png)



```python
t = sp.arange(0,12,0.01)
y = sp.sin(t)
```


```python
plt.figure(figsize=(10,6))
```




    <Figure size 720x432 with 0 Axes>




    <Figure size 720x432 with 0 Axes>



```python
import scipy as sp
t = sp.arange(0,12,0.01)   ## 0부터 12까지 0.01 간격으로 데이터 생성 : t는 단순히 값 하나가 아니라 1200개 정도의 값을 가진 일종의 배열 
y = sp.sin(t)              ## 이걸 반복문 없이 한 줄로 처리
```


```python
plt.figure(figsize=(10,6))
plt.plot(t,y)
plt.show()
```


![png](output_79_0.png)



```python
plt.figure(figsize=(10,6))
plt.plot(t,y)
plt.grid()
plt.xlabel('time')        ## 축에 라벨링 하기
plt.ylabel('Amplitude')
plt.title('Example of sinewave')   ## 그래프에 제목 붙이기
plt.show
```




    <function matplotlib.pyplot.show(*args, **kw)>




![png](output_80_1.png)



```python
plt.figure(figsize=(10,6))    ## 한 화면에 두 개 만들기
plt.plot(t,sp.sin(t))
plt.plot(t, sp.cos(t))
plt.grid()
plt.xlabel('time')
plt.ylabel('Amplitude')
plt.title('Example of sinewave')
plt.show
```




    <function matplotlib.pyplot.show(*args, **kw)>




![png](output_81_1.png)



```python
plt.figure(figsize=(10,6))    ## 한 화면에 두 개 만들기
plt.plot(t,sp.sin(t) , label='sin')
plt.plot(t, sp.cos(t), label = 'cos')
plt.grid()
plt.legend()         ## 범례 붙이는 옵션
plt.xlabel('time')
plt.ylabel('Amplitude')
plt.title('Example of sinewave')
plt.show
```




    <function matplotlib.pyplot.show(*args, **kw)>




![png](output_82_1.png)



```python
s1 = sp.random.normal(loc=0, scale=1, size=1000)
s2 = sp.random.normal(loc=5, scale=0.5, size=1000)
s3 = sp.random.normal(loc=10, scale=2, size=1000)
```


```python
plt.figure(figsize=(10,6))
plt.plot(s1, label='s1')
plt.plot(s2, label='s2')
plt.plot(s3, label='s3')
plt.legend()
plt.show()
```


![png](output_84_0.png)



```python
plt.figure(figsize=(10,6))
plt.boxplot((s1,s2,s3))
plt.show()
```


![png](output_85_0.png)



```python
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
```


```python
data_result.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>소계</th>
      <th>최근증가율</th>
      <th>인구수</th>
      <th>한국인</th>
      <th>외국인</th>
      <th>고령자</th>
      <th>외국인비율</th>
      <th>고령자비율</th>
    </tr>
    <tr>
      <th>구별</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>강남구</th>
      <td>3238</td>
      <td>150.619195</td>
      <td>547453</td>
      <td>542364</td>
      <td>5089</td>
      <td>67085</td>
      <td>0.929578</td>
      <td>12.254020</td>
    </tr>
    <tr>
      <th>강동구</th>
      <td>1010</td>
      <td>166.490765</td>
      <td>431920</td>
      <td>427573</td>
      <td>4347</td>
      <td>58770</td>
      <td>1.006436</td>
      <td>13.606686</td>
    </tr>
    <tr>
      <th>강북구</th>
      <td>831</td>
      <td>125.203252</td>
      <td>322915</td>
      <td>319164</td>
      <td>3751</td>
      <td>58196</td>
      <td>1.161606</td>
      <td>18.022080</td>
    </tr>
    <tr>
      <th>강서구</th>
      <td>911</td>
      <td>134.793814</td>
      <td>603611</td>
      <td>596949</td>
      <td>6662</td>
      <td>79660</td>
      <td>1.103691</td>
      <td>13.197241</td>
    </tr>
    <tr>
      <th>관악구</th>
      <td>2109</td>
      <td>149.290780</td>
      <td>520040</td>
      <td>501957</td>
      <td>18083</td>
      <td>72249</td>
      <td>3.477233</td>
      <td>13.892970</td>
    </tr>
  </tbody>
</table>
</div>




```python
data_result['소계'].plot(kind='barh', grid=True, figsize=(10,10))
plt.show()
```


![png](output_88_0.png)



```python
data_result['소계'].sort_values().plot(kind='barh', grid=True, figsize=(10,10))
plt.show()
```


![png](output_89_0.png)



```python
data_result['CCTV비율'] = data_result['소계'] / data_result['인구수'] * 100

data_result['CCTV비율'].sort_values().plot(kind='barh', 
                                         grid=True, figsize=(10,10))
plt.show()
```


![png](output_90_0.png)



```python
plt.figure(figsize=(6,6))
plt.scatter(data_result['인구수'], data_result['소계'], s=50)  ## s : 마커의 크기 옵션
plt.xlabel('인구수')
plt.ylabel('CCTV')
plt.grid()
plt.show()
```


![png](output_91_0.png)



```python
fp1 = sp.polyfit(data_result['인구수'], data_result['소계'], 1)
fp1
```




    array([1.07336946e-03, 1.08384235e+03])




```python
f1 = sp.poly1d(fp1)
fx = sp.linspace(100000, 700000, 100)
```


```python
plt.figure(figsize=(10,10))
plt.scatter(data_result['인구수'], data_result['소계'], s=50)
plt.plot(fx, f1(fx), ls='dashed', lw=3, color='g')    ## 위에서 생성한 polyfit 직선을 그려줌
plt.xlabel('인구수')
plt.ylabel('CCTV')
plt.grid()
plt.show()
```


![png](output_94_0.png)



```python
fp1 = sp.polyfit(data_result['인구수'], data_result['소계'], 1)

f1 = sp.poly1d(fp1)
fx = sp.linspace(100000,700000, 100)

data_result['오차'] = sp.absolute(data_result['소계'] - f1(data_result['인구수']))  ## sp에는 absolute가 절대값 기능

df_sort = data_result.sort_values(by='오차', ascending=False)

df_sort.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>소계</th>
      <th>최근증가율</th>
      <th>인구수</th>
      <th>한국인</th>
      <th>외국인</th>
      <th>고령자</th>
      <th>외국인비율</th>
      <th>고령자비율</th>
      <th>CCTV 비율</th>
      <th>CCTV비율</th>
      <th>오차</th>
    </tr>
    <tr>
      <th>구별</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>강남구</th>
      <td>3238</td>
      <td>150.619195</td>
      <td>547453</td>
      <td>542364</td>
      <td>5089</td>
      <td>67085</td>
      <td>0.929578</td>
      <td>12.254020</td>
      <td>0.591466</td>
      <td>0.591466</td>
      <td>1566.538319</td>
    </tr>
    <tr>
      <th>양천구</th>
      <td>2482</td>
      <td>34.671731</td>
      <td>468145</td>
      <td>464185</td>
      <td>3960</td>
      <td>58045</td>
      <td>0.845892</td>
      <td>12.398936</td>
      <td>0.530178</td>
      <td>0.530178</td>
      <td>895.665104</td>
    </tr>
    <tr>
      <th>강서구</th>
      <td>911</td>
      <td>134.793814</td>
      <td>603611</td>
      <td>596949</td>
      <td>6662</td>
      <td>79660</td>
      <td>1.103691</td>
      <td>13.197241</td>
      <td>0.150925</td>
      <td>0.150925</td>
      <td>820.739963</td>
    </tr>
    <tr>
      <th>용산구</th>
      <td>2096</td>
      <td>53.216374</td>
      <td>245090</td>
      <td>228999</td>
      <td>16091</td>
      <td>37640</td>
      <td>6.565343</td>
      <td>15.357624</td>
      <td>0.855196</td>
      <td>0.855196</td>
      <td>749.085528</td>
    </tr>
    <tr>
      <th>서초구</th>
      <td>2297</td>
      <td>63.371266</td>
      <td>438163</td>
      <td>433951</td>
      <td>4212</td>
      <td>54751</td>
      <td>0.961286</td>
      <td>12.495578</td>
      <td>0.524234</td>
      <td>0.524234</td>
      <td>742.846867</td>
    </tr>
  </tbody>
</table>
</div>




```python
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
```


![png](output_96_0.png)



```python
plt.figure(figsize=(14,10))
plt.scatter(data_result['인구수'], data_result['소계'],
           c=data_result['오차'], s=50)
plt.plot(fx, f1(fx), ls='dashed', lw=3, color='g')

    
plt.xlabel('인구수')
plt.ylabel('인구당비율')

plt.colorbar()
plt.grid()
plt.show()
```


![png](output_97_0.png)



```python

```
