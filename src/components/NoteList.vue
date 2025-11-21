<script setup>
import { onMounted } from 'vue'
import MyButton from './MyButton.vue'
import FilterBar from './FilterBar.vue'
import MySelectButton from './MySelectButton.vue'
import MyScroller from './MyScroller.vue'
import { useNoteStore } from '../stores/NoteStore'

const noteStore = useNoteStore()

onMounted(async () => {
  await noteStore.fetchNotes()
  await noteStore.fetchAllTasks() 
})
</script>

<template>
  <section id="note-list">
    <div class="new-note flex">
      <h2>Notes</h2>
      <MyButton bg="white" color="var(--color-primary)" border="var(--border)" width="fit-content">
        <i class="fa fa-plus fa-sm"></i><span class="create"> Create New</span>
      </MyButton>
    </div>

    <div class="notes-info flex">
      <p><span class="num-notes">{{ Object.keys(noteStore.notes).length }}</span> Notes</p>
      <FilterBar />
    </div>

    <MySelectButton />
    <MyScroller :notes="noteStore.notes" />
  </section>
</template>


<style scoped>
#note-list {
    grid-area: note-list;
    display: flex;
    flex-direction: column;
    min-width: 0;
    max-width: 100%;
    height: 100%; /* Mantén 100% */
    color: black;
    overflow: hidden; /* Añade esto */
}

.new-note {
    border-bottom: var(--border);
    padding: 1.5625rem;
    display: flex;
    align-items: center;
    gap: 1.25rem;
    flex-shrink: 0; /* Evita que se comprima */
}

.notes-info {
    justify-content: space-around;
    font-weight: 600;
    font-size: 0.9375rem;
    border-bottom: var(--border);
    color: var(--color-secondary);
    padding: 0.625rem;
    flex-wrap: wrap;
    flex-shrink: 0; /* Evita que se comprima */
}

*::-webkit-scrollbar {
    display: none;
}


h2 {
    color: var(--color-accent);
    padding-right: 1.875rem;
    border-right: var(--border);
    margin: 0;
}


.num-notes {
    color: var(--color-accent);
    font-weight: bold;
}
</style>