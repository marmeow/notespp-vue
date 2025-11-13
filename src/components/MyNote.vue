<script setup>
import { computed } from 'vue';

// Guardem les props en una variable per poder-les usar
const props = defineProps({
  noteId: {
    type: String,
    required: true
  },
  nota: {
    type: Object,
    required: true
  }
});

// Creem la URL de la imatge basant-nos en l'ID si has_img és true
const imageUrl = computed(() => {
  if (props.nota.has_img) {
    // Ajusta aquesta URL segons com tinguis les imatges al backend
    return `http://localhost:8002/images/${props.noteId}.jpg`;
    // O potser: return `/assets/notes/${props.noteId}.jpg`;
  }
  return null;
});

console.log('Nota:', props.nota);
console.log('Has imatge:', props.nota.has_img);
console.log('Image URL:', imageUrl.value);
</script>

<template>
  <article class="nota flex" :data-id="noteId" :class="{ active: nota.isActive }">
    <div class="text-note">
      <div class="inner">
        <h3 class="note-title">{{ nota.titol }}</h3>
        <p class="note-preview">{{ nota.contingut.slice(0, 70) }}.</p>
        
        <div class="details-time flex">
          <div class="details flex">
            <!-- Tasks -->
            <div v-if="nota.has_tasks" class="detail flex">
              <i class="fa-solid fa-list-check fa-sm text-secondary"></i>
              <p class="task-num">{{ nota.num_tasks || 0 }}</p>
            </div>
            
            <!-- Links -->
            <div v-if="nota.num_links > 0" class="detail flex">
              <i class="fa-solid fa-link fa-sm text-secondary"></i>
              <p class="link-num">{{ nota.num_links }}</p>
            </div>
            
            <!-- Tag -->
            <div v-if="nota.tags" class="detail tag-detail flex">
              <i class="fa-solid fa-tag fa-sm"></i>
              <p class="tag-name">{{ nota.tags }}</p>
            </div>
          </div>
          
          <div class="time flex">
            <div class="detail notebook-details flex">
              <p class="time-detail">{{ nota.time }}</p>
            </div>
            <div class="detail notebook-details flex">
              <i class="fa-solid fa-book fa-sm text-secondary"></i>
              <p class="task-num">{{ nota.notebook }}</p>
            </div>
          </div>
        </div>
      </div>
    </div>
    
    <!-- Imatge: usem has_img per saber si mostrar-la i imageUrl per la URL -->
    <div v-if="nota.has_img && imageUrl" class="img-preview">
      <img :src="imageUrl" :alt="nota.titol">
    </div>
    
    <div class="detail extra-details-top flex w100">
      <p v-if="nota.has_tasks" class="task-num-top">{{ nota.num_tasks || 0 }}</p>
      <p class="time-detail-top">{{ nota.time }}</p>
      <!-- Alarma -->
      <i v-if="nota.has_alarm" class="fa-solid fa-bell fa-sm"></i>
    </div>
  </article>
</template>

<style scoped>
.nota {
  border-bottom: var(--border);
  padding: 1rem;
  cursor: pointer;
}

.nota.active {
  background: var(--color-primary-light);
}

.nota:hover {
  background: #f5f5f5;
}

.text-note {
  flex: 1;
}

.note-title {
  margin: 0 0 0.5rem 0;
  color: var(--color-accent);
}

.note-preview {
  color: var(--color-secondary);
  margin: 0 0 1rem 0;
}

.details-time {
  justify-content: space-between;
  align-items: center;
  font-size: 0.875rem;
}

.details, .time {
  gap: 0.75rem;
}

.detail {
  gap: 0.25rem;
  align-items: center;
}

.img-preview {
  width: 120px;
  height: 120px;
  margin-left: 1rem;
  border-radius: 8px;
  overflow: hidden;
}

.img-preview img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.text-secondary {
  color: var(--color-secondary);
}
</style>