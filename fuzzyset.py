class FuzzySet:
    def __init__(self, members):
        self.members = members

    def union(self, other_set):
        union_result = {}
        for key in self.members:
            union_result[key] = max(self.members[key], other_set.members.get(key, 0))
        for key in other_set.members:
            if key not in union_result:
                union_result[key] = other_set.members[key]
        return FuzzySet(union_result)

    def intersection(self, other_set):
        intersection_result = {}
        for key in self.members:
            if key in other_set.members:
                intersection_result[key] = min(self.members[key], other_set.members[key])
        return FuzzySet(intersection_result)

    def complement(self):
        complement_result = {key: 1 - self.members[key] for key in self.members}
        return FuzzySet(complement_result)

    def print_fuzzy_set(self, label):
        print(f"Fuzzy Set {label}: {self.members}")


# Example usage
set_A = FuzzySet({"a": 0.6, "b": 0.3, "c": 0.8})
set_B = FuzzySet({"a": 0.4, "b": 0.7, "d": 0.5})

set_A.print_fuzzy_set("A")
set_B.print_fuzzy_set("B")

# Union of sets A and B
set_union = set_A.union(set_B)
set_union.print_fuzzy_set("Union(A, B)")

# Intersection of sets A and B
set_intersection = set_A.intersection(set_B)
set_intersection.print_fuzzy_set("Intersection(A, B)")

# Complement of set A
set_A_complement = set_A.complement()
set_A_complement.print_fuzzy_set("Complement(A)")

# Complement of set B
set_B_complement = set_B.complement()
set_B_complement.print_fuzzy_set("Complement(B)")

