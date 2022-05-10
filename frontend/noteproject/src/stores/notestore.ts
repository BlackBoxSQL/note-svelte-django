/** create a store for notes */

class NoteStore {
	private _notes: Note[] = [];

	constructor() {
		this._notes = [];
	}

	public get notes(): Note[] {
		return this._notes;
	}

	public addNote(note: Note): void {
		this._notes.push(note);
	}

	public removeNote(note: Note): void {
		const index = this._notes.indexOf(note);
		if (index > -1) {
			this._notes.splice(index, 1);
		}
	}

	public updateNote(note: Note): void {
		const index = this._notes.indexOf(note);
		if (index > -1) {
			this._notes[index] = note;
		}
	}
}

export default NoteStore;
