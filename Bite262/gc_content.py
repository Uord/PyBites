def calculate_gc_content(sequence):
    """
    Receives a DNA sequence (A, G, C, or T)
    Returns the percentage of GC content (rounded to the last two digits)
    """
    sequence = sequence.upper()
    sequence = "".join(filter(str.isalpha, sequence))
    return round(
        (sequence.count("G") + sequence.count("C"))
        / (
            sequence.count("G")
            + sequence.count("C")
            + sequence.count("A")
            + sequence.count("T")
        )
        * 100,
        2,
    )
