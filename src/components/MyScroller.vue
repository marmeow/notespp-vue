<script setup>
import MyNote from './MyNote.vue';

// rebem les notes com a prop del component pare
// IMPORTANT: afegim un valor per defecte {} per evitar errors
const props = defineProps({
  notes: {
    type: Object,
    default: () => ({}) // objecte buit per defecte
  }
});
</script>

<template>
  <div class="llista-notes">
    <!-- v-for amb Object.entries() per iterar sobre un objecte -->
    <!-- [noteId, nota] és la destructuració de cada entrada [clau, valor] -->
    <MyNote 
      v-for="[noteId, nota] in Object.entries(notes)" 
      :key="noteId"
      :note-id="noteId"
      :nota="nota"
    />
  </div>
</template>

<style scoped>
.llista-notes {
    overflow-y: scroll;
    -ms-overflow-style: none;
    scrollbar-width: none;
}

</style>