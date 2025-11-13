<script setup>
import Select from 'primevue/select';
import { ref } from "vue";

const selectedOption = ref();
const sortOptions = ref([
    { name: 'Newest first' },
    { name: 'Oldest first' },
]);
</script>

<template>
    <div class="card flex justify-center">
        <p>Date created: </p>
        <Select v-model="selectedOption" :options="sortOptions" optionLabel="name" placeholder="Newest first" class="w-full md:w-56">
            <template #value="slotProps">
                <div v-if="slotProps.value" class="flex items-center">
                    <div>{{ slotProps.value.name }}</div>
                </div>
                <span v-else>
                    {{ slotProps.placeholder }}
                </span>
            </template>
            <template #option="slotProps">
                <div class="flex items-center">
                    <div>{{ slotProps.option.name }}</div>
                </div>
            </template>
            <template #dropdownicon>
                <i class="pi pi-sort" />
            </template>
        </Select>
        <i class="pi pi-filter"></i>
    </div>
</template>


<style scoped>
.p-select {
    background-color: transparent;
    border: none;
    box-shadow: none;
}


:deep( .p-select-label ) {
  color: var(--color-accent)!important;
}


.p-select-label.p-placeholder span {
        color: var(--color-accent);
}
</style>