<script setup>
import Image from 'primevue/image'
import { computed } from 'vue'
import { useNoteStore } from '../stores/NoteStore'

const noteStore = useNoteStore()

const props = defineProps({
  noteId: { type: String, required: true },
  titol: String,
  contingut: String,
  images: Array,
  hasTasks: Boolean,
  tasksId: Array,
  numLinks: Number,
  tags: Array,
  time: String,
  notebook: String,
  hasAlarm: Boolean,
  isShared: Boolean
})


const isActive = computed(() => noteStore.selectedNoteId === props.noteId)


const imageUrl = computed(() => {
  if (props.images && props.images.length > 0) {
    return `/images/${props.images[0]}`
  }
  return null
})
</script>


<template>
  <article @click="noteStore.selectNote(noteId)"  class="nota" :data-id="noteId" :class="{ active: isActive, 'hasimg': imageUrl, 'noimg': !imageUrl }" >
    <div class="text-note">
      <div class="inner">
        <h3 class="note-title">{{ titol }}</h3>
        <p class="note-preview">{{ contingut?.slice(0, 70) }}.</p>

        <div class="details">
          <div class="info-note flex">
            <div v-if="hasTasks" class="detail flex">
              <i class="fa-solid fa-list-check fa-sm text-secondary"></i>
              <p class="task-num">0/{{ tasksId.length }}</p>
            </div>

            <div v-if="numLinks > 0" class="detail flex">
              <i class="fa-solid fa-link fa-sm text-secondary"></i>
              <p class="link-num">{{ numLinks }}</p>
            </div>

            <div v-if="tags" class="detail tag-detail flex" :class="tags[0].toLowerCase()">
              <i class="fa-solid fa-tag fa-sm"></i>
              <p class="tag-name">{{ tags[0] }}</p>
            </div>
            <p v-if="tags && tags.length > 1" class="tag-amount">
              + <span class="tag-num">{{ tags.length }}</span>
            </p>
          </div>

          <div class="time-note flex">
            <div class="detail notebook-details flex">
              <p class="time-detail">{{ time }}</p>
            </div>
            <div class="detail notebook-details flex">
              <i class="fa-solid fa-book fa-sm text-secondary"></i>
              <p class="task-num">{{ notebook }}</p>
            </div>

            <div class="detail extra-details flex">
              <i v-if="isShared" class="fa-solid fa-users fa-sm text-primary"></i>
              <i v-if="hasAlarm" class="fa-solid fa-alarm-clock fa-sm text-primary"></i>
            </div>
          </div>
        </div>
      </div>
    </div>

    <div class="img-preview">
      <Image class="image" v-if="imageUrl" :src="imageUrl" :alt="titol" preview />
    </div>

    <div class="detail extra-details-bottom flex w100">
      <p v-if="hasTasks" class="task-num-bottom">{{ numTasks || 0 }}</p>
      <p class="time-detail-bottom">{{ time }}</p>
      <i v-if="hasAlarm" class="fa-solid fa-bell fa-sm"></i>
    </div>

    <i class="pi pi-trash delete-task" @click="noteStore.deleteNote(noteId)"></i>
  </article>
</template>



<style scoped>

.nota:not(.active):hover  {
  background-color: var(--color-bg-light);
  cursor: pointer;
}

.active {
  background-color: #2e84ed22;
  border-left: 3px solid var(--color-primary) !important;
}

.flex {
  flex-wrap: wrap;
}

.note-title,
.note-preview {
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
  max-width: 100%;
}

.note-title {
  color: var(--color-accent);
  font-size: 1.15625rem;
  margin: 0px 0px 0.625rem 0px;
}

.note-preview {
  color: var(--color-secondary);
  font-size: 1.09375rem;
}

article.hasimg {
  width: 100%;
  display: grid;
  grid-template-columns: 70% 30%;
  padding: 0px 10px;
}

.p-image {
  width: 100px;
  height: 100px;
  object-fit: cover;

}

:deep(img) {
  border-radius: var(--btn-radius);
}

.inner,
.img-preview {
  padding: 10px;
}

.img-preview {
  display: flex;
  justify-content: flex-end;
}

.inner-noimg {
  width: 100%;
}

.inner-img {
  width: 100%;
}



.details,
.time {
  flex-wrap: wrap;
}

.detail {
  margin: 0.5rem 1rem 0.3125rem 0;
}

.detail p {
  font-size: 0.96875rem;
  color: #575757;
  margin-left: 0.3125rem;
}

.tag-detail {
  padding: 0.25rem 0.5rem;
  border-radius: 0.9375rem;
  
}

p.time-detail {
  margin-left: 0px;
}

.extra-details .fa-sm {
  margin-right: 0.625rem;
}




.delete-task {
  margin: 5px;
}


.extra-details-bottom {
  display: none;
}
</style>