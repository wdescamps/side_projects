# Define common chords and their note structures for all 12 keys
chord_mapping = {
    'C Major': [60, 64, 67],
    'C Minor': [60, 63, 67],
    'C Diminished': [60, 63, 66],
    'C Augmented': [60, 64, 68],
    'C Major 7': [60, 64, 67, 71],
    'C Minor 7': [60, 63, 67, 70],
    'C Dominant 7': [60, 64, 67, 70],
    'C Diminished 7': [60, 63, 66, 69],
    # Repeat for all keys
    'C# Major': [61, 65, 68],
    'C# Minor': [61, 64, 68],
    'C# Diminished': [61, 64, 67],
    'C# Augmented': [61, 65, 69],
    'C# Major 7': [61, 65, 68, 72],
    'C# Minor 7': [61, 64, 68, 71],
    'C# Dominant 7': [61, 65, 68, 71],
    'C# Diminished 7': [61, 64, 67, 70],
    # Continue for all keys up to B
    'D Major': [62, 66, 69],
    'D Minor': [62, 65, 69],
    'D Diminished': [62, 65, 68],
    'D Augmented': [62, 66, 70],
    'D Major 7': [62, 66, 69, 73],
    'D Minor 7': [62, 65, 69, 72],
    'D Dominant 7': [62, 66, 69, 72],
    'D Diminished 7': [62, 65, 68, 71],
    'D# Major': [63, 67, 70],
    'D# Minor': [63, 66, 70],
    'D# Diminished': [63, 66, 69],
    'D# Augmented': [63, 67, 71],
    'D# Major 7': [63, 67, 70, 74],
    'D# Minor 7': [63, 66, 70, 73],
    'D# Dominant 7': [63, 67, 70, 73],
    'D# Diminished 7': [63, 66, 69, 72],
    'E Major': [64, 68, 71],
    'E Minor': [64, 67, 71],
    'E Diminished': [64, 67, 70],
    'E Augmented': [64, 68, 72],
    'E Major 7': [64, 68, 71, 75],
    'E Minor 7': [64, 67, 71, 74],
    'E Dominant 7': [64, 68, 71, 74],
    'E Diminished 7': [64, 67, 70, 73],
    'F Major': [65, 69, 72],
    'F Minor': [65, 68, 72],
    'F Diminished': [65, 68, 71],
    'F Augmented': [65, 69, 73],
    'F Major 7': [65, 69, 72, 76],
    'F Minor 7': [65, 68, 72, 75],
    'F Dominant 7': [65, 69, 72, 75],
    'F Diminished 7': [65, 68, 71, 74],
    'F# Major': [66, 70, 73],
    'F# Minor': [66, 69, 73],
    'F# Diminished': [66, 69, 72],
    'F# Augmented': [66, 70, 74],
    'F# Major 7': [66, 70, 73, 77],
    'F# Minor 7': [66, 69, 73, 76],
    'F# Dominant 7': [66, 70, 73, 76],
    'F# Diminished 7': [66, 69, 72, 75],
    'G Major': [67, 71, 74],
    'G Minor': [67, 70, 74],
    'G Diminished': [67, 70, 73],
    'G Augmented': [67, 71, 75],
    'G Major 7': [67, 71, 74, 78],
    'G Minor 7': [67, 70, 74, 77],
    'G Dominant 7': [67, 71, 74, 77],
    'G Diminished 7': [67, 70, 73, 76],
    'G# Major': [68, 72, 75],
    'G# Minor': [68, 71, 75],
    'G# Diminished': [68, 71, 74],
    'G# Augmented': [68, 72, 76],
    'G# Major 7': [68, 72, 75, 79],
    'G# Minor 7': [68, 71, 75, 78],
    'G# Dominant 7': [68, 72, 75, 78],
    'G# Diminished 7': [68, 71, 74, 77],
    'A Major': [69, 73, 76],
    'A Minor': [69, 72, 76],
    'A Diminished': [69, 72, 75],
    'A Augmented': [69, 73, 77],
    'A Major 7': [69, 73, 76, 80],
    'A Minor 7': [69, 72, 76, 79],
    'A Dominant 7': [69, 73, 76, 79],
    'A Diminished 7': [69, 72, 75, 78],
    'A# Major': [70, 74, 77],
    'A# Minor': [70, 73, 77],
    'A# Diminished': [70, 73, 76],
    'A# Augmented': [70, 74, 78],
    'A# Major 7': [70, 74, 77, 81],
    'A# Minor 7': [70, 73, 77, 80],
    'A# Dominant 7': [70, 74, 77, 80],
    'A# Diminished 7': [70, 73, 76, 79],
    'B Major': [71, 75, 78],
    'B Minor': [71, 74, 78],
    'B Diminished': [71, 74, 77],
    'B Augmented': [71, 75, 79],
    'B Major 7': [71, 75, 78, 82],
    'B Minor 7': [71, 74, 78, 81],
    'B Dominant 7': [71, 75, 78, 81],
    'B Diminished 7': [71, 74, 77, 80]
}

