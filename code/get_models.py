import os
import sys
import json
import requests
from dotenv import load_dotenv
from huggingface_hub import snapshot_download

load_dotenv()
custom_hf_cache_dpath = os.getenv("HF_HOME")
# HF_HOME = os.getenv("HF_HOME")
# HF_HOME = os.environ["HF_HOME"]


def get_model(args):
    # Access specific arguments
    if len(sys.argv) != 3:
        print("Incorrect number of arguments")
        return None

    if sys.argv[1] != "--model" and sys.argv[1] != "-m":
        print("Argument --model missing.")
        return None

    return sys.argv[2]  # model name


def get_model_id(model):
    """
    Input:

    - model: combination of organization and model name separated by slash,
    e.g. Unbabel/wmt22-cometkiwi-da
    """

    response = requests.get(f"https://huggingface.co/api/models/{model}")

    if response.status_code != 200:
        print(f"Model '{model}' does not exist on Hugging Face.")

    return json.loads(response.text).get("modelId")


def find_model_in_hf(model):
    response = requests.get(f"https://huggingface.co/api/models?search={model}")

    # Check if the request was successful
    if response.status_code == 200:
        models = response.json()
        for model in models:
            print(f"{model=}")
    else:
        print(f"Failed to search for models. Status code: {response.status_code}")


if __name__ == "__main__":
    model = get_model(sys.argv)
    print(f"{model=}")

    if not model:
        sys.exit(
            "Incorrect call, expected:\n\n  > python code/get_models.py --model Organization/model-name"
        )

    # x = find_model_in_hf(model)
    repo_id = get_model_id(model)

    snapshot_download(
        repo_id=repo_id,
        repo_type="model",
        cache_dir=f"{custom_hf_cache_dpath}",
    )

    print(
        f"Downloading model to {custom_hf_cache_dpath}/models--{repo_id.replace('/', '--')}"
    )
