# 需求：实现员工管理模块的登录
# 导包
import requests

# 发送IHRM登录的接口请求
response = requests.post(url="http://ihrm-test.itheima.net/api/sys/login",
                         json={"mobile": "13800000002", "password": "123456"},
                         headers={"Content-Type": "application/json"})
# 查看登录的结果
print("登录的结果为：", response.json())

# 获取登录返回的令牌
token = "Bearer " + response.json().get("data")
print("提取的令牌为：",token)
# 发送添加员工接口
headers = {"Content-Type":"application/json","Authorization":token}     # 添加员工的请求头
response = requests.post(url="http://ihrm-test.itheima.net" + "/api/sys/user",
                         json={
                                "username":"尼古拉斯5",
                                "mobile":"138765375465",
                                "timeOfEntry":"2020-05-05",
                                "formOfEmployment":1,
                                "departmentName":"测试部",
                                "departmentId":"1063678149528784896",
                                "correctionTime":"2020-05-19T16:00:00.000Z"
                                },
                         headers = headers)
# 打印添加员工系接口
print("添加员工的接口返回数据为：",response.json())
# 提取添加员工接口返回的员工id
emp_id = response.json().get("data").get("id")
print("提取的员工id为：",emp_id)


# 拼接查询员工接口的URL
query_url = "http://ihrm-test.itheima.net" +  "/api/sys/user" + "/" + emp_id
# 发送查询员工接口的请求
response = requests.get(url=query_url, headers=headers)
# 打印添加员工的结果
print("查询员工的结果为：",response.json())


# 拼接修改员工接口的URL
modify_url = "http://ihrm-test.itheima.net" +  "/api/sys/user" + "/" + emp_id
# 发送修改员工接口的请求
response = requests.put(url=modify_url,json={"username":"牛顿"},headers=headers)
# 打印修改员工的结果
print("修改员工的结果为：",response.json())

# 拼接删除员工的URL
delete_url = "http://ihrm-test.itheima.net" +  "/api/sys/user" + "/" + emp_id
# 发送删除员工的接口请求
response = requests.delete(url=delete_url,headers=headers)
# 打印删除员工的结果
print("删除员工的结果为：",response.json())

