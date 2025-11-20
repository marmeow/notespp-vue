import { defineStore } from "pinia"


export const useNoteStore = defineStore('noteStore', {
    state: () => ({
        notes: {},
        tasksNota: {},
        selectedNoteId: null
    }),
    getters: {
        selectedNote(state) {
            if (!state.selectedNoteId) return null
            return state.notes[state.selectedNoteId]
        },
        notesWithTasks(state) {
            if (!state.selectedNoteId) return null
            const note = state.notes[state.selectedNoteId]
            if (!note) return null


            return {
                ...note, // meter tasks en nota 
                tasks: state.tasksNota[state.selectedNoteId] || []
            }
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
        async selectNote(id) {
            this.selectedNoteId = id
            await this.fetchTasksForNote(id)  // Agregar esta línea
        },
        async fetchTasksForNote(noteId) {
            const res = await fetch(`http://localhost:8002/notes/${noteId}/tasks`)
            const data = await res.json()
            this.tasksNota[noteId] = data
        }
    }
})
