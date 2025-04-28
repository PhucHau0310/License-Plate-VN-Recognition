# import pandas as pd
# import matplotlib.pyplot as plt

# # Đọc file results.csv
# df = pd.read_csv('runs/detect/train/results.csv')

# # Các cột thường có trong results.csv của YOLOv8
# # Ví dụ: 'epoch', 'train/box_loss', 'val/box_loss', 'metrics/precision', 'metrics/recall', 'metrics/mAP50', 'metrics/mAP50-95'
# df.columns = df.columns.str.strip()  # Loại bỏ khoảng trắng trong tên cột

# # Vẽ biểu đồ Loss
# plt.figure(figsize=(10, 5))
# plt.plot(df['epoch'], df['train/box_loss'], label='Training Box Loss', marker='o')
# plt.plot(df['epoch'], df['val/box_loss'], label='Validation Box Loss', marker='s')
# plt.title('Training and Validation Box Loss')
# plt.xlabel('Epoch')
# plt.ylabel('Loss')
# plt.legend()
# plt.grid(True)
# plt.savefig('custom_loss_plot.png')
# plt.show()

# # Vẽ biểu đồ mAP
# plt.figure(figsize=(10, 5))
# plt.plot(df['epoch'], df['metrics/mAP50'], label='mAP@0.5', marker='o')
# plt.plot(df['epoch'], df['metrics/mAP50-95'], label='mAP@0.5:0.95', marker='s')
# plt.title('mAP During Training')
# plt.xlabel('Epoch')
# plt.ylabel('mAP')
# plt.legend()
# plt.grid(True)
# plt.savefig('custom_map_plot.png')
# plt.show()

# from graphviz import Digraph
# import os

# # Đường dẫn đến dot.exe
# os.environ["PATH"] += os.pathsep + r"D:\Program Files\Graphviz-12.2.1-win64\bin"

# dot = Digraph(comment='YOLOv8 Training Pipeline')
# dot.node('A', 'Prepare Dataset\n(Images + Labels)')
# dot.node('B', 'Configure YOLOv8\n(args.yaml)')
# dot.node('C', 'Train Model\n(yolo train)')
# dot.node('D', 'Evaluate Metrics\n(Loss, mAP)')
# dot.node('E', 'Save Model\n(best.pt, last.pt)')
# dot.node('F', 'Visualize Results\n(results.png, PR_curve.png)')
# dot.edges(['AB', 'BC', 'CD', 'DE', 'EF'])
# dot.render('training_pipeline.gv', view=True, format='png')

from graphviz import Digraph
import os
os.environ["PATH"] += os.pathsep + r"D:\Program Files\Graphviz-12.2.1-win64\bin"

dot = Digraph(comment='License Plate Recognition Pipeline')

dot.node('A', 'Input Image')
dot.node('B', 'YOLOv8\nDetect Plate')
dot.node('C', 'Crop Plate')
dot.node('D', 'EasyOCR\nRecognize Text')
dot.node('E', 'Draw Bounding Box\nand Text')
dot.node('F', 'Output Image\n(Base64)')

dot.edges(['AB', 'BC', 'CD', 'DE', 'EF'])

dot.render('pipeline_diagram.gv', view=True, format='png')