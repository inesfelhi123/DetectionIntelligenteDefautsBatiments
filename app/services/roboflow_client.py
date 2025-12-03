import tempfile
from inference_sdk import InferenceHTTPClient

# Connexion au workflow Roboflow
client = InferenceHTTPClient(
    api_url="https://serverless.roboflow.com",
    api_key="04WucGhgL7KK3t9Rpd9K"  
)

def predict_image(image_bytes):
    # Créer un fichier temporaire
    with tempfile.NamedTemporaryFile(delete=False, suffix=".jpg") as tmp:
        tmp.write(image_bytes)
        tmp_path = tmp.name

    # Appeler Roboflow
    result = client.run_workflow(
        workspace_name="detectionintelligentedefautsbatiments",
        workflow_id="custom-workflow",
        images={"image": tmp_path},
        use_cache=True
    )

    prediction_info = result[0]['predictions']
    top_class = prediction_info['top']
    confidence = prediction_info['confidence']

    return top_class, confidence
