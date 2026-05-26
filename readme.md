# ⚙️ Cài đặt môi trường

Đảm bảo bạn đã cài đặt Python 3.11 trên máy. Để cài đặt các thư viện cần thiết cho việc chạy test (bao gồm `pytest` và `pytest-cov`), hãy mở terminal tại thư mục gốc của dự án và chạy lệnh sau:

```bash
pip install -r requirements.txt
```

# 🚀 Hướng dẫn chạy Test và Đo lường độ phủ (Coverage)

Dự án hỗ trợ đo độ phủ mã theo hai tiêu chuẩn quan trọng trong kiểm thử: C0 (Statement Coverage - Độ phủ dòng lệnh) và C1 (Branch Coverage - Độ phủ nhánh).

## 1. Đo độ phủ C0 (Statement Coverage)

Để kiểm tra mức độ bao phủ các dòng lệnh của bộ test, sử dụng cú pháp:

```bash
pytest --cov=<tên_file_cần_test>
```

Ví dụ chạy thực tế:

```bash
pytest --cov=loan_origination_system
```

## 2. Đo độ phủ C1 (Branch Coverage)

Để kiểm tra xem các test case đã quét qua đầy đủ các nhánh logic (if/elif/else) hay chưa, thêm cờ --cov-branch vào cú pháp:

```Bash
pytest --cov=<tên_file_cần_test> --cov-branch
```

Ví dụ chạy thực tế:

```Bash
pytest --cov=loan_origination_system --cov-branch
```

## 3. Xuất báo cáo trực quan (HTML Report)

Để dễ dàng theo dõi chi tiết (những dòng code hoặc nhánh nào chưa được cover sẽ bị highlight màu đỏ), bạn có thể xuất kết quả test C1 ra giao diện web:

```Bash
pytest --cov=<tên_file_cần_test> --cov-branch --cov-report=html
```

Ví dụ chạy thực tế:

```Bash
pytest --cov=loan_origination_system --cov-branch --cov-report=html
```

Lưu ý: Sau khi lệnh này chạy xong, hệ thống sẽ sinh ra một thư mục có tên là htmlcov. Bạn chỉ cần tìm và mở file index.html trong thư mục đó bằng bất kỳ trình duyệt web nào để xem báo cáo chi tiết.
