FROM alpine:latest

# COPY  ./PA /playbooks/

RUN echo "===> Update the index of all available packages ..."             && \
           apk update 

RUN echo "===> Install the required apk packages and Python ..."           && \
      apk add --no-cache  \
        build-base        \
        libffi-dev        \
        openssl-dev       \
        py3-cryptography  \
        py3-jinja2        \
        py3-paramiko      \
        py3-pip           \
        py3-six           \
        py3-yaml          \
        python3           \
        python3-dev       \
        bash              \
#        wheel             \
        wget

RUN echo "===> Upgrade pip to lastest ..."                            && \
      pip3 install -U  \
        pip            \
        cffi

RUN echo "===> Install Ansible ..."                                   && \
      pip3 install                                                           \
        'ansible==2.10.0'                                            \
        ansible-lint

RUN mkdir /playbooks

COPY  ./PA/  /playbooks/

RUN echo "===> Install Panos Ansible Collection .. "                  && \
       ansible-galaxy collection install paloaltonetworks.panos