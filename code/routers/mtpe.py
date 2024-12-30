import random

# from pathlib import Path
from code.models.mtpe import ScoredTranslation, Translation
from typing import List

# from comet import download_model, load_from_checkpoint
# from huggingface_hub import snapshot_download
from dotenv import load_dotenv
from fastapi import APIRouter, HTTPException  # , status

# from comet import download_model, load_from_checkpoint
# from huggingface_hub import snapshot_download


load_dotenv()

# login(token=TOKEN, add_to_git_credential=True)
clean_up_tokenization_spaces = True


router = APIRouter()


def produce_scores_mock(data):
    data_dict = [{"src": obj.src, "mt": obj.mt} for obj in data]
    return [round(random.uniform(0.5, 1), 15) for x in range(len(data_dict))]


def add_scores_to_data(data, scores):
    # scores = produce_scores(data)
    return [
        ScoredTranslation(
            **translation.dict(),  # Unpack the Translation instance data
            score=score,  # Add the new score value
        )
        for translation, score in zip(data, scores)
    ]


@router.get("/scores")
async def get_scores(translations: List[Translation], model: str, mode: str = "mock"):
    if mode == "mock":
        scores = produce_scores_mock(translations)
    else:
        raise HTTPException(status_code=404, detail="Invalid parameter")

    # model_output_scores = [0.3048415184020996, 0.23436091840267181, 0.6128204464912415]
    # model_output_system_score = 0.38400762776533764

    return {
        "data": add_scores_to_data(translations, scores),
        "model_output_system_score": sum(scores) / len(scores),
    }
