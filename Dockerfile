# syntax=docker/dockerfile:1

ARG PYTHON_VERSION=3.11.5-bookworm
FROM python:${PYTHON_VERSION} as base
ARG DEBIAN_FRONTEND=noninteractive

ARG PROJECT_NAME=plinor_backend_py
# ARG GROUP_ID=5000
# ARG USER_ID=5000


ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# RUN groupadd --gid ${GROUP_ID} ${PROJECT_NAME}
# RUN useradd --uid ${USER_ID} --gid ${GROUP_ID} --shell /bin/sh --skel /dev/null ${PROJECT_NAME} 
# RUN mkdir ${PROJECT_NAME}
# RUN chown -R ${PROJECT_NAME}:${PROJECT_NAME} ${PROJECT_NAME}


WORKDIR /${PROJECT_NAME}

COPY . .

RUN pip3 install --no-cache -r /${PROJECT_NAME}/requirements.txt
RUN pip3 install --no-cache -r /${PROJECT_NAME}/requirements-dev.txt


# USER ${REMOTE_USER}
EXPOSE 5000