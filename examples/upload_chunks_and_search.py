from trieve_client.api.chunk import create_chunk, search_chunk
from trieve_client.api.chunk_group import create_chunk_group
from trieve_client.models import ChunkGroup, CreateChunkData, CreateChunkGroupData, SearchChunkData, ReturnCreatedChunk, SearchChunkQueryResponseBody
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

        print("hi")
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
            print(create_chunk_response)
            if type(create_chunk_response) == ReturnCreatedChunk:
                print(f"Creating chunk queue'd pos: {create_chunk_response.pos_in_queue}")
            elif type(create_chunk_response) == ErrorResponseBody:
                print(f"Failed to create chunk body {create_chunk_response.message}")
                exit(1)

        # Conduct an example search
        search_data = SearchChunkData(
            # The query that you want to search for
            query="example",
            # The type of search that you want to conduct
            search_type="semantic",
            # Bias search results that are more recent
            date_bias=False,
            # Filters are based on metadata keys that you inserted
            filters={
                "anykey": "any-data",
            },
            # Rather or not to fetch collisions, this is a
            # more advanced feature that is not used often
            get_collisions=False,
            # We highlight relevant parts of the search highlight_results
            # the delimeters are what characters to split on. By default
            # we split on sentence end. (., !, ?)
            highlight_delimiters=None,
            # Rather or not to highlight results
            highlight_results=True,
            # Require that the search results have a links that fuzzy match
            link=["example"],
            # What page of results to fetch
            page=1,
            # Only fetch results that are in a specified tag group
            tag_set=["test"],
            # A tuple of two strings, the start and end of the time range
            time_range=None,
        )

        search_response = search_chunk.sync(tr_dataset=dataset_id, client=client, body=search_data)
        if type(search_response) == SearchChunkQueryResponseBody:
            print(f"Got {search_response.total_chunk_pages} pages of results. Search results: {search_response}")
        elif type(search_response) == ErrorResponseBody:
            print(f"Failed to search body {search_response.message}")
            exit(1)
