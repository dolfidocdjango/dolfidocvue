<template>
  <div class="grid grid-rows-[1fr_auto] min-h-screen bg-bgdolfidocGray pt-32 md:pt-32">
    
    <main>
      
      <div class="grid grid-cols-1 lg:grid-cols-2 h-full">
        
        <section class="flex items-center justify-center p-4 md:p-8 lg:p-12 bg-bgdolfidocGray">
          <div class="w-full max-w-[400px] lg:max-w-[600px] xl:max-w-[800px]">
            <SearchForm />
          </div>
        </section>

        <section
          class="relative hidden lg:flex flex-col items-center justify-end overflow-hidden bg-bgdolfidocGray
                 px-4 md:px-6 lg:px-8 pt-4 md:pt-6 lg:pt-8 pb-0"
        >
          <p
            class="text-white text-3xl xl:text-5xl font-semibold text-center mb-4 z-10 drop-shadow-lg font-lato leading-tight tracking-tight"
          >
            Todas as consultas<br />
            <span class="text-white text-3xl xl:text-5xl font-semibold block mt-2">
              médicas em um único lugar.
            </span>
          </p>
          <img
            src="@/assets/images/doctors.png"
            alt="Equipe médica Dolfidoc"
            class="w-full max-w-[550px] h-auto object-contain z-10 mb-0"
          />
        </section>

      </div>
    </main>

    <footer
      class="bg-white text-center py-4 border-t border-gray-300 text-gray-600 text-sm font-lato"
    >
      © 2025 Dolfidoc — Todos os direitos reservados.
    </footer>
  </div>
</template>

<script setup>
import SearchForm from '@/components/SearchForm.vue'
</script>