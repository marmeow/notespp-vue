import { createApp } from "vue";
import PrimeVue from "primevue/config";
import Aura from "@primeuix/themes/aura";
import App from "./App.vue";
import { createPinia } from "pinia";

import "bootstrap-icons/font/bootstrap-icons.css";
import "primeicons/primeicons.css";
import "@fortawesome/fontawesome-free/css/all.css";

import ToastService from "primevue/toastservice";

const app = createApp(App);

app.use(createPinia());   // Pinia
app.use(PrimeVue, {       // PrimeVue con tema
  theme: {
    preset: Aura,
  },
});
app.use(ToastService);    // ToastService

app.mount("#app");        // montar la misma instancia