CHORD_INTERVALS = {
    'major': {
        'root': [0, 4, 7],
        '1st_inversion': [4, 7, 12],
        '2nd_inversion': [7, 12, 16],
    },
    'minor': {
        'root': [0, 3, 7],
        '1st_inversion': [3, 7, 12],
        '2nd_inversion': [7, 12, 15],
    },
    'diminished': {
        'root': [0, 3, 6],
        '1st_inversion': [3, 6, 9],
        '2nd_inversion': [6, 9, 12],
    },
    'augmented': {
        'root': [0, 4, 8],
        '1st_inversion': [4, 8, 12],
        '2nd_inversion': [8, 12, 16],
    },
    'sus2': {
        'root': [0, 2, 7],
        '1st_inversion': [2, 7, 12],
        '2nd_inversion': [7, 12, 14],
    },
    'sus4': {
        'root': [0, 5, 7],
        '1st_inversion': [5, 7, 12],
        '2nd_inversion': [7, 12, 17],
    },
    'add9': {
        'root': [0, 4, 7, 14],
        '1st_inversion': [4, 7, 14, 16],
        '2nd_inversion': [7, 14, 16, 19],
    },
    'add11': {
        'root': [0, 4, 7, 17],
        '1st_inversion': [4, 7, 17, 19],
        '2nd_inversion': [7, 17, 19, 23],
    },
    'major_6': {
        'root': [0, 4, 7, 9],
        '1st_inversion': [4, 7, 9, 12],
        '2nd_inversion': [7, 9, 12, 16],
    },
    'minor_6': {
        'root': [0, 3, 7, 9],
        '1st_inversion': [3, 7, 9, 12],
        '2nd_inversion': [7, 9, 12, 15],
    },
    'major_7': {
        'root': [0, 4, 7, 11],
        '1st_inversion': [4, 7, 11, 12],
        '2nd_inversion': [7, 11, 12, 16],
    },
    'minor_7': {
        'root': [0, 3, 7, 10],
        '1st_inversion': [3, 7, 10, 12],
        '2nd_inversion': [7, 10, 12, 15],
    },
    'dominant_7': {
        'root': [0, 4, 7, 10],
        '1st_inversion': [4, 7, 10, 12],
        '2nd_inversion': [7, 10, 12, 16],
    },
    'diminished_7': {
        'root': [0, 3, 6, 9],
        '1st_inversion': [3, 6, 9, 12],
        '2nd_inversion': [6, 9, 12, 15],
    },
    'half_diminished_7': {
        'root': [0, 3, 6, 10],
        '1st_inversion': [3, 6, 10, 12],
        '2nd_inversion': [6, 10, 12, 15],
    },
    'minor_major_7': {
        'root': [0, 3, 7, 11],
        '1st_inversion': [3, 7, 11, 12],
        '2nd_inversion': [7, 11, 12, 15],
    },
    'major_9': {
        'root': [0, 4, 7, 11, 14],
        '1st_inversion': [4, 7, 11, 14, 16],
        '2nd_inversion': [7, 11, 14, 16, 19],
    },
    'minor_9': {
        'root': [0, 3, 7, 10, 14],
        '1st_inversion': [3, 7, 10, 14, 15],
        '2nd_inversion': [7, 10, 14, 15, 19],
    },
    'dominant_9': {
        'root': [0, 4, 7, 10, 14],
        '1st_inversion': [4, 7, 10, 14, 16],
        '2nd_inversion': [7, 10, 14, 16, 19],
    },
    'minor_11': {
        'root': [0, 3, 7, 10, 14, 17],
        '1st_inversion': [3, 7, 10, 14, 17, 19],
        '2nd_inversion': [7, 10, 14, 17, 19, 21],
    },
    'dominant_11': {
        'root': [0, 4, 7, 10, 14, 17],
        '1st_inversion': [4, 7, 10, 14, 17, 19],
        '2nd_inversion': [7, 10, 14, 17, 19, 21],
    },
    'major_13': {
        'root': [0, 4, 7, 11, 14, 21],
        '1st_inversion': [4, 7, 11, 14, 21, 24],
        '2nd_inversion': [7, 11, 14, 21, 24, 28],
    },
    'minor_13': {
        'root': [0, 3, 7, 10, 14, 21],
        '1st_inversion': [3, 7, 10, 14, 21, 24],
        '2nd_inversion': [7, 10, 14, 21, 24, 27],
    },
    'dominant_13': {
        'root': [0, 4, 7, 10, 14, 21],
        '1st_inversion': [4, 7, 10, 14, 21, 24],
        '2nd_inversion': [7, 10, 14, 21, 24, 28],
    },
    'augmented_7': {
        'root': [0, 4, 8, 10],
        '1st_inversion': [4, 8, 10, 12],
        '2nd_inversion': [8, 10, 12, 16],
    },
    'augmented_major_7': {
        'root': [0, 4, 8, 11],
        '1st_inversion': [4, 8, 11, 12],
        '2nd_inversion': [8, 11, 12, 16],
    },
    'dominant_7_b5': {
        'root': [0, 4, 6, 10],
        '1st_inversion': [4, 6, 10, 12],
        '2nd_inversion': [6, 10, 12, 16],
    },
    'dominant_7_sharp5': {
        'root': [0, 4, 8, 10],
        '1st_inversion': [4, 8, 10, 12],
        '2nd_inversion': [8, 10, 12, 16],
    },
    'dominant_7_b9': {
        'root': [0, 4, 7, 10, 13],
        '1st_inversion': [4, 7, 10, 13, 14],
        '2nd_inversion': [7, 10, 13, 14, 17],
    },
    'dominant_7_sharp9': {
        'root': [0, 4, 7, 10, 15],
        '1st_inversion': [4, 7, 10, 15, 16],
        '2nd_inversion': [7, 10, 15, 16, 19],
    },
    'dominant_7_b5_b9': {
        'root': [0, 4, 6, 10, 13],
        '1st_inversion': [4, 6, 10, 13, 14],
        '2nd_inversion': [6, 10, 13, 14, 17],
    },
    'dominant_7_sharp5_sharp9': {
        'root': [0, 4, 8, 10, 15],
        '1st_inversion': [4, 8, 10, 15, 16],
        '2nd_inversion': [8, 10, 15, 16, 19],
    },
    }