FROM python:latest
LABEL org.opencontainers.image.source="https://github.com/m62624/FilesCustodian"

WORKDIR /main_project

RUN mkdir FilesCustodianGUI dist;
ENV VIRTUAL_ENV=FilesCustodianGUI/.env;
RUN python -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

RUN pip install pyinstaller \
                PyQt5 \
                altgraph \
                click \
                packaging \
                pyinstaller-hooks-contrib \
                PyQt5-Qt5 \
                PyQt5-sip \
                qt5-applications \
                qt5-tools \
                setuptools;

RUN apt-get update && apt-get install -y \
    python3-pyqt5 \
    python3-pyqt5.qttools

COPY . .

CMD ["sh"]
