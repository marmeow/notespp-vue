<script setup>
defineProps({
  bg: { type: String, default: "#0859bc" },
  color: { type: String, default: "white" },
  border: { type: String, default: "none" },
  width: { type: String, default: "100%" }
});
</script>

<template>
  <button
    :style="{
      backgroundColor: bg,
      color: color,
      border: border,
      width: width
    }"
  >
    <slot />
  </button>
</template>

<style scoped>
button {
  cursor: pointer;
  font-size: 1rem;
  padding: var(--btn-padding);
  border-radius: var(--btn-radius);
  font-weight: 600;
}
button:hover {
  background-color: #0859bc6a !important;
  color: var(--color-accent) !important;
}
</style>
