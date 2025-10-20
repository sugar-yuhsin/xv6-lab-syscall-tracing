FROM mcr.microsoft.com/devcontainers/cpp:ubuntu-24.04

ARG USER=vscode
ARG GROUP=vscode

ENV HOME="/home/${USER}"
ENV DEBIAN_FRONTEND=noninteractive

# Update & install core packages for development + observability
RUN apt-get update && apt-get install -y --no-install-recommends \
    sudo \
    git \
    curl \
    build-essential \
    gdb-multiarch \
    qemu-system-misc \
    gcc-riscv64-linux-gnu \
    binutils-riscv64-linux-gnu \
    linux-tools-common \
    linux-tools-generic \
    linux-headers-generic \
    strace \
    time \
    lsof \
    net-tools \
    vim \
    man \
    manpages-dev \
    python3 \
    python3-pip \
    bpfcc-tools \
    libbpf-dev \
    libelf-dev \
    zstd \
    ca-certificates \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

RUN chown -R "${USER}:${GROUP}" /home/${USER} \
    && echo "${USER} ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers

# Persist bash hystory
RUN SNIPPET="export PROMPT_COMMAND='history -a' && export HISTFILE=/commandhistory/.bash_history" \
    && mkdir /commandhistory \
    && touch /commandhistory/.bash_history \
    && chown -R "${USER}" /commandhistory \
    && echo "$SNIPPET" >> "/home/${USER}/.bashrc"

USER $USER

