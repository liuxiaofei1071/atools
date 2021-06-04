import websocket
import time

try:
    import thread
except ImportError:
    import _thread as thread




class WSClient:
    '''
    websocket客户端
    根据接收消息分发执行流程
    返回执行结果
    '''

    def __init__(self, ws_url):
        self.ws_url = ws_url

    def run(self):

        self.ws = websocket.WebSocketApp(
            self.ws_url,
            on_message=self.on_message,
            on_error=self.on_error,
            on_close=self.on_close,
            on_open=self.on_open,
        )
        self.ws.run_forever(ping_interval=10)

    def on_open(self):
        def run():
            while True:
                time.sleep(5)
                self.ws.send(f"sno：{'007'}；send my sweet  heartbeat!")

        def run1():
            while True:
                time.sleep(5)
                self.ws.send(f"sno：{'008'}；send my sweet  heartbeat!")

        thread.start_new_thread(run, ())
        thread.start_new_thread(run1, ())

    def on_message(self, message):
        print(f"ws:{self.ws}收到 {self.ws_url} 消息：{message}")

    def on_error(self, error):
        print(f'ws：{self.ws} 连接失败，原因为{error}')

    def on_close(self):
        print(f'ws:{self.ws} 连接关闭')
        self.on_open()


if __name__ == "__main__":
    ws_url = "ws://127.0.0.1:9000/ws/user333"
    ws_client = WSClient(ws_url)
    ws_client.run()
