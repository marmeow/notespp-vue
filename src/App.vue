<script setup>
import MyHeader from "./components/MyHeader.vue";
import FirstSidebar from "./components/FirstSidebar.vue";
import SecondSidebar from "./components/SecondSidebar.vue";
import NoteList from "./components/NoteList.vue";
</script>

<template>
  <div id="grid">


    <MyHeader />
    <FirstSidebar />
    <SecondSidebar />
    <NoteList/>
    <div class="notepanel">
      <p>AAAAAeowef</p>
    </div>
  </div>
</template>

<style scoped>
#grid {
  height: 100%;
  display: grid;
    grid-template-columns: 70px 250px 450px auto;
    grid-template-rows: 70px auto;
  grid-template-areas:
    "first-sidebar header header header"
    "first-sidebar second-sidebar note-list notepanel";
}


.notelist {
  grid-area: notelist;
}


.notepanel {
  grid-area: notepanel;
}
</style>
