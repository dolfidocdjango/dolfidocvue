// tailwind.config.js
/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{vue,js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      // === INÍCIO DA MAGIA ===
      screens: {
        /**
         * Adiciona um breakpoint 'short' (baixo).
         * Ativado em viewports com 800px de altura ou MENOS.
         * Perfeito para 1366x768.
         */
        'short': { 'raw': '(max-height: 800px)' },
      },
      // === FIM DA MAGIA ===

      colors: {
        'dolfidocBlue': "#2f3061",
        'dolfidocGray': "#D3DAE0",
        'bgdolfidocGray': "#D3DAE0",
        'primary': '#2f3061',
        'bg': '#D3DAE0',
        'text': '#333',
        'text-light': '#767575',
        'placeholder': '#d0d0d0',
        'error': '#dc3545',
        'hover': '#0056b3',
      },
      fontFamily: {
        inter: ['Inter', 'sans-serif'],
        lato: ['Lato', 'sans-serif'],
      },
      zIndex: {
        '1000': '1000',
      },
      maxWidth: {
        '320px': '320px',
      }
    },
  },
  plugins: [],
}