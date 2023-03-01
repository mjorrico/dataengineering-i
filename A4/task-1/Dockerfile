FROM ubuntu:jammy
RUN apt-get update
RUN apt-get -y upgrade
RUN apt-get install sl
ENV PATH="${PATH}:/usr/games/"
RUN echo $PATH
ENV TESTVAR="HELLO"
CMD ["echo", "Data Engineering-I."]

