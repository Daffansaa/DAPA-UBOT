# Using Python Slim-Buster
FROM daffansaa/docks:buster

RUN git clone -b DAPA-UBOT https://github.com/Daffansaa/DAPA-UBOT /root/userbot
RUN mkdir /root/userbot/.bin
RUN pip install --upgrade pip setuptools
WORKDIR /root/userbot

#Install python requirements
RUN pip3 install -r https://raw.githubusercontent.com/Daffansaa/DAPA-UBOT/DAPA-UBOT/requirements.txt

EXPOSE 80 443

# Finalization
CMD ["python3","-m","userbot"]
