// stores/NoteStore.js
import { defineStore } from "pinia"

export const useNoteStore = defineStore('noteStore', {
    state: () => ({
        notes: {},
        selectedNoteId: null
    }),
    getters: {
        selectedNote(state) {
            if (!state.selectedNoteId) return null
            return state.notes[state.selectedNoteId]
        }
    },
    actions: {
        async fetchNotes() {
            const res = await fetch("http://localhost:8002/notes")
            const data = await res.json()
            this.notes = data
        },
        deleteNote(noteId) {
            this.notes = Object.fromEntries(
                Object.entries(this.notes).filter(([id]) => id !== noteId)
            )
        },
        selectNote(id) {
            this.selectedNoteId = id
        }
    }
})
