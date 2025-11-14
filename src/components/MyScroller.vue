<script setup>
import MyNote from './MyNote.vue';


const props = defineProps({
  notes: {
    type: Object,
    default: () => ({}) 
  }

});

// https://www.youtube.com/watch?v=Wz9mPaprSVw
const emit = defineEmits(['update:notes']);

const deleteNote = (noteId) => {
  const notesActualitzades = Object.fromEntries(
    Object.entries(props.notes).filter(([id]) => id !== noteId)
  );
    console.log(notesActualitzades);
  emit('update:notes', notesActualitzades); 
}


</script>

<template>
  <div class="llista-notes">
     <!-- Objecte notes a array k v, l bule es para ya enviar nota pot nota en lugar de todo un objeto de muchas notas  -->
    <MyNote 
      v-for="[noteId, nota] in Object.entries(notes)" 
      :key="noteId"
      :note-id="noteId"
      :nota="nota"
      @onDeleteClicked="deleteNote"
    />
  </div>
</template>

<style scoped>
.llista-notes {
  height: 100%;
    overflow-y: scroll;
    -ms-overflow-style: none;
    scrollbar-width: none;
}

</style>