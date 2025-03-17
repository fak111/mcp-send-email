# MCP 邮件发送服务开发文档

## 1. 项目概述
本项目是一个基于 Gmail API 的邮件发送服务，使用 OAuth 认证实现安全的邮件发送功能。

## 2. 技术栈
- FastAPI
- Python 3.8+
- 主要依赖:
  - google-api-python-client
  - google-auth-oauthlib
  - fastapi
  - uvicorn
  - pydantic
  - python-dotenv

## 3. API 接口

### 发送邮件接口
```
POST /api/send-email

请求体:
{
    "address": string,  // 收件人邮箱
    "content": string   // 邮件内容
}

响应:
{
    "status": string,   // "success" 或 "error"
    "message": string   // 状态信息
}
```

## 4. OAuth 配置

### 设置步骤
1. 使用提供的 OAuth 凭据文件:
   `/client_secret_708919691151-gvtj0rkg8ooonjn2jbd3lauu2iai63nn.apps.googleusercontent.com.json`

2. Gmail API 权限:
   - `https://www.googleapis.com/auth/gmail.send`

## 5. 项目结构
```
mcp-send-email/
├── app/
│   ├── main.py
│   ├── config.py
│   └── services/
│       └── email_service.py
├── requirements.txt
└── README.md
```

## 6. 启动步骤
1. 安装依赖:
   ```bash
   pip install -r requirements.txt
   ```

2. 配置环境变量:
   ```
   GOOGLE_CLIENT_ID=your_client_id
   GOOGLE_CLIENT_SECRET=your_client_secret
   ```

3. 启动服务:
   ```bash
   uvicorn app.main:app --reload
   ```

## 7. 注意事项
1. OAuth 令牌安全
2. 输入验证
3. 凭据安全存储
