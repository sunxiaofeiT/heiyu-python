# python 3.6.x
# author: sunpengfei
# desc: python adb for 黑域

import os

devices = "adb devices"
text = "adb -d shell sh /data/data/me.piebridge.brevent/brevent.sh"

devices_num = os.popen(devices).read()
if "successful" in devices_num:
	print("连接成功")
print(devices_num)

result = os.popen(text).read()
if "error" in result:
	print("失败")
print(result)