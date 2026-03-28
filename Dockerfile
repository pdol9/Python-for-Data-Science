FROM python:3.10
RUN apt-get update && apt-get install -y vim \
 && echo "alias p='python'" >> /etc/bash.bashrc
WORKDIR /app
#COPY requirements.txt .
#RUN pip install --no-cache-dir -r requirements.txt
CMD ["bash"]
