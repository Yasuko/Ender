FROM    python:3.9.7

RUN apt update
RUN apt -y install locales && \
    localedef -f UTF-8 -i ja_JP ja_JP.UTF-8
ENV LANG ja_JP.UTF-8
ENV LANGUAGE ja_JP:ja
ENV LC_ALL ja_JP.UTF-8
ENV TZ JST-9
ENV TERM xterm

RUN apt install -y vim less

# pytorch jupyter notebook setup
RUN python3 -m pip install --upgrade pip
RUN python3 -m pip install --upgrade setuptools
RUN pip3 install notebook matplotlib pandas keras tensorflow

# add jupyter notebook user
#COPY ./user /tmp
#RUN newusers /tmp/user
#RUN rm -f /tmp/user

RUN mkdir /root/work
RUN jupyter notebook --generate-config
COPY ./jupyter_notebook_config.py /root/.jupyter/

#RUN mkdir -p /home/jupyter/work
#RUN chown -R jupyter:jupyter /home/jupyter
