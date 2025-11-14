<script setup>
import { ref, onMounted } from 'vue';
import MyButton from './MyButton.vue';
import FilterBar from './FilterBar.vue';
import MySelectButton from './MySelectButton.vue';
import MyScroller from './MyScroller.vue';




// ref reactiu per guardar les notes
const notes = ref({});

async function fetchNotes() {
  try {
    const res = await fetch("http://localhost:8002/notes");
    const data = await res.json();


    notes.value = data; // guardem les notes tal com venen del backend

  } catch (error) {
    console.error("Error en carregar les notes: ", error);
  }
}

// quan el component es munta, carreguem les notes
onMounted(() => {
  fetchNotes();
});





//VIRTUAL SCROLL 
</script>


<template>
    <section id="note-list">
        <div class="new-note flex">
            <h2>Notes</h2>
            <MyButton bg="white" color="var(--color-primary)" border="var(--border)" width="fit-content"><i
                    class="fa fa-plus fa-sm"></i><span class="create"> Create New</span></MyButton>
        </div>


        <div class="notes-info flex">
            <p><span class="num-notes">0</span> Notes</p>
            <FilterBar />

        </div>
        <MySelectButton />

        <!--al haber un v-model eso indica que el hijo DEBE devolver algo (ya que las props son solo de lectura), en este caso las nnotas actualizadas que se actualizan cada vez que se hace click en la basura-->
       <MyScroller v-model:notes="notes" />
    </section>

</template>


<style scoped>
#note-list {
    grid-area: note-list;
    display: flex;
    flex-direction: column;
    min-width: 0;
    max-width: 100%;
    height: 100%;
    color: black;
    height: 100%;

}


.new-note {
    border-bottom: var(--border);
    padding: 1.5625rem;
    display: flex;
    align-items: center;
    gap: 1.25rem;
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

.notes-info {
    justify-content: space-around;
    font-weight: 600;
    font-size: 0.9375rem;
    border-bottom: var(--border);
    color: var(--color-secondary);
    padding: 0.625rem;
    flex-wrap: wrap;

}

.num-notes {
    color: var(--color-accent);
    font-weight: bold;
}
</style>