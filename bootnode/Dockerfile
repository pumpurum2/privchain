FROM ethereum/client-go:alltools-stable

COPY ./genesis.json /tmp
RUN geth init /tmp/genesis.json

RUN bootnode -nodekey ~/.ethereum/geth/nodekey -writeaddress > ~/.ethereum/enode

ENTRYPOINT ["geth"]