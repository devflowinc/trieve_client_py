cd $(git rev-parse --show-toplevel)
repo_name=${PWD##*/}
cd ..
openapi-python-client update --path="./${repo_name}/.code-gen/openapi.json" --config="./${repo_name}/.code-gen/py-generator.yaml"
