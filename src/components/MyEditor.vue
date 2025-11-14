<script setup>

import Checkbox from 'primevue/checkbox';
import CheckboxGroup from 'primevue/checkboxgroup';

import Editor from 'primevue/editor';

import { ref } from "vue";

const value = ref('');






/// https://codepen.io/djones4822/pen/NWeEBab
//https://github.com/koffeinfrei/quill-task-list

</script>



<template>
    <div class="card">
      <Editor v-model="noteContent" :modules="editorModules">
        <template>
            <Checkbox v-model="checked" binary />
        </template>
    </Editor>
    </div>
</template>

