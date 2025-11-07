from midiutil import MIDIFile

def create_midi_from_notes(notes_array, output_file='output.mid', tempo=120, instrument=0):
    """
    Create MIDI file supporting chords, rests, and monophonic lines
    
    Parameters:
    - notes_array: List of events where each event is:
        (pitch, duration)              -> Single note
        ([p1, p2, ...], duration)      -> Chord
        (None, duration)               -> Rest
        
    - Other parameters same as before
    """
    
    midi = MIDIFile(1)
    midi.addTempo(0, 0, tempo)
    midi.addProgramChange(0, 0, 0, instrument)
    
    current_time = 0
    
    for event in notes_array:
        pitches, duration = event
        
        # Add notes if not rest
        if pitches is not None:
            # Ensure we handle both chords and single notes
            if not isinstance(pitches, list):
                pitches = [pitches]
                
            for pitch in pitches:
                midi.addNote(
                    track=0,
                    channel=0,
                    pitch=pitch,
                    time=current_time,
                    duration=duration,
                    volume=100
                )
        
        current_time += duration
    
    with open(output_file, "wb") as f:
        midi.writeFile(f)
    print(f"Generated: {output_file}")

# Usage Example with Chords and Rests
if __name__ == "__main__":

    ## Enter your array ->
    melody = []
    
    create_midi_from_notes(melody, "melody.mid", tempo=90)