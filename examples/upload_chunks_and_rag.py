from trieve_client.api.chunk import create_chunk, search_chunk
from trieve_client.api.chunk_group import create_chunk_group
from trieve_client.api.message import create_message_completion_handler
from trieve_client.api.topic import create_topic
from trieve_client.models import ChunkGroup, CreateChunkData, CreateChunkGroupData, SearchChunkData, ReturnCreatedChunk, SearchChunkQueryResponseBody, CreateTopicData, CreateMessageData
from trieve_client.models.error_response_body import ErrorResponseBody
import os
from dotenv import load_dotenv
from trieve_client import AuthenticatedClient

load_dotenv()

api_key = os.getenv("VITE_API_KEY")
dataset_id = os.getenv("VITE_DATASET_ID")

if api_key is None or dataset_id is None:
    raise ValueError("Please set your environment variables for VITE_API_KEY, VITE_DATASET_ID, and VITE_ORGANIZATION_ID")

if __name__ == "__main__":

    client = AuthenticatedClient(prefix="", base_url="http://localhost:8090", token=api_key).with_headers({
        "TR-Dataset": dataset_id,
    });

    group = CreateChunkGroupData(
        description="This is a test group",
        name="Test Group",
    );

    group_id = None

    with client as client:

        create_chunk_group_response = create_chunk_group.sync(tr_dataset=dataset_id, client=client, body=group)
        if type(create_chunk_group_response) == ChunkGroup:
            group_id = create_chunk_group_response.id
            print(f"Created group {group_id}") 
        elif type(create_chunk_group_response) == ErrorResponseBody:
            print(f"Failed to create group body {create_chunk_group_response.message}")
            exit(1)

        for i in range(1, 10):
            id = f"example-{i}"

            # Create a chunk
            chunk = CreateChunkData(
                chunk_html=f"<h1>Hello, World! chunk {id}</h1>",
                link=f"https://example-{id}.com",
                tag_set=["example", "test", id],
                tracking_id=f"{id}-man22-pani",
                time_stamp="2021-01-01T00:00:00Z",
                group_ids=[group_id] if group_id is not None else None,
                chunk_vector=None,
                file_id=None,
                metadata=None,
                weight=None
            )
            create_chunk_response = create_chunk.sync(tr_dataset=dataset_id, client=client, body=chunk)
            if type(create_chunk_response) == ReturnCreatedChunk:
                print(f"Creating chunk queue'd pos: {create_chunk_response.pos_in_queue}")
            elif type(create_chunk_response) == ErrorResponseBody:
                print(f"Failed to create chunk body {create_chunk_response.message}")
                exit(1)

        # Create a new RAG chat
        chat_topic = CreateTopicData(
            first_user_message="Hello, World!",
            model="gpt-3.5-turbo",
            name="Test Chat",
        )
        create_topic_response = create_topic.sync(tr_dataset=dataset_id, client=client, body=chat_topic)

        topic_id = None

        if type(create_topic_response) == CreateTopicData:
            print(f"Created chat {create_topic_response.id}")
            topic_id = create_topic_response.id
        elif type(create_topic_response) == ErrorResponseBody:
            print(f"Failed to create chat body {create_topic_response.message}")
            exit(1)

        if topic_id is None:
            print("Failed to create chat")
            exit(1)

        # Stream a new RAG chat
        message = CreateMessageData(
            new_message_content="Hello, World!",
            highlight_citations=True,
            model="gpt-3.5-turbo",
            highlight_delimiters=None,
            stream_response=False,
            topic_id=topic_id
        )
        create_message_response = create_message_completion_handler.sync(tr_dataset=dataset_id, client=client, body=message)
