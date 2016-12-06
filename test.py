import comm
import API
import json
reData={"pageDetail":"<li class=\"list-item fst-li\" data-from=\"\"> \n <div class=\"item-img\"> \n  <img src=\"http://a.pic1.ajkimg.com/display/hj/867c7afbf6d38514e69681065eb4eb3c/240x180m.jpg?t=1\" width=\"180\" height=\"135\"> \n </div> \n <div class=\"house-details\"> \n  <div class=\"house-title\"> \n   <a data-from=\"\" data-company=\"\" title=\"东和时代，滨江核心区块，精装修酒店式公寓，送家具家电\" href=\"http://hangzhou.anjuke.com/prop/view/G43687?from=esf_list_skfy&amp;position=1&amp;now_time=1476171053\" target=\"_blank\" class=\"houseListTitle \"> 东和时代，滨江核心区块，精装修酒店式公寓，送家具家电</a> \n   <i class=\"icon-sk\" title=\"真实在售、真实图片、真实价格\"></i> \n  </div> \n  <div class=\"details-item\"> \n   <span>52平方米</span>\n   <em>|</em>\n   <span>1室1厅</span>\n   <em>|</em>\n   <span>18269元/m²</span>\n   <em>|</em>\n   <span>9/30层</span> \n  </div> \n  <div class=\"details-item\"> \n   <span class=\"comm-address\" title=\"东和时代&nbsp;&nbsp;[滨江-长河 滨盛路(滨盛路与江晖路交叉口)]\"> 东和时代&nbsp;&nbsp; [滨江-长河&nbsp;滨盛路(滨盛路与江晖路交叉口)] </span> \n  </div> \n  <div class=\"details-item details-bottom\"> \n   <span class=\"broker-name\">认证房</span> \n  </div> \n </div> \n <!-- price --> \n <div class=\"pro-price\"> \n  <span class=\"price-det\"> <strong>95</strong>万 </span> \n </div> </li>"}

reData = json.dumps(reData)
print(reData)
dictHandler = comm.DictHandler()

Page = API.Page
page = Page()
page.setH("==11111 test==", 3)
page.setMethod('post')
page.setScribe('告警策略列表')
page.setResEx(reData)
page.setResParams(reData)
data = page.getPage()
f = open('e:/api/test.md', 'w',encoding='utf-8')
f.write(data)
f.close()
print(data)
