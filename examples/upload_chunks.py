import os

from dotenv import load_dotenv

from trieve_client import AuthenticatedClient
from trieve_client.api.chunk import create_chunk
from trieve_client.models import CreateChunkData, ReturnCreatedChunk
from trieve_client.models.error_response_body import ErrorResponseBody

### This sample only shows how to upload chunks to Trieve

load_dotenv()

if __name__ == "__main__":
    ## Load environment variables
    api_key = os.getenv("API_KEY")
    dataset_id = os.getenv("DATASET_ID")
    organization_id = os.getenv("ORGANIZATION_ID")

    client = AuthenticatedClient(base_url="https://api.trieve.ai", prefix="", token=api_key).with_headers(
        {
            "TR-Dataset": dataset_id,
            "TR-Organization": organization_id,
        }
    )
    with client as client:
        for i in range(10):
            id = "example-chunk-id"
            chunk = CreateChunkData(
                # We accept html inputs, the html tags are NOT embedded.
                # HTML does help for us to highlight results in the response.
                chunk_html=f"<h1>Hello, World! chunk {id}</h1>",
                # If you have a link that relates to your chunk
                link=f"https://{id}.com",
                # Add as many tags as needed
                tag_set=["example", "test", id],
                # Since we queue writes, tracking id helps to prevent duplicates
                # This can be any internal id system that you have or simply left
                # blank
                tracking_id=id,
                # You can put a timestamp as when it was made, this helps with the
                # timerange filter that we have
                time_stamp="2021-01-01T00:00:00Z",
                # You can place a list of group ids that the chunk will automatically
                # be added to. Chunks can also be added to groups after.
                group_ids=[],
                # Similar thing with GroupID just less flexible, adding this chunk to a fileID
                file_id=None,
                # Chunk Vector is an alternative to chunk_html.
                # Chunk Vector may be used if you already embedded the data
                chunk_vector=None,
                weight=None,
                # We allow for arbitrary metadata
                metadata={
                    "anykey": "any-data",
                    "id": id,
                },
            )

            chunk_response = create_chunk.sync(tr_dataset=dataset_id, client=client, body=chunk)

            if type(chunk_response) == ReturnCreatedChunk:
                print(f"queue'd pos: {chunk_response.pos_in_queue}")
            elif type(chunk_response) == ErrorResponseBody:
                print(f"Failed {chunk_response.message}")
                exit(1)
