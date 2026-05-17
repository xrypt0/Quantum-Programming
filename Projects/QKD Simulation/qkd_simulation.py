import sys
sys.stdout.reconfigure(encoding='utf-8')

import random

def simulate_qkd(num_bits=10, eve_active=False):
    alice_bits = [random.randint(0, 1) for _ in range(num_bits)]
    alice_bases = [random.choice(['Z', 'X']) for _ in range(num_bits)]
    bob_bases = [random.choice(['Z', 'X']) for _ in range(num_bits)]
    
    eve_bases = []
    eve_bits = []
    bob_bits = []
    
    if eve_active:
        eve_bases = [random.choice(['Z', 'X']) for _ in range(num_bits)]
        for i in range(num_bits):
            if eve_bases[i] == alice_bases[i]:
                eve_bit = alice_bits[i]
            else:
                eve_bit = random.randint(0, 1)
            eve_bits.append(eve_bit)
            
            if bob_bases[i] == eve_bases[i]:
                bob_bit = eve_bit
            else:
                bob_bit = random.randint(0, 1)
            bob_bits.append(bob_bit)
    else:
        for i in range(num_bits):
            if bob_bases[i] == alice_bases[i]:
                bob_bit = alice_bits[i]
            else:
                bob_bit = random.randint(0, 1)
            bob_bits.append(bob_bit)
            
    matching_indices = []
    shared_key_alice = []
    shared_key_bob = []
    
    for i in range(num_bits):
        if alice_bases[i] == bob_bases[i]:
            matching_indices.append(i)
            shared_key_alice.append(alice_bits[i])
            shared_key_bob.append(bob_bits[i])
            
    return alice_bits, alice_bases, eve_bases, eve_bits, bob_bases, bob_bits, matching_indices, shared_key_alice, shared_key_bob
