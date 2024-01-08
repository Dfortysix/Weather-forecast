# Sử dụng một hình ảnh cơ sở có Python đã được cài đặt
FROM python:3.9

# Đặt thư mục làm việc trong container
WORKDIR /app

# Sao chép các tệp tin requirements.txt vào container
COPY requirements.txt .

# Cài đặt các dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Sao chép các tệp tin trong thư mục gốc vào container
COPY . .

# Khai báo port mà ứng dụng Django sẽ lắng nghe
EXPOSE 8000

# Chạy lệnh để khởi chạy ứng dụng Django
CMD ["python3", "manage.py", "runserver",]

