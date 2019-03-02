## Pynacl memory usage tester

### Encryption
```
pipenv run python -m memory_profiler main encrypt ./test-img.jpg encrypted
```

### Decryption
```
pipenv run python -m memory_profiler main decrypt encrypted ./test-img-decrypted.jpg
```
