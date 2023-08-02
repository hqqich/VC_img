from wsgiref.simple_server import make_server
#导入simple_server模块

#定义一个application，遵循wsgi协议；
def app(env, start_response):  #服务器接收到的客户端请求都会存储在env中，再传入到app进行处理，处理后再返回
    start_response("200 ok",[("Content-Type","text/plain")])
    return [b'hello'] #swgi协议规定必须返回bety


#实例化一个服务器设置ip为本机，端口为5000，执行程序为上面的app
server = make_server("", 5000, app)
#开启一个服务器，默认0.5秒轮询，接收客户端请求
server.serve_forever()
