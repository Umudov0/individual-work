def asm_team(topic: list[str]) -> list[int]:
    results = [
        bin(int(a, 2) | int(b, 2)).count('1')
        for i, a in enumerate(topic)
        for b in topic[i + 1:]
    ]
    return [max(result), results.count(max(results))]