
ENV PROJECT=default

FROM image-registry.openshift-image-registry.svc:5000/$PROJECT/seldon-core-s2i-python37-ubi8:1.2.2
# FROM seldon-core-s2i-python37-ubi8:1.2.2
COPY . /microservice
WORKDIR /microservice

RUN echo "---> Adding extra index url to pip... EXTRA_INDEX_URL: ${EXTRA_INDEX_URL} "

RUN pip config set global.extra-index-url "${EXTRA_INDEX_URL}"
RUN echo "---> Installing dependencies ..."
RUN pip install -r requirements.txt
# RUN echo "---> Installing licenses ..."
# RUN pip install pip-licenses
# RUN mkdir ./licenses && pip-licenses --from=mixed --format=csv --output-file=./licenses/license_info.csv && \
    # pip-licenses --from=mixed --format=plain-vertical --with-license-file --no-license-path --output-file=./licenses/license.txt
# RUN mv ./licenses /licenses
CMD exec seldon-core-microservice $MODEL_NAME $API_TYPE --service-type $SERVICE_TYPE --persistence $PERSISTENCE

EXPOSE 5000