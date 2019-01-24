from . import template as tp
from . import css
from bs4 import BeautifulSoup as bs
import os

class Dashboard():
    def __init__(self,title='DashBoard',logo_img='',background_img='',template=None):
        self.title = title
        self._root = bs(tp.gettp(template,title,logo_img,background_img))
        self.__jsdv = bs('<div></div>').div
        os.makedirs(title,exist_ok=True)
        os.makedirs(title+'/css',exist_ok=True)
        os.makedirs(title+'/js',exist_ok=True)
        with open(title+'/css/default_style.css','w') as f: f.write(css.dcss)
        
    def save(self):
        self._root.body.append(self.__jsdv)
        with open(self.title+'/'+self.title+'.html','w',encoding='utf8') as f: #不加encoding会有格式问题
            f.write(str(self._root))
        return 'Save as '+os.getcwd()+'/'+self.title
    
    def add_chart(self,chart,note=None):
        dv = bs('<div></div>').div
        dv['class'] = 'dvchart'
        sp = bs(chart.render_embed(),'lxml')
        idd = sp.div['id']
        dv.append(sp.div)
        if note : dv.append(bs('<p>'+note+'</p>').p)
        self._root.find_all(id='chart')[0].append(dv)
        with open(self.title+'/js/'+idd+'.js','w') as f: f.write(sp.script.text)
        self.__jsdv.append(bs('<script type="text/javascript" src="js/{0}.js"></script>'.format(idd)).script)
        return 'success'
        





