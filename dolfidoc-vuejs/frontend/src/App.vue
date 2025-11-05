<template>
  <div>
    <Header />
    <RouterView />
  </div>
</template>

<script setup>
import Header from '@/components/Header.vue'
</script>

<style>
/* ... seus estilos globais de html, body ... */

/* 1. O FEITIÇO DE "NÃO ROLAR" (Permanece para Desktop) */
body {
  overflow-y: hidden !important; 
}

/* 2. O FEITIÇO DE "ENCOLHIMENTO (ZOOM) PARA HD" (Permanece) */
@media (min-width: 1300px) and (max-width: 1400px) and (max-height: 800px) {
  html {
    zoom: 0.86; /* O seu valor de 86% */
  }
  header nav {
    padding-right: 6rem !important;
  }
}

/* === INÍCIO DA MAGIA MOBILE (RECOMENDADA) ===
   Isto define que em telas com 767px de largura ou MENOS (móvel),
   nós permitimos a rolagem.
*/
@media (max-width: 767px) {
  body {
    overflow-y: auto !important; /* PERMITE O SCROLL NO CELULAR */
  }

  html {
    zoom: 1; /* Garante que não haja zoom */
  }
}
</style>