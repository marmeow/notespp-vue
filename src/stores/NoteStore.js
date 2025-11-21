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
            const nota = await res.json()
            this.notes = nota
        },
        deleteNote(noteId) {
            this.notes = Object.fromEntries(
                Object.entries(this.notes).filter(([id]) => id !== noteId)
            )
        },
        async selectNote(id) {
            this.selectedNoteId = id
            await this.fetchTasksForNote(id)
        },
        async fetchTasksForNote(noteId) {
            const res = await fetch(`http://localhost:8002/notes/${noteId}/tasks`)
            const task = await res.json()
            this.tasksNota[noteId] = task
        },
        async fetchAllTasks() {
            const noteIds = Object.keys(this.notes)
            await Promise.all(
                noteIds.map(id => this.fetchTasksForNote(id))
            )
        },
        async updateTask(noteId, taskId, isDone) {
            const res = await fetch(`http://localhost:8002/notes/${noteId}/tasks/${taskId}`, {
                method: "PATCH", // Usa PATCH en lugar de PUT
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify({ is_done: isDone }),
            })

            const tasks = this.tasksNota[noteId] || []
            this.tasksNota[noteId] = tasks.map(task =>
                task.id === taskId ? { ...task, is_done: isDone } : task
            )
        }




    }
})
