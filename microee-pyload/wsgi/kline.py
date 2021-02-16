
import random;
import datetime;
import json;
from matplotlib import pyplot as plt
from mplfinance.original_flavor import candlestick_ohlc
from matplotlib.pylab import date2num;

# https://www.programmersought.com/article/17884763118/
start="2020-1-1"
data=[]
for i in range(31):
    random_data=[random.randint(2000,2500) for _ in range(4)]
    sorted_data=sorted(random_data)
    day=date2num(datetime.datetime.strptime(start,'%Y-%m-%d'))
    if i==0:
        one=(day,sorted_data[1],sorted_data[3],sorted_data[0],sorted_data[2]) if random.random()>0.5 else (day,sorted_data[2],sorted_data[3],sorted_data[0],sorted_data[1])
    else:
        one=(day+i,sorted_data[1],sorted_data[3],sorted_data[0],sorted_data[2]) if random.random()>0.5 else (day+i,sorted_data[2],sorted_data[3],sorted_data[0],sorted_data[1])
    data.append(one)

print(json.dumps(data));


fig,ax=plt.subplots(facecolor="white",figsize=(12,8))
fig.subplots_adjust(bottom=0.1)
ax.xaxis_date()
plt.xticks(rotation=30)
plt.title('K-line')
plt.xlabel('2020')
# plt.ylabel('price')
candlestick_ohlc(ax,data,width=0.5,colorup='r',colordown='green')
plt.grid(True);
plt.savefig('/Users/keesh/Desktop/foo.png')
