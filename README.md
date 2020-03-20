## python requests --> ctrip

	可接入代理ip，存储至Redis数据库，通过YAML配置文件配置需求


	QQ：1586616064
	Author：gdream126.com

--------------



##### 运行环境

	python >= 3.8.0
	
	pyyaml==5.3
	redis==3.4.1
	xpinyin==0.5.6
	requests==2.22.0
	useragentxxc==1.1.0
        python-dateutil==2.8.1

##### 启动工程

	第一步：
		打开并运行"build.py"文件
	
	第二步：
		打开并运行"main.py"文件
		
	注意事项：
		1. 有些部分使用了python3.8最新特性-赋值表达式
		2. build.py是用来安装依赖，而main.py是项目入口
		3. 批量操作，请依照config.yaml文件里的注释来修改此文件
		4. 作者手里没有充足的ip，实际使用里异步协程将会没有意义，所以目前使用的是同步请求库
