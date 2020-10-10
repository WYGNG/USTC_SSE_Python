FROM python:2.7
WORKDIR /app
COPY . /app
RUN pip install --trusted-host pypi.tuna.tsinghua.edu.cn -r requirements.txt -ihttps://pypi.tuna.tsinghua.edu.cn/simple/
CMD ["python", "launch.py"]



