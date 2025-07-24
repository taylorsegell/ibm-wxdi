import os

API_VERSION = "v1"
BASE_URL = f"https://{os.getenv('CPD_CLUSTER_HOST')}/v{API_VERSION}"
