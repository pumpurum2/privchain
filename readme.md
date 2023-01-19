## useful

### accounts

create
`geth --datadir=/some/dir account new`

or import from priv key
`geth --datadir=/some/dir account import /path/to/file/with/priv/key`

then see /some/dir/keystore

## bootnode

need white ip, entrypoint for other nodes to find peers


## connect to local node in container

`docker exec -it node_node_1 sh`
`geth attach`

## clique signing rules

https://geth.ethereum.org/docs/tools/clef/clique-signing#using-rules


# Steps

### 1. create accounts for signers
`geth account new`
or
`geth account import` for existing private key

### 2. create genesis file
`python make-genesis.py <initial amount> 0xSigner1 0xSigner2 > genesis.json`

example
`python make-genesis.py 1000000000000000000000000 0xaaaa6d95c09be8b2f79a68d75d2dd082ed310b88 0xbbba47970357430f913a5c541ef9e16687b0f1e3 0xccc8bf2a199d544220e8301d42acd4427c44f665 > genesis.json`

### 3. run bootnode

on server 1:
`git clone https://github.com/pumpurum2/privchain.git`

generate or copy `genesis.json` to `privchain` dir

`cd privchain/bootnode`
`docker-compose up -d`

see enode in docker storage in `enode` file
or attach geth and run:
`admin.nodeInfo.enode`
enode will be needed to setup other nodes


### 3. run n nodes

on server n:
`git clone https://github.com/pumpurum2/privchain.git`

generate or copy `genesis.json` to `privchain` dir
copy `keyfile.json` somewhere on server
write to node/.password password for keyfile

create `node/.env` (see .env.example):

`cd privchain/node`
`docker-compose up -d`

### 4. run rpc node

on server n+2:
`git clone https://github.com/pumpurum2/privchain.git`

generate or copy `genesis.json` to `privchain` dir
create `rpcnode/.env` (see .env.example):

`cd privchain/rpcnode`
`docker-compose up -d`
