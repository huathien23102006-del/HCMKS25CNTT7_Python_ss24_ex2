"""
    (1) Phân tích lỗi Code Review
    Câu 1:

    Nếu để:

    self.points = points

    là public thì hậu quả gì?

    Vì ai cũng có thể sửa:

    card1.points = -50

    hoặc:

    card1.points = "năm mươi"

    Dẫn tới:

    Dữ liệu điểm trong database bị sai.
    Các phép tính cộng điểm bị lỗi:

    Ví dụ:

    card1.points += 100

    nếu trước đó là:

    "năm mươi"

    thì thành:

    "năm mươi100"

    hoặc crash chương trình.

    => Vi phạm Encapsulation (tính đóng gói) và Data Validation.

    Câu 2:

    Muốn kiểm tra dữ liệu trước khi gán vào:

    __points

    dùng decorator:

    @property.setter

    Cụ thể:

    @points.setter
    def points(self,value):

    Nó đóng vai trò như một "cửa kiểm tra" trước khi thay đổi dữ liệu.

    Ví dụ:

    if value >= 0:
        self.__points = value
    Câu 3:

    Hàm:

    def is_eligible_for_voucher(self,bill_amount)

    có self là dư thừa vì:

    Không dùng:
    customer_name
    points
    bất kỳ dữ liệu object nào

    Nó chỉ kiểm tra:

    bill_amount >= 200000

    => Đây là hàm tiện ích, không thuộc về một object cụ thể.

    Câu 4:

    Muốn gọi:

    MemberCard.is_eligible_for_voucher(250000)

    dùng:

    @staticmethod
"""

# Hệ thống Thẻ thành viên Rikkei Coffee

class MemberCard:


    def __init__(self, customer_name, points=0):

        self.customer_name = customer_name

        # thuộc tính private
        self.__points = 0

        # đi qua setter để kiểm tra
        self.points = points



    # Getter đọc điểm
    @property
    def points(self):

        return self.__points



    # Setter kiểm tra dữ liệu
    @points.setter
    def points(self, value):

        if isinstance(value, int) and value >= 0:

            self.__points = value

        else:

            print("Dữ liệu điểm không hợp lệ!")



    # cộng điểm
    def add_points(self, amount):

        if isinstance(amount, int) and amount > 0:

            self.__points += amount

        else:

            print("Số điểm cộng không hợp lệ!")



    # Utility function
    @staticmethod
    def is_eligible_for_voucher(bill_amount):

        return bill_amount >= 200000




# =========================
# TEST HỆ THỐNG
# =========================


card1 = MemberCard("Le Van C",100)



# Thu ngân nhập sai

card1.points = -50



# thử nhập chữ

# card1.points = "năm mươi"



print(
    f"Khách hàng: {card1.customer_name}"
)


print(
    f"Điểm hiện tại: {card1.points}"
)



# gọi trực tiếp từ Class

result = MemberCard.is_eligible_for_voucher(250000)



print(
    f"Hóa đơn 250k có voucher không? {result}"
)