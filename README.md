# 作用
使用matrix，将需要记录的信息自动新增到obsidian里面；
要求obsidian使用 Self-hosted LiveSync进行双向同步；
程序会根据你发送给matrix机器人的信息自动记录到obsidian LiveSync的数据库中；
LiveSync会自动同步到obsidian对应的笔记中。

# 使用说明
```
git clone https://github.com/vvxu/matrix-obsidian.git
cd matrix-obsidian
```
先把参数样本文件复制一下
```
cp config.py.sample config.py
```
填入对应的参数
```
python main.py
```