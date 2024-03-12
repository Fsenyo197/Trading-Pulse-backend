import { defineConfig } from "vite";
import react from "@vitejs/plugin-react";
import tailwindcss from "tailwindcss";

export default defineConfig({
  plugins: [react(), tailwindcss("./tailwind.config.js")],
  server: {
    port: 3000,
  },
  resolve: {
    alias: {
      "@Images": "/src/Images",
    },
  },
});
