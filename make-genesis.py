import sys

if len(sys.argv) == 1:
    print("usage: python make-genesys.py <initial balance> 0xAddress01 0xAddress02 0xAddress03 > genesis.json")
    exit()

balance = sys.argv[1]
addresses = sys.argv[2:]

nl = "\n"
print(f"""{{
  "config": {{
    "chainId": 112211,
    "homesteadBlock": 0,
    "eip150Block": 0,
    "eip155Block": 0,
    "eip158Block": 0,
    "byzantiumBlock": 0,
    "constantinopleBlock": 0,
    "petersburgBlock": 0,
    "istanbulBlock": 0,
    "berlinBlock": 0,
    "londonBlock": 0,
    "clique": {{
      "period": 5,
      "epoch": 30000
    }}
  }},
  "difficulty": "1",
  "gasLimit": "30000000",
  "extradata": "0x0000000000000000000000000000000000000000000000000000000000000000{"".join([a[2:] for a in addresses])}0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000",
  "alloc": {{
    {("," + nl + "    ").join([f'"{a[2:]}": {{ "balance": "{balance}" }}' for a in addresses])}
  }}
}}""")