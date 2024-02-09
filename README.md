# trieve_client_py
A client library for accessing trieve.ai

## Installation
```
pip install trieve_client_py
```

## Usage
First, create a client:

```python
from trieve_client import Client

client = Client(base_url="https://api.example.com")
```

If the endpoints you're going to hit require authentication, use `AuthenticatedClient` instead:

```python
from trieve_client import AuthenticatedClient

api_key = os.getenv("API_KEY")
dataset_id = os.getenv("DATASET_ID")
organization_id = os.getenv("ORGANIZATION_ID")

client = AuthenticatedClient(base_url="https://api.trieve.ai",
    prefix="",
    token=api_key
).with_headers({
    "TR-Dataset": dataset_id,
    "TR-Organization": organization_id,
});
```

### Uploading Chunks

```python
from trieve_client.api.chunk import create_chunk
from trieve_client.models import CreateChunkData, ReturnCreatedChunk
from trieve_client.models.error_response_body import ErrorResponseBody

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

chunk_response = create_chunk.sync(
    tr_dataset=dataset_id,
    client=client,
    body=chunk
)

if type(chunk_response) == ReturnCreatedChunk:
    print(f"queue'd pos: {chunk_response.pos_in_queue}")
elif type(chunk_response) == ErrorResponseBody:
    print(f"Failed {chunk_response.message}")
    exit(1)

```

### Searching Chunks

```py
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
```

### More

For more examples checkout the `examples/` directory for a full scripts

## Regenerating the apitypes

Modify the .code-gen/openapi.json to a new version
run

```
.code-gen/generate.sh
```

Everything should be up-to-date then
