# Dockerfile
FROM python:3.10-slim

# 设置工作目录
WORKDIR /code

# 复制依赖文件并安装
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 复制项目所有代码
COPY . .

# 设置默认命令
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
