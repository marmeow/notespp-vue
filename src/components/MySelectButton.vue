<script setup>
import SelectButton from 'primevue/selectbutton';
import { ref } from 'vue';

const value = ref('All');
const options = ref(['All', 'Reminder']);


</script>

<template>
    <div class="card flex justify-center">
        <SelectButton v-model="value" :options="options" :allow-empty="false" fluid />
    </div>
</template>

<style scoped>
:root {
    --p-selectbutton-border-radius: 0px;
}

:deep(.p-selectbutton) {
    background: transparent !important;
    border: none !important;
    border-bottom: var(--border) !important;
    border-radius: 0px;

}

:deep(.p-selectbutton .p-togglebutton) {
    background: transparent !important;
    border: none !important;
    box-shadow: none;
    color: var(--color-secondary);
}

:deep(.p-togglebutton.p-component.p-togglebutton-checked) {
    background: transparent !important;
    border-bottom: 3px solid var(--color-primary) !important;
    color: var(--color-primary) !important;
    font-weight: 600;
        border-radius: 0px;
}

:deep(.p-togglebutton-checked .p-togglebutton-content) {
    background: transparent !important;
        box-shadow: none !important;
}
</style>
