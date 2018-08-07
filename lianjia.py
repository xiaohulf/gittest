from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

area={"dongcheng":"东城","xicheng":"西城","chaoyang":"朝阳","haidian":"海淀",
      "fengtai":"丰台","shijingshan":"石景山","tongzhou":"通州","changping":"昌平",
      "daxing":"大兴","yizhuangkaifaqu":"亦庄开发区","shunyi":"顺义","fangshan":"房山",
      "mentougou":"门头沟","pinggu":"平谷","huairou":"怀柔","miyun":"密云",
      "yanqing":"延庆","yanjiao":"燕郊"}
print(area)
