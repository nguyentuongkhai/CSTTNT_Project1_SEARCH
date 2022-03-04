Đồ án tìm kiếm đường đi

Tóm tắt đồ án Cài đặt các thuật toán tìm kiếm tìm đường từ vị trí xuất phát đến vị trí đích (vị trí thoát khỏi bản đồ) trong các bản đồ trò chơi. Các thuật toàn cần cài đặt bao gồm: 
  - Thuật toán tìm kiếm có thông tin: 
    + Thuật toán tìm kiếm DFS (Depth First Search). 
    + Thuật toán tìm kiếm BFS (Breadth First Search).
  - Thuật toán tìm kiếm có thông tin: 
    + Thuật toán tìm kiếm tham lam (Greedy Best First Search). 
    + Thuật toán tìm kiếm A. Bản đồ: 
  - Các loại bản đồ: 
    + Bản đồ không có điểm thưởng: Gồm 5 bản đồ khác nhau. 
    + Bản đồ có điểm thưởng: Gồm 3 bản đồ tương ứng 3 trường hợp: 2, 5, và 10 điểm thưởng với các giá trị điểm thưởng khác nhau.. 
  - Kích thước các bản đồ: tất cả đều là 20x40. 
  - Chi phí đường đi từ node này đến node khác bằng nhau (coi các chi phí này đều là 1 đơn vị). 
Môi trường: 
  - IDE: Visual Studio Code, Visual Studio 2019 
  - Ngôn ngữ: Python 3

Hướng dẫn chạy chương trình:
Run file main.py trong folder source.
Chọn thuật toán trong menu trên màn hình console.
Chọn bản dồ:
1 trong 5 bản dồ không có điểm thưởng.
1 trong 3 bản đồ có điểm thưởng.
Chọn thuật thoán A* nếu muốn chạy thuật toán với bản đồ có điểm thưởng.
Nhấn thoát trong menu để quay về bước trước.
Khi đang ở bước chọn menu thuật toán, nếu chọn thoát sẽ thoát chương trình.
Chương trình chỉ nhận diện được cái file bản dồ bên trong folder maze (folder maze cùng cấp với folder source).
