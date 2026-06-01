# Khởi tạo dữ liệu video rỗng
# Lặp vô hạn
#     Hiển thị menu
#     Nhập lựa chọn
#    Nếu không phải số
#         báo lỗi
#         quay lại menu
#     Nếu lựa chọn = 1
#         nhập thông tin video
#         kiểm tra username
#         kiểm tra description
#         xử lý thống kê
#     Nếu lựa chọn = 2
#         chuẩn hóa username
#     Nếu lựa chọn = 3
#         nhập hashtag
#         kiểm tra hashtag hợp lệ
#         nếu hợp lệ
#             thêm vào danh sách hashtag
#     Nếu lựa chọn = 4
#         kiểm tra đã có mô tả chưa
#         nhập từ khóa cần tìm
#         nhập từ khóa thay thế
#         tìm kiếm
#         thay thế
#     Nếu lựa chọn = 5
#         thoát chương trình
#     Ngược lại
#         báo lỗi menu


# Hệ thống kiểm duyệt nội dung video TikTok

# Các biến này dùng để lưu dữ liệu video hiện tại
username = ""
video_title = ""
video_description = ""
hashtags = []


def show_menu():
    # Hàm hiển thị menu chương trình
    print("+================================================+")
    print("|        HỆ THỐNG QUẢN LÝ NỘI DUNG TIKTOK        |")
    print("+================================================+")
    print("| 1. Nhập và phân tích thông tin video           |")
    print("| 2. Chuẩn hóa tên tài khoản                     |")
    print("| 3. Kiểm tra tính hợp lệ của hashtag            |")
    print("| 4. Tìm kiếm và thay thế từ khóa trong mô tả    |")
    print("| 5. Thoát chương trình                          |")
    print("+================================================+")


def normalize_hashtags(hashtag_input):
    # Tách chuỗi hashtag theo dấu phẩy
    hashtag_list = hashtag_input.split(",")

    # Danh sách lưu hashtag sau khi đã xóa khoảng trắng
    normalized_list = []

    for hashtag in hashtag_list:
        # Xóa khoảng trắng đầu và cuối từng hashtag
        clean_hashtag = hashtag.strip()

        # Chỉ thêm hashtag không rỗng vào danh sách
        if clean_hashtag != "":
            normalized_list.append(clean_hashtag)

    return normalized_list


def show_video_report(username, video_title, video_description, hashtags):
    # Chuẩn hóa dữ liệu trước khi in báo cáo
    clean_username = username.strip()
    clean_title = video_title.strip().title()
    clean_description = video_description.strip()

    # len() dùng để đếm số ký tự trong mô tả
    description_length = len(clean_description)

    # split() không truyền gì sẽ tách theo khoảng trắng
    # nên có thể dùng để đếm số từ
    word_count = len(clean_description.split())

    # Đếm số lượng hashtag trong danh sách
    hashtag_count = len(hashtags)

    print("\n===== BÁO CÁO THỐNG KÊ VIDEO =====")
    print(f"Tên tài khoản: {clean_username}")
    print(f"Tiêu đề video: {clean_title}")
    print(f"Mô tả video: {clean_description}")
    print(f"Độ dài mô tả video: {description_length}")
    print(f"Số lượng từ trong mô tả video: {word_count}")
    print(f"Danh sách hashtag: {hashtags}")
    print(f"Số lượng hashtag: {hashtag_count}")

    # lower() chuyển chuỗi thành chữ thường
    print(f"Mô tả viết thường: {clean_description.lower()}")

    # upper() chuyển chuỗi thành chữ hoa
    print(f"Mô tả viết hoa: {clean_description.upper()}")


def normalize_username(username):
    # Xóa khoảng trắng và chuyển tên tài khoản về chữ thường
    clean_username = username.strip().lower()

    # Nếu tài khoản chưa có @ ở đầu thì thêm vào
    if not clean_username.startswith("@"):
        clean_username = "@" + clean_username

    return clean_username


