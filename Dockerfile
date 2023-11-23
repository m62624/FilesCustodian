FROM python:3.12
LABEL org.opencontainers.image.source="https://github.com/m62624/FilesCustodian"

WORKDIR /main_project

RUN mkdir FilesCustodianGUI dist;
ENV VIRTUAL_ENV=FilesCustodianGUI/.env
RUN python -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

RUN pip install \
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

RUN pip install --upgrade --pre --extra-index-url https://marcelotduarte.github.io/packages/ cx_Freeze

COPY . .

CMD ['sh']
