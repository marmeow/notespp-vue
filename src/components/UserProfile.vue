<script setup>
import { ref, onMounted, onUnmounted } from "vue";
// Importamos funciones de Vue para crear variables reactivas y manejar el ciclo de vida del componente

import Avatar from "primevue/avatar";
import OverlayBadge from "primevue/overlaybadge";
// Componentes de PrimeVue: Avatar para la foto de perfil y OverlayBadge para mostrar un indicador encima

import MyDropdown from "./MyDropdown.vue";
// Importamos nuestro componente personalizado de menú desplegable


// Variable reactiva que indica si la pantalla es "móvil" (≤1080px)
const isLaptop = ref(window.innerWidth <= 1080);

// Función que actualiza la variable cuando cambia el tamaño de la ventana
function handleResize() {
  isLaptop.value = window.innerWidth <= 1080;
}

// Al montar el componente, añadimos el listener de resize
onMounted(() => window.addEventListener("resize", handleResize));
// Al desmontar el componente, quitamos el listener para evitar fugas de memoria
onUnmounted(() => window.removeEventListener("resize", handleResize));
</script>

<template>
  <div class="user-profile flex">
    <!-- Foto de perfil con badge de estado -->
    <div class="profile-picture">
      <OverlayBadge severity="success" class="inline-flex custom-badge">
        <Avatar label="EH" class="mr-2" size="large" style="background-color: #D6AF15; color: #fff" shape="circle" />
      </OverlayBadge>
    </div>

    <!-- Información del usuario -->
    <div class="user-name">
      <p class="name">Esther Howard</p>
      <p>estherH@gmail.com</p>
    </div>

    <!-- Condicional: si es móvil, se muestra el dropdown -->
    <MyDropdown v-if="isLaptop" />

    <!-- Si NO es móvil, se muestra solo el icono caret -->
    <i v-else class="fa-solid fa-caret-down text-secondary"></i>
  </div>
  <!-- Nota: el dropdown solo aparece en pantallas pequeñas -->
</template>

<style scoped>
.user-profile {
  border-left: var(--border);
  padding: 0 1rem;
  height: 100%;
}

/* Ajustes al badge del avatar */
:deep(.custom-badge .p-badge) {
  transform: none;
  outline-color: white;
}

/* Estilos de la información del usuario */
.user-name {
  color: var(--color-secondary);
  font-size: 0.925rem;
  margin: 0 0.625rem;
}

.name {
  font-weight: bold;
  color: var(--color-accent);
  font-size: 1rem;
}

/* Color del icono caret */
.fa-caret-down {
  color: var(--color-secondary);
}

@media (max-width: 480px) {
  .user-name {
    display: none;

  }

  .user-profile {
    padding: 0.75rem;
  }
}
</style>
