<script setup>
import MyToolBar from './MyToolBar.vue'
import MyTask from './MyTask.vue'

import { useNoteStore } from '../stores/NoteStore'
import { computed } from 'vue'

const noteStore = useNoteStore()
const nota = computed(() => noteStore.notesWithTasks) // solo las tasks correctas



</script>

<template>
    <section id="notepanel">
        <MyToolBar />
        <section class="notebook" id="notebook">
            <div v-if="nota">
                <h2 class="note-title">{{ nota.titol }}</h2>
                <p>{{ nota.contingut }}</p>
                <MyTask v-for="task in nota.tasks" :key="task.id" :task-id="task.id" :titol="task.titol"
                    :is-done="task.is_done" :deadline="task.deadline_formatted" :reminder="task.reminder_formatted"
                    :tipus="task.tipus" />
            </div>
            <div v-else>
                <p>Pick a note</p>
            </div>
        </section>
    </section>
</template>

<style scoped>
#notepanel {
    grid-area: notepanel;
    height: 100%;
    border: var(--border);
    border-width: 0 1px;
    flex-direction: column;
    display: flex;
    background-color: white;
    overflow: hidden;
    color: black;
}

.notebook {
    padding: 0 2.5rem;
    overflow-y: auto;
    -ms-overflow-style: none;
    scrollbar-width: none;
    flex: 1;
    min-height: 0;
}


.info-notebook {
    justify-content: space-between;
}

.info-notebook p {
    color: var(--color-secondary);
    font-weight: 600;
}

.name h5 {
    margin-left: 0.3125rem;
    color: var(--color-accent);
    font-size: var(--font-main);
}

.note-content {
    padding: 0.3125rem 1.875rem;
}

.p-note {
    font-size: 1.0625rem;
    color: #575757;
    margin: 1rem 0px;
    line-height: 1.4;
}

.note-content a {
    color: #0859bc;
    font-size: 1.0625rem;
}

.note-content img {
    width: 100%;
    border-radius: var(--btn-radius);
    margin-bottom: 20px;
}

.close,
.closebtn {
    display: none;
}

.close {
    color: var(--color-primary);
    font-size: 1rem;
    border: none;
    cursor: pointer;
    padding: 0.3125rem;
    background-color: transparent;
    text-align: right;
}

.note-title {
    color: var(--color-accent);
    margin: 0;
    font-size: 1.875rem;
}
</style>