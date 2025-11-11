import { defineConfig } from "eslint/config";
import pluginVue from "eslint-plugin-vue";

export default defineConfig([
  {
    files: ["**/*.{js,vue}"],
  },
  pluginVue.configs["flat/essential"],
]);
