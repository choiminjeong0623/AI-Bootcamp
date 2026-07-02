from app.repositories.conversation_repository import (
    get_recent_conversations
)


def build_history(limit=5):

    history = []

    conversations = get_recent_conversations(limit)

    for c in conversations:

        history.append(
            {
                "role": "user",
                "content": c["sentence"]
            }
        )

        history.append(
            {
                "role": "assistant",
                "content": c["corrected_sentence"]
            }
        )

    return history