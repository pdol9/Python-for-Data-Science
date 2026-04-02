FROM python:3.10

RUN apt-get update && apt-get install -y vim && \
	pip install flake8 && \
	echo "alias norminette='flake8'" >> /etc/bash.bashrc && \
	echo "alias p='python'" >> /etc/bash.bashrc && \
	echo "alias no='flake8'" >> /etc/bash.bashrc

WORKDIR /app

# create a non-root user and group, home dir, and give minimal permissions
ARG USERNAME=devuser
ARG UID=1000
ARG GID=1000

RUN groupadd -g ${GID} ${USERNAME} && \
	useradd -m -u ${UID} -g ${GID} -s /bin/bash ${USERNAME}

# remove if not needed at any point
#COPY requirements.txt .
#RUN pip install --no-cache-dir -r requirements.txt

# ensure app dir is writable by the user (adjust if you bind-mount)
RUN chown -R ${USERNAME}:${USERNAME} /app

# switch to non-root user
USER ${USERNAME}
ENV HOME=/home/${USERNAME}

COPY .vimrc ${HOME}

# start an interactive login shell
CMD ["bash", "--login"]
