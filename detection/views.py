# # detection/views.py
# import cv2
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework.parsers import MultiPartParser, FormParser
# from ultralytics import YOLO
# import numpy as np

# class ClothDetectionView(APIView):                                                  
#     parser_classes = (MultiPartParser, FormParser)

#     def post(self, request, *args, **kwargs):
#         model = YOLO(r'C:\Users\vinothg\Desktop\coordinates\Final_model_cloth_Detect.pt')

#         # Get the uploaded image from the request
#         file_obj = request.FILES['image']
#         image_data = file_obj.read()

#         # Convert the image to a format OpenCV can work with
#         np_arr = np.fromstring(image_data, np.uint8)
#         img = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)
#         img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

#         # Perform inference
#         results = model(img_rgb)

#         response_data = []
#         for result in results:
#             boxes = result.boxes.xyxy.cpu().numpy()
#             scores = result.boxes.conf.cpu().numpy()
#             classes = result.boxes.cls.cpu().numpy()
            
                                  
#             for box, score, cls in zip(boxes, scores, classes):
#                 x1, y1, x2, y2 = map(int, box)
#                 width = x2 - x1
                
#                 height = y2 - y1
#                 label = f"{model.names[int(cls)]}"
#                 confidence = f"{score:.2f}"
#                 coordinates = {
#                     'x': x1,
#                     'y': y1,
#                     'width': width,
#                     'height': height
#                 }
#                 detection = {
#                     'label': label,
#                     'confidence': confidence,
#                     'coordinates': coordinates
#                 }
#                 response_data.append(detection)

#         return Response({'detections': response_data})





import cv2
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from ultralytics import YOLO
import numpy as np

class ClothDetectionView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, *args, **kwargs):
        model = YOLO(r'C:\Users\vinothg\Desktop\coordinates\Final_model_cloth_Detect.pt')

        # Get the uploaded image from the request
        file_obj = request.FILES.get('image')  # Use .get() to safely retrieve the file

        if not file_obj:
            return Response({'error': 'No image provided'}, status=400)

        image_data = file_obj.read()

        # Convert the image to a format OpenCV can work with
        np_arr = np.frombuffer(image_data, np.uint8)
        img = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        # Perform inference
        results = model(img_rgb)

        response_data = []
        for result in results:
            boxes = result.boxes.xyxy.cpu().numpy()
            scores = result.boxes.conf.cpu().numpy()
            classes = result.boxes.cls.cpu().numpy()

            for box, score, cls in zip(boxes, scores, classes):
                x1, y1, x2, y2 = map(int, box)
                width = x2 - x1
                height = y2 - y1
                label = f"{model.names[int(cls)]}"
                confidence = f"{score:.2f}"
                coordinates = {
                    'x': x1,
                    'y': y1,
                    'width': width,
                    'height': height
                }
                detection = {
                    'label': label,
                    'confidence': confidence,
                    'coordinates': coordinates
                }
                response_data.append(detection)

        return Response({'detections': response_data})
