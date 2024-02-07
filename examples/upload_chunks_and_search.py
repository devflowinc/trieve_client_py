from trieve_client.api.chunk import create_chunk, search_chunk
from trieve_client.api.chunk_group import create_chunk_group
from trieve_client.models import ChunkGroup, CreateChunkData, CreateChunkGroupData, SearchChunkData, ReturnCreatedChunk, SearchChunkQueryResponseBody
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

        # Conduct an example search
        search_data = SearchChunkData(
            query="example",
            search_type="semantic",
            date_bias=False,
            filters={
            },
            get_collisions=False,
            highlight_delimiters=None,
            highlight_results=True,
            link=[],
            page=1,
            tag_set=[],
            time_range=None,
        )

        search_response = search_chunk.sync(tr_dataset=dataset_id, client=client, body=search_data)
        if type(search_response) == SearchChunkQueryResponseBody:
            print(f"Got {search_response.total_chunk_pages} pages of results. Search results: {search_response}")
        elif type(search_response) == ErrorResponseBody:
            print(f"Failed to search body {search_response.message}")
            exit(1)
