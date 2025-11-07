Hello! I have Python midi generator.

Create a MIDI-compatible melody array in Python tuple format meeting these specifications:

1. **Duration**: 120 seconds at 90 BPM - medium speed melody.
2. **Musical Characteristics**:
   - Key: E minor (harmonic minor scale modulations)
   - THE MOST IMPORTANT: The melody should contain a motif that develops throughout the entire melody! The melody should be interesting and have a beginning, a plot, a resolution, a climax, and an epic ending.
   - Techniques:
     * Syncopated arpeggios
     * Chromatic passing tones
     * Triplet grace notes
     * Mordent ornaments
     * Modal interchange (Phrygian dominant)
   - Dynamic contrast (pp to ff implied via velocity changes)
3. **Format Requirements**:
   - Strict Python list of tuples: `[(pitch, duration), ...]`
   - Use MIDI note numbers (60=C4)
   - You can use "None, duration" as pause in melody!
   - You can create accords (or two-hand) using [] on pitch : [60, 64, 67] - its play 3 notes
   - NO MARKDOWN - raw code only
   - NO STRING - notes numbers and durations only
4. **Avoid**:
   - Predictable 4-bar patterns
   - Diatonic-only harmony
   - Monotonic dynamics

Generate: 1) Array

Example (fast melody):

```
melody = [
        ([60, 64, 67], 0.5),
        (None, 0.25),
        ([59, 62, 67], 0.25),
        
        (72, 0.25), (76, 0.25), (79, 0.25), (72, 0.25),
        
        ([65, 69, 72], 1.5),
        (64, 0.5),

]
```

Give me the entire melody in one array. Thanks.