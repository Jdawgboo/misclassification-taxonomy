from collections import Counter
def taxonomy(actual: list[str], predicted: list[str]) -> dict[str,int]:
 c=Counter(f'{a}->{p}' for a,p in zip(actual,predicted) if a!=p)
 return dict(sorted(c.items()))
