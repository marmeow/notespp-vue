<script setup>
import { ref } from "vue";
// Importamos la función ref de Vue para crear variables reactivas

import Menu from "primevue/menu";
import Button from "primevue/button";
// Importamos los componentes de PrimeVue: Menu (menú desplegable) y Button (botón)

const menu = ref();
// Creamos una referencia al menú. Esto nos permite acceder a sus métodos (abrir/cerrar)

const items = [
  // Definimos los ítems que aparecerán dentro del menú
  { label: "Tasques", icon: "fa-solid fa-clipboard-check" },
  { label: "Notificacions", icon: "fa-solid fa-bell" },
];

function toggleMenu(event) {
  // Función que abre o cierra el menú cuando se hace clic en el botón
  menu.value.toggle(event);
}
</script>

<template>
  <div class="card flex justify-content-end">
    <!-- Botón que dispara la apertura/cierre del menú, Al hacer clic, ejecuta toggleMenu, Estilo: bordes redondeados, Estilo: botón sin fondo, solo texto/icono,  Icono caret de FontAwesome-->
    <Button
      aria-label="Obrir menú usuari"
      @click="toggleMenu"
      rounded
      text
      icon="fa-solid fa-caret-down text-secondary"
    />

    <!-- Menú desplegable en modo popup -->
    <Menu ref="menu" :model="items" :popup="true">
      <!-- Slot para personalizar cómo se renderiza cada ítem -->
      <template #item="{ item }">
        <a class="p-menuitem-link">
          <!-- Icono del ítem -->
          <i :class="item.icon" class="p-menuitem-icon text-secondary"></i>
          <!-- Texto del ítem -->
          <span class="p-menuitem-text">{{ item.label }}</span>
        </a>
      </template>
    </Menu>
  </div>
</template>

<style scoped>
.p-menu {
  min-width: 160px; /* El menú tendrá un ancho mínimo de 160px */
}

/* Estilos para el botón en estado normal, hover y focus */
.p-button-text:not(:disabled):hover,
.p-button-text:not(:disabled):focus,
.p-button-text {
  color: var(--color-secondary); /* Color secundario definido en tu tema */
}
</style>
