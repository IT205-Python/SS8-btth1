# 2. Nhập dữ liệu và xem báo cáo thống kê
# 	- Nhập dữ liệu, lưu vào từng biến tương ứng
# 	- Chuẩn hoá tên tài khoản (bỏ khoảng trắng đầu cuối)
# 	- Chuẩn hoá tiêu đề (bỏ khoảng trắng đầu cuối, 
# 			viết hoa chữ cái đầu mỗi từ)
# 	- Chuẩn hoá mô tả (bỏ khoảng trắng đầu cuối)
# 	- Hiển thị độ dài mô tả video
# 	- Hiển thị số lượng từ trong mô tả (không dùng mảng)
# 	- Chuẩn hoá danh sách hashtash (Loại bỏ khoảng trắng)
# 		+ #lopcntt5, #monpython, #thaysangdeptrai, #hocchuoi
# 	- Đếm số lượng hashtag (Không dùng mảng)
# 	- Mô tả video chuyển thành chữ thường
# 	- Mô tả video chuyển thành chữ hoa

#Khởi tạo dữ liệu
video_username = ""
video_title = ""
video_description = ""
video_hashtags = []

video_username = input ("Nhập tên tài khoản: ").strip()
video_title = input("Nhập tiêu đề: ").strip().title()
video_description = input("Nhập mô tả: ").strip()
video_hashtags = input("Nhập danh sách hashtag: ").strip().split(",")

result_count_description = 0
print("Độ dài mô tả video:", len(video_description))
for i in video_description:
    if (i == ' '):
        result_count_description += 1

print(f"Số lượng từ trong mô tả: {result_count_description + 1}")

result_count_hashtag = 0
for i in video_hashtags:
    if (i == ' '):
        result_count_hashtag += 1

print(f"Số lượng hashtag: {result_count_hashtag + 1}")

print("Mô tả video chuyển thành chữ thường: ", video_description.lower())

print("Mô tả video chuyển thành chữ hoa: ", video_description.upper())



    