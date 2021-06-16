# Using Python Slim-Buster
FROM xluxz/geezproject:buster
# ramubot minta wkwk
# Geez-UserBot
#
RUN git clone -b DAPA-UBOT https://github.com/Daffansaa/DAPA-USERBOT /root/userbot
RUN mkdir /root/userbot/.bin
RUN pip install --upgrade pip setuptools
WORKDIR /root/userbot

#Install python requirements
RUN pip3 install -r https://raw.githubusercontent.com/Daffansaa/DAPA-USERBOT/RAM-UBOT/requirements.txt

EXPOSE 80 443

# Finalization
CMD ["python3","-m","userbot"]
