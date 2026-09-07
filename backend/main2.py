from http.server import BaseHTTPRequestHandler, HTTPServer
import json

profile = {
    "heroTitle": "关于我",
    "heroSubtitle": "项目，创意，灵感，心得，我的作品",
}

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):  # 请求行里的方法——方法是GET的请求，归这个函数管
        if self.path == "/api/profile":  # 请求行里的路径——判断对方要访问哪个资源
            self.send_response(200) # 响应的状态行——回一个200
            self.send_header("Content-Type", "application/json") # 响应头——一行一条，这里只写了Content-Type这一条
            self.end_headers() # 空行——“头写完了”，头和体的分界线
            body = json.dumps(profile, ensure_ascii=False)  # ensure_ascii=False：让中文原样输出
            self.wfile.write(body.encode("utf-8")) # 响应体——我们的 JSON（encode是因为网络上传输的是字节，文本要先编码）
        else:
            self.send_response(404) # 状态码404——没找到。模块4时是Nginx替我们回，现在轮到我们自己回
            self.end_headers()

print("后端已启动：http://localhost:8000/api/profile")
HTTPServer(("", 8000), Handler).serve_forever() # 指定了http服务在8000端口上启动