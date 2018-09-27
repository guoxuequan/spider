#/ -*- coding:UTF-8 -*-
# 数据可视化分析
# 作者: Charles
# 公众号: Charles的皮卡丘
import os
import json
from pyecharts import Bar
from pyecharts import Pie
from pyecharts import Funnel
from pyecharts import Scatter


# 柱状图(2维)
def DrawBar(title, data, savepath='./results'):
	if not os.path.exists(savepath):
		os.mkdir(savepath)
	bar = Bar(title)
	attrs = [i for i, j in data.items()]
	values = [j for i, j in data.items()]
	bar.add('', attrs, values, mark_point=["min", "max"])
	bar.render(os.path.join(savepath, '%s.html' % title))


# 饼图
def DrawPie(title, data, savepath='./results'):
	if not os.path.exists(savepath):
		os.mkdir(savepath)
	pie = Pie(title, title_pos='center')
	attrs = [i for i, j in data.items()]
	values = [j for i, j in data.items()]
	pie.add('', attrs, values, is_label_show=True, radius=[30, 50], rosetype="radius", legend_pos="left", legend_orient="vertical")
	pie.render(os.path.join(savepath, '%s.html' % title))


# 漏斗图
def DrawFunnel(title, data, savepath='./results'):
	if not os.path.exists(savepath):
		os.mkdir(savepath)
	funnel = Funnel(title, title_pos='center')
	attrs = [i for i, j in data.items()]
	values = [j for i, j in data.items()]
	funnel.add("", attrs, values, is_label_show=True, label_pos="inside", label_text_color="#fff", legend_pos="left", legend_orient="vertical")
	funnel.render(os.path.join(savepath, '%s.html' % title))


# 散点图
def DrawScatter(title, data, savepath='./results'):
	if not os.path.exists(savepath):
		os.mkdir(savepath)
	scatter = Scatter(title)
	attrs = [i for i, j in data.items()]
	values = [j for i, j in data.items()]
	scatter.add('', attrs, values, is_visualmap=True)
	scatter.render(os.path.join(savepath, '%s.html' % title))


if __name__ == '__main__':
	with open('anjuke.json', 'r') as f:
		data = json.loads(f.read())
	'''
	prices = {'0到2000/月': 0, '2000到4000/月': 0, '4000到6000/月': 0, '6000到8000/月': 0, '8000到10000/月': 0, '大于10000/月': 0}
	for d in data:
		price = int(d.get('price'))
		if price in range(0, 2000):
			prices['0到2000/月'] += 1
		elif price in range(2000, 4000):
			prices['2000到4000/月'] += 1
		elif price in range(4000, 6000):
			prices['4000到6000/月'] += 1
		elif price in range(6000, 8000):
			prices['6000到8000/月'] += 1
		elif price in range(8000, 10000):
			prices['8000到10000/月'] += 1
		else:
			prices['大于10000/月'] += 1
	DrawBar(title='上海租房月租金分布柱状图', data=prices, savepath='./results')
	DrawPie(title='上海租房月租金分布饼图', data=prices, savepath='./results')
	'''
	'''
	prices_avg = {'0到50/月': 0, '50到100/月': 0, '100到150/月': 0, '150到200/月': 0, '大于200/月': 0}
	for d in data:
		price = int(float(d.get('price')) / float(d.get('area')))
		if price in range(0, 50):
			prices_avg['0到50/月'] += 1
		elif price in range(50, 100):
			prices_avg['50到100/月'] += 1
		elif price in range(100, 150):
			prices_avg['100到150/月'] += 1
		elif price in range(150, 200):
			prices_avg['150到200/月'] += 1
		else:
			prices_avg['大于200/月'] += 1
	DrawPie(title='上海租房(单位面积)月租金分布饼图', data=prices_avg, savepath='./results')
	'''
	'''
	towards_dict = {}
	for d in data:
		towards = d.get('towards')
		if towards in towards_dict:
			towards_dict[towards] += 1
		else:
			towards_dict[towards] = 1
	DrawFunnel(title='上海出租住房朝向漏斗图', data=towards_dict, savepath='./results')
	'''
	'''
	building_type_dict = {}
	for d in data:
		building_type = d.get('building_type')
		if building_type in building_type_dict:
			building_type_dict[building_type] += 1
		else:
			building_type_dict[building_type] = 1
	DrawBar(title='上海出租住房类型柱状图', data=building_type_dict, savepath='./results')
	'''
