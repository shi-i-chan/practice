def tribonacci(signature, n):
    if n == 0:
        return []
    elif n < 3:
        return signature[0:n]
    
    for i in range(n - len(signature)):
        signature.append(sum(signature[-3:]))
    return signature
