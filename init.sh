#!/bin/bash

GITLAB_HOME=/home/eyammer/repos/gitlab/gitlab

sudo docker run --detach \
 --hostname gitlab.example.com \
 --env GITLAB_OMNIBUS_CONFIG="external_url 'http://gitlab.example.com'" \
 --publish 443:443 --publish 80:80 \
 --name gitlab \
 --restart always \
 --volume $GITLAB_HOME/config:/etc/gitlab \
 --volume $GITLAB_HOME/logs:/var/log/gitlab \
 --volume $GITLAB_HOME/data:/var/opt/gitlab \
 --shm-size 256m \
 gitlab/gitlab-ee:15.11.13-ee.0
# docker exec -it gitlab bash -c 'cat /etc/gitlab/initial_root_password' | grep -i password