from midiutil import MIDIFile

def create_dual_hand_midi(
    right_hand,
    left_hand,
    output_file='piano.mid',
    tempo=120,
    right_instrument=0,  # 0 = Acoustic Grand Piano
    left_instrument=0,
    right_channel=0,
    left_channel=1,
    volume=100
):
    """
    Creates MIDI with independent left/right hands
    
    Format requirements:
    - Each hand is a list of events: [(pitch, duration), ...]
    - pitch = single int | list of ints | None (for rest)
    - durations in beats
    
    MIDI Implementation:
    - Hands on separate MIDI channels (0 and 1)
    """
    
    # Check required: MIDIFile expects a track number when using addTempo/addProgramChange.
    # Since we are using a single track (track 0), this is correct.
    midi = MIDIFile(1)  # Single track, multiple channels
    
    # Setup track 0 and tempo
    midi.addTempo(0, 0, tempo)
    
    # Program changes for each hand/channel
    midi.addProgramChange(0, right_channel, 0, right_instrument)
    
    # Only add program change for left channel if left_hand data exists
    if left_hand:
        midi.addProgramChange(0, left_channel, 0, left_instrument)
    
    # Process hands independently
    # We use tuples for iteration. If a hand list is empty, we still process it, 
    # but the loop inside won't run. We only skip if the input list was None (though unlikely based on usage).
    hand_data = [
        (right_hand, right_channel),
        (left_hand, left_channel) 
    ]
    
    for hand, channel in hand_data:
        # Skip if the hand list was explicitly None, or if it's empty (the loop below handles empty lists fine)
        if not hand:
            continue
            
        current_time = 0
        for event in hand:
            # event should be (pitches, duration)
            if len(event) != 2:
                 print(f"Warning: Skipping malformed event in channel {channel}: {event}")
                 continue
                 
            pitches, duration = event
            
            # --- TIME BUG FIX START ---
            # 1. Note start time is the current_time BEFORE advancing.
            note_start_time = current_time
            
            # 2. Advance time based on the duration of this event (the time the *next* event starts)
            current_time += duration
            # --- TIME BUG FIX END ---
            
            if pitches is None:  # Rest: Time has already been advanced above
                continue
                
            if not isinstance(pitches, list):
                pitches = [pitches]
                
            for pitch in pitches:
                midi.addNote(
                    track=0,
                    channel=channel,
                    pitch=pitch,
                    time=note_start_time,  # Use the time calculated *before* advancing
                    duration=duration,
                    volume=volume
                )
    
    # Ensure output file is opened in binary write mode
    with open(output_file, 'wb') as f:
        midi.writeFile(f)
    print(f"Generated: {output_file}")

# Usage Example
if __name__ == '__main__':

    treble = []
    bass = []


    create_dual_hand_midi(
        right_hand=treble,
        left_hand=bass,
        output_file='duet.mid',
        right_instrument=0,    # Piano
        left_instrument=0,     # Same piano sound
        tempo=90
    )