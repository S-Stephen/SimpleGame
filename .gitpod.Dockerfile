FROM gitpod/workspace-full-vnc

USER root

RUN apt-get update \
    && apt-get install -y libgtk-3-dev \
    && apt-get install -y tk-dev \
    && apt-get install -y python3-tk

# Install custom tools, runtime, etc. using apt-get
# For example, the command below would install "bastet" - a command line tetris clone:
#
# RUN apt-get update \
#    && apt-get install -y bastet \
#    && apt-get clean && rm -rf /var/cache/apt/* && rm -rf /var/lib/apt/lists/* && rm -rf /tmp/*
#
# More information: https://www.gitpod.io/docs/42_config_docker/
