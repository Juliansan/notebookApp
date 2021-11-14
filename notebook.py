import datetime

# Store the next available id for all new notes
last_id = 0


class Note:
    """Represents a note in the notebook. Match against a
    string in searches and store tags for each note."""

    def __init__(self, memo, tags=""):
        """Initialize a note with memo and optional
        space-separated tags.Automatically set the note's
        creation date and unique id."""
        self.memo = memo
        self.creation_date = datetime.date.today()
        self.tags = tags
        global last_id
        last_id += 1
        self.id = last_id

    def match(self, filter):
        """Determine if this note matches the filter text.
        Returns True if it matches, False otherwise.

        Search in case sensitive and matches both text and tags."""
        return filter in self.memo or filter in self.tags


class Notebook:
    """Represents a collection of notes that can be tagged,
    modified, and searched."""

    def __init__(self):
        """Initializes a notebook with an empty list."""
        self.notes = []

    def new_note(self, memo, tags=""):
        """Create a new note and add it to the list."""
        self.notes.append(Note(memo, tags))

    def _find_notes(self, note_id):
        """Locate the note with the given id."""
        for note in self.notes:
            if str(note.id) == str(note_id):
                return note
            else:
                return None

    def modify_memo(self, note_id, memo):
        """find the note with the given id and change it's memo
        to the given value"""
        note = self._find_notes(note_id)
        if note:
            note.memo = memo
            return True
        return False

    def modify_tags(self, note_id, tags):
        """find the note with the given id and change it's tags
        to the given value"""
        note = self._find_notes(note_id)
        if note:
            note.tags = tags
            return True
        return False


    def search(self, filter):
        """Find all notes that match a given filter
        string."""
        return [note for note in self.notes if note.match(filter)]
