from trieve_client.api.chunk import create_chunk
from trieve_client.api.chunk_group import create_chunk_group
from trieve_client.api.message import create_message_completion_handler
from trieve_client.api.topic import create_topic
from trieve_client.models import ChunkGroup, CreateChunkData, CreateChunkGroupData, ReturnCreatedChunk, CreateTopicData, Topic
from trieve_client.models.create_message_data import CreateMessageData
from trieve_client.models.error_response_body import ErrorResponseBody
import os
from dotenv import load_dotenv
from trieve_client import AuthenticatedClient

load_dotenv()

api_key = os.getenv("API_KEY")
dataset_id = os.getenv("DATASET_ID")
print(api_key, dataset_id)

if api_key is None or dataset_id is None:
    raise ValueError("Please set your environment variables for VITE_API_KEY, VITE_DATASET_ID, and VITE_ORGANIZATION_ID")

if __name__ == "__main__":

    client = AuthenticatedClient(base_url="https://api.trieve.ai", prefix="", token=api_key).with_headers({
        "TR-Dataset": dataset_id,
    });


    with client as client:
        group = CreateChunkGroupData(
            description="This is a test group",
            name="Test Group",
        );

        ## In this example, we create a group and add 10 chunks to it
        ## Groups are a way to organize chunks and can be used to filter search results
        ## A chunk can be added to multiple groups
        group_id = None

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
                metadata={
                    "anykey": "anyvalue",
                    "id": id,
                },
                weight=None
            )
            create_chunk_response = create_chunk.sync(tr_dataset=dataset_id, client=client, body=chunk)
            if type(create_chunk_response) == ReturnCreatedChunk:
                print(f"Creating chunk queue'd pos: {create_chunk_response.pos_in_queue}")
            elif type(create_chunk_response) == ErrorResponseBody:
                print(f"Failed to create chunk body {create_chunk_response.message}")
                exit(1)

        # Connduct a new RAG chat (topic)
        topic = CreateTopicData(
            # The title of the topic
            # Can be set to null and assinged 
            # a name based on the context also
            name="Test Topic",
            # The model to use for the chat
            # To use the defalt we just set it to None
            # otherwise set it to the srting model name
            model=None,
            # The first message in the chat
            first_user_message="Hello, World!",
        )

        topic_id = None
        print("Creating a new topic...", end="")
        create_topic_response = create_topic.sync(tr_dataset=dataset_id, client=client, body=topic)
        if type(create_topic_response) == Topic:
            topic_id = create_topic_response.id
            print(f"Created Topic: {create_topic_response.id}")
        elif type(create_topic_response) == ErrorResponseBody:
            print(f"Failed to create topic body {create_topic_response.message}")
            exit(1)

        if topic_id is None:
            print("Failed to create topic")
            exit(1)

        # Stream a new chat
        next_message = CreateMessageData(
            new_message_content="Are you doing well good sir?",
            topic_id=topic_id,
            stream_response=False,
            highlight_citations=True,
            highlight_delimiters=None,
            model=None,
        )
        print("Streaming a new message...", end="")
        create_message_response = create_message_completion_handler.sync(tr_dataset=dataset_id, client=client, body=next_message)
        if type(create_message_response) == ErrorResponseBody:
            print(f"Failed to create message body {create_message_response.message}")
            exit(1)

        # should be a message that is a string
        print(create_message_response)

