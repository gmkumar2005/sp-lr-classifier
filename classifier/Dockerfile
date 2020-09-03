ARG PROJECT
FROM image-registry.openshift-image-registry.svc:5000/$PROJECT/sklearnserver-rest:1.2.2
# FROM seldon-core-s2i-python37-ubi8:1.2.2
COPY . /microservice
WORKDIR /microservice

RUN echo "---> Adding extra index url to pip... EXTRA_INDEX_URL: ${EXTRA_INDEX_URL} "

RUN pip config set global.extra-index-url "${EXTRA_INDEX_URL}"
RUN echo "---> Installing dependencies ..."
RUN pip install -r requirements.txt