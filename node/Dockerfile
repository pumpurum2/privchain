FROM ethereum/client-go:stable

COPY ./genesis.json /tmp
RUN geth init /tmp/genesis.json

ARG ACCOUNT_FILE

COPY node/.password /tmp/pass
COPY ${ACCOUNT_FILE} /root/.ethereum/keystore/account.json

ENTRYPOINT ["geth"]