<template>
  <section class="flex flex-col items-center justify-center min-h-[70vh] text-center px-6">
    <h2 class="text-4xl font-bold text-dolfidoc-blue mb-4">Fale Conosco</h2>
    <p class="max-w-xl text-gray-700 mb-6">
      Envie sua mensagem e entraremos em contato o mais breve possível.
    </p>

    <form class="flex flex-col gap-4 w-full max-w-md">
      <input type="text" placeholder="Seu nome" class="p-3 border rounded-md border-gray-300 focus:outline-none focus:border-dolfidoc-blue" />
      <input type="email" placeholder="Seu e-mail" class="p-3 border rounded-md border-gray-300 focus:outline-none focus:border-dolfidoc-blue" />
      <textarea placeholder="Sua mensagem" class="p-3 border rounded-md border-gray-300 focus:outline-none focus:border-dolfidoc-blue"></textarea>
      <button type="submit" class="dolfidoc-blue text-white py-3 rounded-md hover:bg-blue-700 transition-all">Enviar</button>
    </form>
  </section>
</template>
