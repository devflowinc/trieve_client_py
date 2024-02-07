cd $(git rev-parse --show-toplevel)
repo_name=${PWD##*/}
cd ..
openapi-python-client update --path="./${repo_name}/.regen/openapi.json" --config="./${repo_name}/.regen/py-generator.yaml"
