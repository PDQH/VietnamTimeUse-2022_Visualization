import pandas as pd
from time import gmtime, strftime
from d3blocks import D3Blocks

# Chuyển đổi cột thời gian trong file csv từ số sang định dạng thời gian chuẩn
def convert_time(minute):
    return strftime("%d-%m-%Y %H:%M:%S", gmtime(int(minute) * 60))

# Chuyển đổi cột công việc trong csv từ mã sang chữ 
def get_activity(code):
    code = int(code)
    if code in [101, 102, 103, 104, 199, 201, 202, 203, 204, 205, 299, 301, 302, 303, 304, 305, 398, 399, 
    401, 402, 403, 404, 405, 499, 501, 502, 503, 504, 505, 506, 507, 508, 509, 510, 599]:
        return "Làm việc"
    elif code in [198, 298, 298, 398, 498, 598, 698, 798, 898, 998, 1098, 1198, 1298, 1398, 1498, 1598]:
        return "Di chuyển"
    elif code in [601, 698, 699]:
        return "Làm việc nhà"
    elif code in [801, 802, 803, 804, 805, 899]:
        return "Hoạt động cộng đồng"
    elif code in [602]:
        return "Mua sắm"
    elif code in [701, 702]:
        return "Chăm sóc người thân"
    elif code in [901, 902, 903]:
        return "Học tập và đào tạo"
    elif code in [1201, 1202, 1203, 1299, 1402, 1404]:
        return "Giải trí"
    elif code in [1301, 1302, 1399]:
        return "Chơi thể thao"
    elif code == 1501:
        return "Ngủ"
    elif code == 1502:
        return "Ăn uống"
    elif code == 1503:
        return "Vệ sinh cá nhân"
    elif code == 1506:
        return "Thư giãn/ Không làm gì cả"
    else:
        return "Khác"

# Đọc file csv
data = pd.read_csv("4_diary_main.csv", usecols=["ID", "BEGIN", "Q401"],
                   encoding='latin-1',
                   converters={"Q401": get_activity, "BEGIN": convert_time})

# Sắp xếp dữ liệu
data = data.sort_values(["ID", "BEGIN"])

# Đổi tên các cột thành tên phù hợp với thư viện d3block
data = data.rename(columns={"ID": "sample_id", "BEGIN": "datatime", "Q401": "state"})

# Lấy số lượng dữ liệu tùy ý để biểu diễn trong biểu đồ
# data = data.iloc[:int(len(data) / 2)]

# Dùng thư viện d3block để biểu diễn dữ liệu
d3 = D3Blocks()
d3.movingbubbles(data, datetime="datatime", sample_id="sample_id", state="state",
                 filepath="./vietnam_time_use.html",
                 note="Cách người Việt Nam sử dụng thời gian trong một ngày.",
                 cmap="hsv", damper=1.2 , center="Di chuyển", figsize=(780, 800), size=1)