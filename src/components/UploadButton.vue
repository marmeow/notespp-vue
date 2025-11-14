<script setup>
import { ref } from 'vue';
import { useToast } from "primevue/usetoast";
import Toast from "primevue/toast";
import FileUpload from "primevue/fileupload";
import MyButton from './MyButton.vue';

const toast = useToast();
const fileUploadRef = ref(null);

const onUpload = () => {
  toast.add({
    severity: "info",
    summary: "Success",
    detail: "File Uploaded",
    life: 3000
  });
};

const triggerFileSelect = () => {
  fileUploadRef.value.$el.querySelector('input[type="file"]').click();
};
</script>

<template>
  <div>
    <Toast />
    
    <!-- Tu botón personalizado -->
    <MyButton @click="triggerFileSelect">
      <i class="fa-solid fa-arrow-up-from-bracket"></i>
      <slot>Upload</slot>
    </MyButton>
    

    <FileUpload
      ref="fileUploadRef"
      mode="basic"
      name="demo[]"
      url="/api/upload"
      accept="text/*"
      :maxFileSize="1000000"
      @upload="onUpload"
      :auto="true"
      style="display: none;"
    />
  </div>
</template>
<style scoped></style>




