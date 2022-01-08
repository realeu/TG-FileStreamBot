FROM python:3.9

RUN git clone https://github.com/realeu/TG-FileStreamBot root/realeu
WORKDIR root/realeu/

RUN cd WebStreamer

RUN pip install -r requirements.txt

CMD "python3" "-m" "WebStreamer"
