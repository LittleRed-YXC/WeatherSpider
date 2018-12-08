# WeatherSpider
1. #### 项目概要
   - 按市、区/县地域维度，抓取中国天气网数据
   - 示例  ：http://www.weather.com.cn/weather/101071207.shtml
   
   ![today](https://github.com/LittleRed-YXC/WeatherSpider/blob/master/images/today.png) 
   
   ![days](https://github.com/LittleRed-YXC/WeatherSpider/blob/master/images/days.png) 
   
   ![hours](https://github.com/LittleRed-YXC/WeatherSpider/blob/master/images/hours.png) 
   
   ![indexs](https://github.com/LittleRed-YXC/WeatherSpider/blob/master/images/indexs.png) 
   
2. #### 安装依赖 
   使用anaconda/python3.X对应的包管理器conda/pip（建议虚拟环境下）安装requirements.txt文件里的依赖
3. #### 跑数据 
   ```scrapy runspider weather_spider.py -s FEED_FORMAT="jsonlines" -s FEED_EXPORT_ENCODING="utf-8" -s FEED_URI="file:///tmp/%(site)s"```
4. #### 查看数据
   - 数据路径 
      - unix-like： /tmp/www.weather.com.cn
      - windows： D:\tmp\www.weather.com.cn (D盘还是C盘等其它盘，取决你项目所在盘)
      - mac： 没有机子来测
   - 统计&信息
      - 统计：包含市、区/县，共计3280个城市单元的天气数据
      - 信息：
         - 当天天气详情
         - 6天天气预测
         - 当天天气走势图数据
         - 生活指数
   - 展示&说明
   ```
   [
   {
       "location": "上海-杨浦", # 地理位置信息
       "pub_time": "2018-12-08 07:30:00", # 天气发布时间
       "from_url": "http://www.weather.com.cn/weather/101021700.shtml", # 数据种子url
       "craw_time": "2018-12-08 10:22:25", # 抓取时间
       "today": { # 今天天气详情
           "weather": "小雨转雨夹雪", # 天气
           "temperature": "2~6℃", # 温度
           "wind_direction": "北风", # 风向
           "wind_level": "3-4级转<3级" # 风级
       },
       "days": [ # 未来6天天气简报
           {
               "weather": "小雨",
               "temperature": "5~7℃"
           },
           {
               "weather": "小雨转中雨",
               "temperature": "6~11℃"
           },
           {
               "weather": "小雨转多云",
               "temperature": "2~10℃"
           },
           {
               "weather": "多云转阴",
               "temperature": "2~7℃"
           },
           {
               "weather": "多云",
               "temperature": "5~9℃"
           },
           {
               "weather": "多云转小雨",
               "temperature": "4~12℃"
           }
       ],
       "hours": [ # 当天天气走势图数据
           {
               "time": "08日08时",
               "weather": "小雨",
               "temperature": "3℃",
               "wind_direction": "北风",
               "wind_level": "3-4级"
           },
           {
               "time": "08日11时",
               "weather": "小雨",
               "temperature": "5℃",
               "wind_direction": "北风",
               "wind_level": "3-4级"
           },
           {
               "time": "08日14时",
               "weather": "小雨",
               "temperature": "5℃",
               "wind_direction": "北风",
               "wind_level": "3-4级"
           },
           {
               "time": "08日17时",
               "weather": "小雨",
               "temperature": "4℃",
               "wind_direction": "北风",
               "wind_level": "3-4级"
           },
           {
               "time": "08日20时",
               "weather": "小雨",
               "temperature": "3℃",
               "wind_direction": "北风",
               "wind_level": "3-4级"
           },
           {
               "time": "08日23时",
               "weather": "雨夹雪",
               "temperature": "2℃",
               "wind_direction": "北风",
               "wind_level": "<3级"
           },
           {
               "time": "09日02时",
               "weather": "雨夹雪",
               "temperature": "2℃",
               "wind_direction": "北风",
               "wind_level": "<3级"
           },
           {
               "time": "09日05时",
               "weather": "雨夹雪",
               "temperature": "2℃",
               "wind_direction": "北风",
               "wind_level": "<3级"
           },
           {
               "time": "09日08时",
               "weather": "雨夹雪",
               "temperature": "2℃",
               "wind_direction": "北风",
               "wind_level": "<3级"
           }
       ],
       "indexs": [ # 生活指数数据
           {
               "title": "紫外线指数", # 项目标题
               "advice": "辐射弱，涂擦SPF8-12防晒护肤品。", # 建议
               "level": "最弱" # 级别
           },
           {
               "title": "减肥指数",
               "advice": "风雨交加特别冷，适当偷懒低强度运动吧。",
               "level": "1星"
           },
           {
               "title": "健臻·血糖指数",
               "advice": "血糖较易波动，注意监测。",
               "level": "较易波动"
           },
           {
               "title": "穿衣指数",
               "advice": "建议着棉衣加羊毛衫等冬季服装。",
               "level": "冷"
           },
           {
               "title": "洗车指数",
               "advice": "有雨，雨水和泥水会弄脏爱车。",
               "level": "不宜"
           },
           {
               "title": "空气污染扩散指数",
               "advice": "气象条件有利于空气污染物扩散。",
               "level": "良"
           }
       ]
   },
   {
       "location": "香港-新界",
       "pub_time": "2018-12-08 07:30:00",
       "from_url": "http://www.weather.com.cn/weather/101320103.shtml",
       "craw_time": "2018-12-08 10:22:25",
       "today": {
           "weather": "阴",
           "temperature": "15~19℃",
           "wind_direction": "无持续风向转北风",
           "wind_level": "<3级转3-4级"
       },
       "days": [
           {
               "weather": "阴转小雨",
               "temperature": "14~18℃"
           },
           {
               "weather": "阴转多云",
               "temperature": "14~21℃"
           },
           {
               "weather": "多云转晴",
               "temperature": "12~17℃"
           },
           {
               "weather": "晴",
               "temperature": "14~16℃"
           },
           {
               "weather": "晴转多云",
               "temperature": "15~18℃"
           },
           {
               "weather": "多云转阴",
               "temperature": "17~19℃"
           }
       ],
       "hours": [
           {
               "time": "08日08时",
               "weather": "阴",
               "temperature": "15℃",
               "wind_direction": "无持续风向",
               "wind_level": "<3级"
           },
           {
               "time": "08日11时",
               "weather": "阴",
               "temperature": "17℃",
               "wind_direction": "无持续风向",
               "wind_level": "<3级"
           },
           {
               "time": "08日14时",
               "weather": "阴",
               "temperature": "19℃",
               "wind_direction": "无持续风向",
               "wind_level": "<3级"
           },
           {
               "time": "08日17时",
               "weather": "阴",
               "temperature": "16℃",
               "wind_direction": "无持续风向",
               "wind_level": "<3级"
           },
           {
               "time": "08日20时",
               "weather": "阴",
               "temperature": "17℃",
               "wind_direction": "无持续风向",
               "wind_level": "<3级"
           },
           {
               "time": "08日23时",
               "weather": "阴",
               "temperature": "17℃",
               "wind_direction": "北风",
               "wind_level": "3-4级"
           },
           {
               "time": "09日02时",
               "weather": "阴",
               "temperature": "17℃",
               "wind_direction": "北风",
               "wind_level": "3-4级"
           },
           {
               "time": "09日05时",
               "weather": "阴",
               "temperature": "15℃",
               "wind_direction": "北风",
               "wind_level": "3-4级"
           },
           {
               "time": "09日08时",
               "weather": "阴",
               "temperature": "15℃",
               "wind_direction": "北风",
               "wind_level": "3-4级"
           }
       ],
       "indexs": [
           {
               "title": "紫外线指数",
               "advice": "辐射弱，涂擦SPF8-12防晒护肤品。",
               "level": "最弱"
           },
           {
               "title": "减肥指数",
               "advice": "天气较舒适，减肥正当时。",
               "level": "5星"
           },
           {
               "title": "健臻·血糖指数",
               "advice": "天气条件好，血糖不易波动，可适时进行户外锻炼。",
               "level": "不易波动"
           },
           {
               "title": "穿衣指数",
               "advice": "建议穿薄外套或牛仔裤等服装。",
               "level": "较舒适"
           },
           {
               "title": "洗车指数",
               "advice": "无雨且风力较小，易保持清洁度。",
               "level": "较适宜"
           },
           {
               "title": "空气污染扩散指数",
               "advice": "气象条件较不利于空气污染物扩散。。",
               "level": "较差"
           }
       ]
   },
   ...# 省略了其它城市信息
   ]
   ```
5. #### TODO
    - docker deployment
    - restful api
