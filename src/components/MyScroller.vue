<script setup>
import MyNote from './MyNote.vue'

const props = defineProps({
  notes: { type: Object, default: () => ({}) }
})


</script>

<template>
  <div class="llista-notes">
    <MyNote
      v-for="[noteId, nota] in Object.entries(notes)"
      :key="noteId"
      :note-id="noteId"
      :titol="nota.titol"
      :contingut="nota.contingut"
      :images="nota.images"
      :has-tasks="nota.has_tasks"
      :tasks-id="nota.tasks_id"
      :num-links="nota.num_links"
      :tags="nota.tags"
      :time="nota.time"
      :notebook="nota.notebook"
      :has-alarm="nota.has_alarm"
      :is-active="nota.isActive"
      :is-shared="nota.is_shared"
    />
  </div>
</template>


<style scoped>

.llista-notes {
    overflow-y: auto;
    -ms-overflow-style: none;
    scrollbar-width: none;
    flex: 1; /* Toma el espacio disponible */
    min-height: 0; /* CRÍTICO */
}

</style>