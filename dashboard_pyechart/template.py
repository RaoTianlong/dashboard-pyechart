import base64

# get base64
def get64(path):
    if path:
        with open(path,'rb') as f:
            hh = base64.b64encode(f.read())
        return hh.decode()
    else:
        return ''

# create template
def gettp(temp,title,logo,bgd):
    if temp:
        raise ValueError('自定义模板请参照默认模板修改')
    else:
        return tp.format(title=title,bgd=get64(bgd),logo=get64(logo))

# default template
tp = """
<html>
<head>
       <script type="text/javascript" src="http://echarts.baidu.com/gallery/vendors/echarts/echarts.min.js"></script>
       <script type="text/javascript" src="http://echarts.baidu.com/gallery/vendors/echarts-gl/echarts-gl.min.js"></script>
       <script type="text/javascript" src="http://echarts.baidu.com/gallery/vendors/echarts-stat/ecStat.min.js"></script>
       <script type="text/javascript" src="http://echarts.baidu.com/gallery/vendors/echarts/extension/dataTool.min.js"></script>
       <script type="text/javascript" src="http://echarts.baidu.com/gallery/vendors/echarts/map/js/china.js"></script>
       <script type="text/javascript" src="http://echarts.baidu.com/gallery/vendors/echarts/map/js/world.js"></script>
       <script type="text/javascript" src="https://api.map.baidu.com/api?v=2.0&ak=ZUONbpqGBsYGXNIYHicvbAbM"></script>
       <script type="text/javascript" src="http://echarts.baidu.com/gallery/vendors/echarts/extension/bmap.min.js"></script>
       <script type="text/javascript" src="http://echarts.baidu.com/gallery/vendors/simplex.js"></script>
       <link rel="stylesheet" type="text/css" href="css/default_style.css" />
       <title>{title}</title>
</head>
 <body style="background-image: url('data:image/png;base64,{bgd}')">
  <div id = "dashhead" name = "dashhead">
  <h1 id = "tt" name = "tt">{title}</h1>
  <img id = "logo" name = "logo" src="data:image/png;base64,{logo}" />
  </div>
  <div id="chart">
  </div>
 </body>
</html>
"""


