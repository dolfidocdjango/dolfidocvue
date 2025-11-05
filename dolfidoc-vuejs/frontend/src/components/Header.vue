<template>
  <header 
    class="fixed top-0 left-0 right-0 z-[9999] bg-bgdolfidocGray 
           flex flex-col md:flex-row items-center justify-between 
           h-auto md:h-[120px] 
           px-4 sm:px-8 
           py-3 md:py-0
           transition-all duration-300 ease-in-out" 
    :class="{ 
      'opacity-0 -translate-y-full pointer-events-none': isScrolled 
    }"
  >
    <div class="flex-shrink-0 flex items-center justify-center md:justify-start w-full md:w-auto mb-2 md:mb-0">
      <RouterLink to="/" class="h-[60px] md:h-[90px] flex items-center">
        <img
          :src="logoImage"
          alt="Dolfidoc Logo"
          class="h-full w-auto object-contain"
        />
      </RouterLink>
    </div>

    <nav
      class="flex flex-row items-center justify-center gap-5 md:gap-10
             w-full md:w-auto text-center 
             md:text-right md:pr-20 lg:pr-32 xl:pr-44 2xl:pr-65"
    >
      <RouterLink
        v-for="link in navLinks"
        :key="link.path"
        :to="link.path"
        class="relative 
               text-base md:text-[1.5rem] xl:text-[1.7rem]
               font-semibold text-dolfidocBlue transition-all duration-300
               hover:text-blue-900 whitespace-nowrap
               after:content-[''] after:absolute after:left-0 after:bottom-0 after:w-0 after:h-[2px]
               after:bg-dolfidocBlue after:transition-all after:duration-300 hover:after:w-full"
      >
        {{ link.label }}
      </RouterLink>
    </nav>
  </header>
</template>

<script setup>
// 1. IMPORTAR OS FEITIÇOS REATIVOS
import { ref, onMounted, onUnmounted } from 'vue'
import { RouterLink } from 'vue-router'
import logoImage from '@/assets/images/logo_hd.png'

// --- INÍCIO DA MAGIA DE SCROLL ---

// 2. O ESTADO REATIVO
// 'false' significa "não rolado" (visível)
const isScrolled = ref(false)

// O limite em pixels antes de esconder o header
const SCROLL_THRESHOLD = 50 // 50 pixels

// 3. O FEITIÇO OBSERVADOR
const handleScroll = () => {
  // Se o scroll passar do nosso limite
  if (window.scrollY > SCROLL_THRESHOLD) {
    isScrolled.value = true // Esconda o header
  } else {
    isScrolled.value = false // Mostre o header
  }
}

// 4. ATIVAR O FEITIÇO NO CICLO DE VIDA
onMounted(() => {
  // Começa a ouvir o scroll quando o componente é montado
  window.addEventListener('scroll', handleScroll)
})

onUnmounted(() => {
  // Para de ouvir (limpa a magia) quando o componente é destruído
  // Isso é crucial para evitar memory leaks!
  window.removeEventListener('scroll', handleScroll)
})

// --- FIM DA MAGIA DE SCROLL ---

const navLinks = [
  { path: '/', label: 'Cadastro' },
  { path: '/sobre', label: 'Sobre' },
  { path: '/contato', label: 'Contato' }
]
</script>

<style scoped>
/* Seu <style scoped> permanece o mesmo */
header {
  box-shadow: none !important;
}

nav a::after {
  border-radius: 2px;
}

nav a:active {
  transform: scale(0.97);
}
</style>