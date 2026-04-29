from Bio import SeqIO
from Bio.Seq import Seq
from random import randint, choice

# Task 1: Load sequence from a file in the inputs directory
def load_sequence(filepath):
    """
    Pseudocode:
    - Use SeqIO to read the file in GenBank format.
    - Print the sequence ID.
    - Check if the sequence is defined or non-empty:
        - If valid, print the sequence.
        - Otherwise, print a message and assign an empty sequence.
    - Return the sequence record.
    """
    try:
        record = SeqIO.read(filepath, "genbank")
        print(f"ID sekvencie: {record.id}")
        if len(record.seq) > 0:
            print(f"Sekvencia: {record.seq[:50]}...")
        else:
            print("Sekvencia nie je definovaná alebo je prázdna.")
            record.seq = Seq("")
        return record
    except Exception as e:
        print(f"Chyba pri načítaní: {e}")
        return None

# Task 2: Create complementary strand
def create_complementary_strand(dna_sequence):
    """
    Pseudocode:
    - Create a translation table for DNA base complements (A <-> T, G <-> C).
    - Translate the input DNA sequence using the complement table.
    - Print the complementary strand.
    - Return the complementary strand.
    """
    trans_table = str.maketrans("ATGC", "TACG")
    complement_sequence = dna_sequence.translate(trans_table)
    print(f"Komplementárna sekvencia: {complement_sequence}")
    return complement_sequence

# Task 3: Create gene mutation
def mutate(dna):
    """
    Pseudocode:
    - Convert the DNA sequence into a list of characters.
    - Perform 1000 random mutations:
        - Select a random index in the DNA sequence.
        - Replace the base at the selected index with a random different base.
    - Join the mutated list back into a string.
    - Print the mutated DNA sequence.
    - Return the mutated DNA sequence.
    """
    dna_list = list(str(dna))
    bases = ['A', 'T', 'G', 'C']
    for _ in range(1000):
        idx = randint(0, len(dna_list) - 1)
        current_base = dna_list[idx]
        new_base = choice([b for b in bases if b != current_base])
        dna_list[idx] = new_base
    mutated_sequence = "".join(dna_list)
    print(f"Zmutovaná sekvencia: {mutated_sequence[:50]}...")
    return mutated_sequence

# Task 4: Calculate GC content
def calculate_gc_content(dna_sequence):
    """
    Pseudocode:
    - Count the occurrences of 'G' and 'C' in the DNA sequence.
    - Calculate the GC content as a percentage of the total sequence length.
    - Print the GC content percentage.
    - Return the GC content percentage.
    """
    count_g = dna_sequence.count("G")
    count_c = dna_sequence.count("C")
    total_length = len(dna_sequence)
    gc_content = (count_g + count_c) / total_length * 100 if total_length > 0 else 0
    print(f"GC podiel: {gc_content:.2f}%")
    return gc_content

# Example usage
if __name__ == "__main__":
    # Task 1: Load sequence from the inputs directory
    sequence_record = load_sequence("inputs/NC_005816.gb")

    # Task 2: Create complementary strand
    create_complementary_strand("TACCGGAT")

    # Task 3: Mutate a sequence loaded from the inputs directory
    fasta_sequence = SeqIO.read("inputs/AE017046.1.fasta", "fasta").seq
    mutated_sequence = mutate(str(fasta_sequence))

    # Task 4: Calculate GC content
    calculate_gc_content(str(fasta_sequence))