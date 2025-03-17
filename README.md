# MCP Send Email 项目总结

## 技术选型

### 后端技术栈
- Python 3.8+
- FastAPI 框架
- Gmail API (OAuth 2.0)
- Google API Python Client
- Uvicorn ASGI服务器

### 前端技术栈
- React/TypeScript (mcp-client)
- Modern CSS

### 工具和依赖
- google-api-python-client：Gmail API 交互
- google-auth-oauthlib：OAuth 2.0 认证
- fastapi：Web API 框架
- uvicorn：ASGI 服务器
- pydantic：数据验证
- python-dotenv：环境变量管理

## 系统架构

项目采用两种不同的架构模式运行：

### 1. 传统Web服务架构
```
[FastAPI Backend] <-> [Gmail API]
       ↑
[HTTP Clients]
```
- 使用 Uvicorn 运行 FastAPI 服务
- RESTful API 接口
- OAuth 2.0 认证流程
- 标准 HTTP 通信

### 2. MCP Client-Server架构
```
[MCP Client] <-> [MCP Server] <-> [Gmail API]
```
- 自定义协议通信
- 支持实时命令执行
- 更灵活的交互模式
- 支持扩展功能（如天气查询等）

## API 文档

### 1. FastAPI 模式

**发送邮件接口**
```
POST /api/send-email
Content-Type: application/json

Request:
{
    "address": string,  // 收件人邮箱
    "content": string   // 邮件内容
}

Response:
{
    "status": string,   // "success" 或 "error"
    "message": string   // 状态信息
}
```

### 2. MCP 模式

**命令格式**
```
exec send_email {"address": "example@gmail.com", "content": "message"}
```

## 运行指南

### 1. 环境准备
```bash
# 创建虚拟环境
python -m venv .venv
source .venv/bin/activate  # Unix
.venv\Scripts\activate     # Windows

# 安装依赖
pip install -r requirements.txt
```

### 2. FastAPI 模式运行
```bash
uvicorn app.main:app --reload
```

### 3. MCP 模式运行
```bash
# 启动 MCP 服务器
uv run client_no_api.py /path/to/mcp-server/build/index.js
```

## 功能概述

1. **邮件发送**
   - 支持 Gmail OAuth 认证
   - 安全的邮件发送功能
   - 支持纯文本邮件内容

2. **认证管理**
   - OAuth 2.0 认证流程
   - 令牌自动刷新
   - 安全凭据存储

3. **错误处理**
   - 完善的错误提示
   - 异常状态处理
   - 认证失败处理

4. **扩展功能**
   - 天气查询（通过 MCP 模式）
   - 其他 MCP 支持的功能

## 安全性考虑

1. OAuth 凭据安全存储
2. 环境变量配置敏感信息
3. 输入验证和清洗
4. 错误信息安全处理
