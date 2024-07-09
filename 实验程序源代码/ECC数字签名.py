from fastecdsa import curve, ecdsa, keys
from hashlib import sha384
from hashlib import sha3_256

msg = "A message to sign via ECDSA"

private_key = keys.gen_private_key(curve.p256)
public_key = keys.get_public_key(private_key, curve.p256)
r, s = ecdsa.sign(msg, private_key)
result1 = ecdsa.verify((r, s), msg, public_key)
print("\nDSA with ECC-P256 and SHA2")
print("r = ", r)
print("s = ", s)
print("verify result is :", result1)

r, s = ecdsa.sign(msg, private_key, hashfunc=sha384)
result2 = ecdsa.verify((r, s), msg, public_key, hashfunc=sha384)
print("\nDSA with ECC-P256 and SHA3-384")
print("r = ", r)
print("s = ", s)
print("verify result is :", result2)

private_key = keys.gen_private_key(curve.p224)
public_key = keys.get_public_key(private_key, curve.p224)
r, s = ecdsa.sign(msg, private_key, curve=curve.p224)
result3 = ecdsa.verify((r, s), msg, public_key, curve=curve.p224)
print("\nDSA with ECC-P224 and SHA2")
print("r = ", r)
print("s = ", s)
print("verify result is :", result3)

private_key, public_key = keys.gen_keypair(curve.p256)
r, s = ecdsa.sign(msg, private_key, hashfunc=sha3_256)
result4 = ecdsa.verify((r, s), msg, public_key, hashfunc=sha3_256)
print("\nDSA with ECC-P256 and SHA3-256")
print("r = ", r)
print("s = ", s)
print("verify result is :", result4)
