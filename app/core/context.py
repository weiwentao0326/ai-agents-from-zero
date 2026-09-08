from contextvars import ContextVar
# contextvars 是异步环境（FastAPI/asyncio）下的上下文存储。
# 作用：每个协程拥有自己独立的变量副本，协程之间互不干扰。
# 定义一个上下文变量
request_id_ctx_var = ContextVar("request_id", default="1")

