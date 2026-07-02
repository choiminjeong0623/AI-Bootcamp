import json
import os

FILE_NAME = "conversation_log.json"


def save_conversation(
    sentence,
    answer,
    corrected_sentence,
    time
):

    data = load_conversations()

    data.append(
        {
            "sentence": sentence,
            "answer": answer,
            "corrected_sentence": corrected_sentence,
            "time": time
        }
    )

    with open(
        FILE_NAME,
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            data,
            file,
            ensure_ascii=False,
            indent=4
        )


def load_conversations():

    if not os.path.exists(FILE_NAME):
        return []

    try:

        with open(
            FILE_NAME,
            "r",
            encoding="utf-8"
        ) as file:

            return json.load(file)

    except json.JSONDecodeError:
        return []


def get_recent_conversations(limit=5):

    conversations = load_conversations()

    return conversations[-limit:]