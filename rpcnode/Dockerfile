FROM ethereum/client-go:stable

COPY ./genesis.json /tmp
RUN geth init /tmp/genesis.json

ENTRYPOINT ["geth"]