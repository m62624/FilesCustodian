FROM python:latest
LABEL org.opencontainers.image.source="https://github.com/m62624/FilesCustodian"

WORKDIR /main_project

RUN mkdir FilesCustodianGUI dist;
ENV VIRTUAL_ENV=FilesCustodianGUI/.env;
RUN python -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

RUN pip install cx_Freeze \
                PyQt5 \
                altgraph \
                click \
                packaging \
                PyQt5-Qt5 \
                PyQt5-sip \
                qt5-applications \
                qt5-tools \
                black \
                setuptools;

COPY . .

CMD ["sh"]
