## useful

### accounts

create
`geth --datadir=/some/dir account new`

or import from priv key
`geth --datadir=/some/dir account import /path/to/file/with/priv/key`

then see /some/dir/keystore

## bootnode

need white ip, entrypoint for other nodes to find peers



# Steps

### 1. create accounts for signers
`geth account new`
or
`geth account import` for existing private key
### 2. create genesis file
`python make-genesis.py <initial amount> 0xSigner1 0xSigner2 > genesis.json`