Create 120 seconds at 120 BPM duration melody, having a developing motif throughout the entire melody. At least 200 notes for each hand.
Generate separate python ARRAYS for treble (right hand) and bass (left hand):

Right Hand Requirements:
- Bass Accords

Left Hand Requirements:
- Solid rhythmic foundation
- Sparse but deliberate note placement

Format:
   - Strict Python list of tuples: `[(pitch, duration), ...]`
   - Use MIDI note numbers (60=C4)
   - Duration is indicated in seconds (0.125, 0.5, etc.)!
   - You can use "None, duration" as pause in melody!
   - You can create accords using [] on pitch : [60, 64, 67] - its play 3 notes
   - No comments (#...)
   - NO MARKDOWN - raw code only
   - NO STRING - notes numbers and durations only
   - NO SCRIPTS - ARRAYS ONLY!

Format Example:

treble = [
    # Baroque-style decoration
    ([67, 71], 0.5),       # G5 + B5 chord
    (72, 0.25), (71, 0.25),# C6 + B5 
    # ... continuing pattern ...
]

bass = [
    (48, 1.5),             # C3 dotted half
    (43, 0.5),             # G2
    # ... harmonic foundation ...
]

Each hand maintains its own duration counter.
No need to synchronize event timing across hands.

Print ONLY RAW ARRAYS!

