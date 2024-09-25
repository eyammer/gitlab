#!/bin/bash

export GITLAB_TOKEN=''
GITLAB_HOME=/home/eyammer/repos/gitlab/gitlab
MY_GILAB_URL=http://172.19.16.84:80/

docker run -it -e ACCESS_TOKEN="${GITLAB_TOKEN}" -v $(pwd)/gpt.json:/tmp/gpt.json gitlab/gpt-data-generator "--environment=/tmp/gpt.json"