def validate_hashtag(hashtag):
    # Xóa khoảng trắng đầu và cuối hashtag
    clean_hashtag = hashtag.strip()

    # Hashtag không được rỗng
    if clean_hashtag == "":
        return False, "Hashtag không được rỗng"

    # Hashtag phải bắt đầu bằng #
    if not clean_hashtag.startswith("#"):
        return False, "Hashtag phải bắt đầu bằng ký tự #"

    # Hashtag không được chứa khoảng trắng
    if " " in clean_hashtag:
        return False, "Hashtag không được chứa khoảng trắng"

    # Hashtag phải có ít nhất 2 ký tự, ví dụ: #a
    if len(clean_hashtag) < 2:
        return False, "Hashtag phải có ít nhất 2 ký tự"

    # Lấy phần sau dấu #
    content = clean_hashtag[1:]

    # Kiểm tra từng ký tự sau dấu #
    for char in content:
        # isalnum() cho phép chữ cái và chữ số
        # ngoài ra bài cho phép thêm dấu gạch dưới _
        if not (char.isalnum() or char == "_"):
            return (
                False,
                "Hashtag chỉ được chứa chữ cái, chữ số hoặc dấu gạch dưới sau ký tự #",
            )

    return True, "Hashtag hợp lệ"


def replace_keyword(video_description):
    # Nếu chưa có mô tả thì không thể tìm kiếm
    if video_description.strip() == "":
        print("Chưa có mô tả video để tìm kiếm và thay thế")
        return video_description

    keyword = input("Nhập từ khóa cần tìm: ").strip()
    replacement = input("Nhập từ khóa thay thế: ").strip()

    # Từ khóa cần tìm không được rỗng
    if keyword == "":
        print("Từ khóa cần tìm không được rỗng")
        return video_description

    # Kiểm tra từ khóa có trong mô tả không
    if keyword in video_description:
        # count() đếm số lần từ khóa xuất hiện
        count = video_description.count(keyword)

        # replace() thay từ khóa cũ bằng từ khóa mới
        new_description = video_description.replace(keyword, replacement)

        print(f"Số lần từ khóa xuất hiện: {count}")
        print(f"Mô tả sau khi thay thế: {new_description}")

        return new_description

    print("Không tìm thấy từ khóa cần tìm trong mô tả video")
    return video_description


# Vòng lặp chính của chương trình
while True:
    show_menu()

    choice_input = input("> Mời bạn chọn chức năng (1-5): ").strip()

    # Bẫy lỗi: nếu nhập abc, @, 2.5 thì không cho chạy tiếp
    if not choice_input.isdigit():
        print("Lựa chọn không hợp lệ. Vui lòng nhập số từ 1 đến 5.\n")
        continue

    choice = int(choice_input)

    # Bẫy lỗi: nếu nhập số ngoài khoảng 1 đến 5
    if choice < 1 or choice > 5:
        print("Lựa chọn không hợp lệ. Vui lòng nhập lại.\n")
        continue

    if choice == 1:
        username = input("Nhập tên tài khoản người đăng video: ")

        # Bẫy lỗi: tên tài khoản không được rỗng
        if username.strip() == "":
            print("Tên tài khoản không được rỗng\n")
            continue

        video_title = input("Nhập tiêu đề video: ")

        video_description = input("Nhập mô tả video: ")

        # Bẫy lỗi: mô tả không được rỗng
        if video_description.strip() == "":
            print("Mô tả video không được rỗng\n")
            continue

        hashtag_input = input("Nhập danh sách hashtag, cách nhau bởi dấu phẩy: ")

        # Chuẩn hóa danh sách hashtag
        hashtags = normalize_hashtags(hashtag_input)

        # In báo cáo sau khi nhập xong
        show_video_report(username, video_title, video_description, hashtags)
        print()

    elif choice == 2:
        # Nếu chưa nhập username thì không chuẩn hóa được
        if username.strip() == "":
            print(
                "Chưa có tên tài khoản để chuẩn hóa. Vui lòng nhập dữ liệu ở chức năng 1 trước.\n"
            )
            continue

        print("\n===== CHUẨN HÓA TÊN TÀI KHOẢN =====")
        print(f"Tên tài khoản ban đầu: {username}")
        print(f"Tên tài khoản sau khi chuẩn hóa: {normalize_username(username)}\n")

    elif choice == 3:
        hashtag = input("Nhập hashtag cần kiểm tra: ")

        # Kiểm tra hashtag hợp lệ hay không
        is_valid, message = validate_hashtag(hashtag)

        if is_valid:
            clean_hashtag = hashtag.strip()

            # Nếu hợp lệ thì thêm hashtag vào danh sách hiện tại
            hashtags.append(clean_hashtag)

            print(message)
            print(f"Đã thêm hashtag vào danh sách hiện tại: {hashtags}\n")
        else:
            print(message)
            print()

    elif choice == 4:
        # Hàm này trả về mô tả mới sau khi thay thế
        video_description = replace_keyword(video_description)
        print()

    elif choice == 5:
        print("Thoát chương trình")
        break

    


