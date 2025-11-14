<script setup>


import Image from 'primevue/image';
import { ref, computed } from 'vue';



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




const emit= defineEmits(['onDeleteClicked'])
const handleDeleteClick = () => {
  emit('onDeleteClicked', props.noteId)
}



const hidden = ref(false);



const imageUrl = computed(() => {

  if (props.nota.images && props.nota.images.length > 0) {
    const imageName = props.nota.images[0];
    const url = `/images/${imageName}`;
    return url;
  }
  return null;
});

console.log('Nota:', props.nota);
console.log('Alarm:', props.nota.has_alarm);
console.log('Has imatge:', props.nota.has_img);
console.log('Imagtes array:', props.nota.images);
console.log('Image URL:', imageUrl.value);
</script>

<template>


  <article class="notas" :data-id="noteId" :class="{ active: nota.isActive, 'hasimg': imageUrl, 'noimg': !imageUrl }"
    v-if="!hidden">
    <div class="text-note">
      <div class="inner">
        <i class="pi pi-trash delete-task" @click.prevent="handleDeleteClick"></i>
        <h3 class="note-title">{{ nota.titol }}</h3>
        <p class="note-preview">{{ nota.contingut.slice(0, 70) }}.</p>

        <div class="details flex">
          <div class="info-note flex">

            <div v-if="nota.has_tasks" class="detail flex">
              <i class="fa-solid fa-list-check fa-sm text-secondary"></i>
              <p class="task-num">{{ nota.num_tasks || 0 }}</p>
            </div>


            <div v-if="nota.num_links > 0" class="detail flex">
              <i class="fa-solid fa-link fa-sm text-secondary"></i>
              <p class="link-num">{{ nota.num_links }}</p>
            </div>


            <div v-if="nota.tags" class="detail tag-detail flex">
              <i class="fa-solid fa-tag fa-sm"></i>
              <p class="tag-name">{{ nota.tags }}</p>
            </div>
          </div>

          <div class="time-note flex">
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

    <div class="img-preview">
      <Image class="image" v-if="imageUrl" :src="imageUrl" :alt="nota.titol" preview />
    </div>

    <div class="detail extra-details-bottom flex w100">
      <p v-if="nota.has_tasks" class="task-num-bottom">{{ nota.num_tasks || 0 }}</p>
      <p class="time-detail-bottom">{{ nota.time }}</p>

      <i v-if="nota.has_alarm" class="fa-solid fa-bell fa-sm"></i>
    </div>
  </article>
</template>


<style scoped>
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



.details p {
  margin: 5px;
}

article.hasimg {
  width: 100%;
  display: grid;
  grid-template-columns: 70% 30%;
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
}

.delete-task {
  margin: 5px;
}

.inner-noimg {
  width: 100%;
}

.inner-img {
  width: 100%;
}


.extra-details-bottom {
  display: none;
}


</style>