from django.http import JsonResponse
from rest_framework.views import APIView

class DetectView(APIView):
    def post(self, request, *args, **kwargs):
        file_obj = request.FILES.get('image')  # Use .get() to avoid KeyError
        if not file_obj:
            return JsonResponse({"error": "No file uploaded with the key 'image'"}, status=400)

        # Process the file_obj (e.g., run detection)
        # result = run_detection_model(file_obj)

        return JsonResponse({"message": "Detection successful", "result": result})
