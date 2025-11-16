import math
from fractions import Fraction
import networkx as nx

class TriadicRelationalFramework:
    def __init__(self):
        pass # No initial state needed for basic implementation
    
    def compute_triad(self, C1, C2, C3, a, b):
        """
        Compute the triadic relational transformation.
        
        Parameters:
        - C1, C2, C3: Input integer concepts
        - a, b: Positive integer balancing coefficients (minimal, co-prime)
        
        Returns:
        - C4: The computed output integer
        - K: The simplicity constant (Fraction: 1 / (a * b))
        - steps: Dictionary with intermediate steps for transparency
        """
        if not all(isinstance(x, int) and x > 0 for x in [C1, C2, C3, a, b]):
            raise ValueError("All inputs must be positive integers.")
        
        steps = {}
        
        # Step 1: Input Concepts
        steps['inputs'] = {'C1': C1, 'C2': C2, 'C3': C3, 'a': a, 'b': b}
        
        # Step 2: Normalization
        gcd_in = math.gcd(C1, C2, C3)
        C1_prime = C1 // gcd_in
        C2_prime = C2 // gcd_in
        C3_prime = C3 // gcd_in
        steps['normalization'] = {'gcd_in': gcd_in, 'C1_prime': C1_prime, 'C2_prime': C2_prime, 'C3_prime': C3_prime}
        
        # Step 3: Relational Transformation (Phi)
        numerator = a * C2_prime * C3_prime
        denominator = b * C1_prime
        C4_prime = Fraction(numerator, denominator)
        steps['transformation'] = {'C4_prime': str(C4_prime)}
        
        # Step 4: Denormalization
        C4 = C4_prime * gcd_in
        if C4.denominator != 1:
            raise ValueError("The balancing does not result in an integer C4_prime. Adjust a, b or inputs.")
        C4 = int(C4) # Convert to int if integer
        steps['denormalization'] = {'C4': C4}
        
        # Simplicity K
        K = Fraction(1, a * b)
        steps['K'] = str(K)
        
        return C4, K, steps
    
    def analogy_variant(self, C1, C2, C3):
        """
        Variant for analogies like King:Man :: Queen:Woman, which is C4 = (C1 * C3) / C2.
        Assumes a=1, b=1, but adjusted order.
        
        Parameters:
        - C1: Starting concept (e.g., King)
        - C2: To remove (e.g., Man/Male)
        - C3: To add (e.g., Woman/Female)
        
        Returns:
        - C4: Predicted concept (e.g., Queen)
        - steps: Dictionary with intermediate steps
        """
        if not all(isinstance(x, int) and x > 0 for x in [C1, C2, C3]):
            raise ValueError("All inputs must be positive integers.")
        
        steps = {}
        
        # Normalization (over inputs)
        gcd_in = math.gcd(C1, C2, C3)
        C1_prime = C1 // gcd_in
        C2_prime = C2 // gcd_in
        C3_prime = C3 // gcd_in
        steps['normalization'] = {'gcd_in': gcd_in, 'C1_prime': C1_prime, 'C2_prime': C2_prime, 'C3_prime': C3_prime}
        
        # Analogy transformation: C4_prime = (C1_prime * C3_prime) / C2_prime
        numerator = C1_prime * C3_prime
        C4_prime = Fraction(numerator, C2_prime)
        steps['transformation'] = {'C4_prime': str(C4_prime)}
        
        # Denormalization
        C4 = C4_prime * gcd_in
        if C4.denominator != 1:
            raise ValueError("The analogy does not result in an integer output. Check attribute mappings.")
        C4 = int(C4) # Convert to int if integer
        steps['denormalization'] = {'C4': C4}
        
        # For analogy, a=1, b=1 implicitly
        K = Fraction(1, 1) # 1.0 as Fraction
        steps['K'] = str(K)
        
        return C4, K, steps
    
    def check_static_balance(self, C1, C2, C3, C4):
        """
        Check static balance for existing formula (find minimal co-prime a,b such that a C2' C3' = b C1' C4').
        
        Parameters:
        - C1, C2, C3, C4: Positive integers
        
        Returns:
        - a, b: Minimal co-prime balancing coefficients
        - K: Simplicity (1 / (a * b))
        - steps: Dictionary with steps
        """
        if not all(isinstance(x, int) and x > 0 for x in [C1, C2, C3, C4]):
            raise ValueError("All inputs must be positive integers.")
        
        steps = {'inputs': {'C1': C1, 'C2': C2, 'C3': C3, 'C4': C4}}
        
        gcd_in = math.gcd(C1, C2, C3, C4)
        C1_prime = C1 // gcd_in
        C2_prime = C2 // gcd_in
        C3_prime = C3 // gcd_in
        C4_prime = C4 // gcd_in
        steps['normalization'] = {'gcd_in': gcd_in, 'C1_prime': C1_prime, 'C2_prime': C2_prime,
            'C3_prime': C3_prime, 'C4_prime': C4_prime}
        
        ratio = Fraction(C1_prime * C4_prime, C2_prime * C3_prime)
        a = ratio.numerator
        b = ratio.denominator
        gcd_ab = math.gcd(a, b)
        a //= gcd_ab
        b //= gcd_ab
        steps['balancing'] = {'a': a, 'b': b}
        
        K = Fraction(1, a * b)
        steps['K'] = str(K)
        
        return a, b, K, steps
    
    def chain_triads(self, initial_C1, triad_list):
        """
        Chain multiple triads: Each triad is (C2, C3, a, b). Output of one is C1 for next.
        
        Parameters:
        - initial_C1: Starting C1
        - triad_list: List of tuples [(C2, C3, a, b), ...]
        
        Returns:
        - final_C4: Final output
        - all_K: List of Ks
        - all_steps: List of steps dicts
        """
        current_C1 = initial_C1
        all_K = []
        all_steps = []
        for C2, C3, a, b in triad_list:
            C4, K, steps = self.compute_triad(current_C1, C2, C3, a, b)
            all_K.append(K)
            all_steps.append(steps)
            current_C1 = C4 # Chain
        return current_C1, all_K, all_steps

