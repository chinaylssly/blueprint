# _*_ coding:utf-8 _*_
import random
import os

def get_filename():

	name=raw_input(u'请输入文件名（不输入文件名则使用默认文件名）：'.encode('gbk'))
	if name:

		if u'.' in name:
			##如果文件存在扩展名，则不生成py文件
			filename=name
		else:
			filename=u'%s.py'%name
	else:

		r=random.randint(1,10)
		filename='test_%s.py'%str(r)
	print u'准备创建的文件名为：%s'%filename
	return filename

def run():
	str=u'# _*_ coding:utf-8 _*_ '
	filename=get_filename()
	if not  os.path.exists(filename):
		
		with open(filename,'wb')as f:

			f.write(str)
			print u'成功创建新文件:%s'%(filename)

		return True
	else:
		print u'文件%s已存在'%filename
		return False


def main():
	#循环
	flag=run()
	while not flag:
		flag=run()

global count
count=0

def test():
	#递归

	str=u'# _*_ coding:utf-8 _*_ '
	filename=get_filename()
	if not os.path.exists(filename):
		
		with open(filename,'wb')as f:

			f.write(str)
			print u'成功创建新文件:%s'%(filename)

		
	else:
		print u'文件%s已存在'%filename
		global count
		count=count+1
		if count<=10:
			test()
			
			#避免递归溢出，加入终止条件
		else:
			print u'递归溢出，自动终止'


if __name__ =='__main__':

	# main()
	test()
	pass