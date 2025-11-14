<script setup>
import MenuBar from './MenuBar.vue';
import MyEditor from './MyEditor.vue';
</script>

<template>
<section id="notepanel">
<MenuBar/>
<MyEditor/>
</section>
    


</template>

<style scoped>
#notepanel {
    grid-area: notepanel;
}
</style>