class TriadicNetwork:
    def __init__(self):
        self.graph = nx.DiGraph() # Directed for chaining
    
    def add_triad(self, triad_id, C1, C2, C3, a, b):
        framework = TriadicRelationalFramework()
        _, K, _ = framework.compute_triad(C1, C2, C3, a, b)
        self.graph.add_node(triad_id, K=K)
    
    def add_connection(self, from_id, to_id):
        if from_id in self.graph and to_id in self.graph:
            w = self.graph.nodes[from_id]['K'] # Weight = K of from
            self.graph.add_edge(from_id, to_id, weight=w)
    
    def visualize(self):
        # Manual print for compatibility with networkx >=3.0
        print(f"Graph with {self.graph.number_of_nodes()} nodes and {self.graph.number_of_edges()} edges")
        for node, data in self.graph.nodes(data=True):
            print(f"Node {node}: {data}")
        for from_node, to_node, data in self.graph.edges(data=True):
            print(f"Edge {from_node} -> {to_node}, weight: {data['weight']}")

# Example Usage and Tests
framework = TriadicRelationalFramework()

# Test 1: Abstract Numerical Example from Paper
C4, K, steps = framework.compute_triad(18, 6, 8, 3, 4)
print("Abstract Example:")
print(f"C4: {C4}, K: {K}")
print("Steps:", steps)

# Test 2: King-Queen Analogy with Primes
C4_analogy, K_analogy, steps_analogy = framework.analogy_variant(21, 3, 5)
print("\nKing-Queen Analogy:")
print(f"C4 (Queen): {C4_analogy}, K: {K_analogy}")
print("Steps:", steps_analogy)

# Test 3: Static Balance (e.g., 2 KE = m v^2, dummy values KE=1, m=1, v^2=2, 'C4' as placeholder for balance)
a, b, K_static, steps_static = framework.check_static_balance(1, 1, 2, 1) # Should give a=1, b=2
print("\nStatic Balance Example:")
print(f"a: {a}, b: {b}, K: {K_static}")
print("Steps:", steps_static)

# Test 4: Chaining (from paper example)
final_C, Ks, steps_list = framework.chain_triads(18, [(6, 8, 3, 4), (5, 10, 1, 1)])
print("\nChaining Example:")
print(f"Final C: {final_C}, Ks: {Ks}")
print("Steps List:", steps_list)

# Test 5: Network Example
net = TriadicNetwork()
net.add_triad('Delta1', 18, 6, 8, 3, 4)
net.add_triad('Delta2', 2, 5, 10, 1, 1)
net.add_connection('Delta1', 'Delta2')
print("\nNetwork Example:")
net.visualize()

# Fractional Example (e.g., approx pi in circumference C = 2pir approx 2*(22/7)r)
# Predict r from C=44, dummy C2=1, C3=1, a=7, b=44 (inverted for demo; this will raise since not integer)
try:
    C4_frac, K_frac, steps_frac = framework.compute_triad(44, 1, 1, 7, 44)
    print("\nFractional Example (pi approx):")
    print(f"C4 (approx r): {C4_frac}, K: {K_frac}")
except ValueError as e:
    print(f"\nFractional Example Error (expected for non-integer): {e}")