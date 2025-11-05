<template>
  <div class="grid grid-rows-[1fr_auto] min-h-screen bg-bgdolfidocGray overflow-y-auto">
    <main class="about-page bg-bgdolfidocGray pt-36 pb-16 px-6 md:pt-40 md:pb-20">
      <!-- ===== TÍTULO ===== -->
      <h1 class="font-lato">Sobre a Dolfidoc</h1>

      <!-- ===== INTRO ===== -->
      <p class="about-intro font-lato">
        É inconcebível que, em plena era da informação, ainda seja tão difícil encontrar respostas simples sobre saúde.
        Quem oferece a consulta pneumológica mais acessível na sua cidade? Quais ortopedistas atendem mais perto da sua casa?
        Existe um neuro-oftalmologista no seu município? A falta de informação ainda é uma barreira real — E é exatamente
        isso que a Dolfidoc veio eliminar. Acreditamos que a tecnologia pode transformar a saúde, tornando-a mais acessível
        e humanizada. Por isso, trabalhamos constantemente para oferecer a melhor experiência aos nossos usuários, com
        transparência, segurança e compromisso com a excelência no atendimento.
      </p>

      <!-- ===== CARDS DE VALORES ===== -->
      <section class="about-values">
        <div
          v-for="(card, index) in cards"
          :key="index"
          class="value-card"
          :class="{ flipped: flipped[index] }"
          @click="flipCard(index)"
        >
          <div class="card-inner">
            <!-- Frente -->
            <div class="card-front">
              <h3>{{ card.title }}</h3>
            </div>

            <!-- Verso -->
            <div class="card-back">
              <p>{{ card.description }}</p>
            </div>
          </div>
        </div>
      </section>
    </main>

    <!-- ===== FOOTER ===== -->
    <footer
      class="bg-white text-center py-3 border-t border-gray-300 text-gray-600 text-xs md:text-sm font-lato"
    >
      © 2025 Dolfidoc — Todos os direitos reservados.
    </footer>
  </div>
</template>

<script setup>
import { ref } from 'vue'

const flipped = ref([false, false, false])

const cards = [
  {
    title: 'Missão',
    description:
      'Empoderar a população, revelando a amplitude dos serviços médicos existentes e facilitando o acesso a cuidados especializados de forma rápida, justa e inclusiva.'
  },
  {
    title: 'Visão',
    description:
      'Ser a principal referência nacional de inteligência informacional em saúde, transformando dados públicos em inclusão, equidade e bem-estar social.'
  },
  {
    title: 'Valores',
    description:
      'Transparência: Garantir que as informações sobre serviços médicos sejam acessíveis, verificáveis e apresentadas de forma neutra e imparcial.\n\nÉtica: Utilizar tecnologia e dados de forma ética, respeitando a privacidade e priorizando o interesse público.\n\nSustentabilidade: Promover um modelo digital duradouro, que equilibre eficiência econômica com compromisso social e ambiental.'
  }
]

const flipCard = (index) => {
  flipped.value[index] = !flipped.value[index]
}
</script>

<style scoped>
/* ================== PÁGINA SOBRE ================== */
.about-page {
  padding: 4rem 2rem;
  max-width: 1600px;
  margin: 0 auto;
  text-align: center;
  box-sizing: border-box;
}

.about-page h1 {
  color: var(--color-primary, #2f3061);
  font-size: 2.4rem;
  margin-bottom: 2rem;
  font-weight: 700;
  text-transform: uppercase;
}

.about-intro {
  color: var(--color-text, #333);
  font-size: 1.3rem;
  line-height: 1.6;
  margin-bottom: 3rem;
  max-width: 900px;
  margin-left: auto;
  margin-right: auto;
}

/* ================== FLIP CARDS — MISSÃO / VISÃO / VALORES ================== */
.about-values {
  display: flex;
  justify-content: center;
  align-items: stretch;
  gap: 3rem;
  flex-wrap: wrap;
  margin-top: 2rem;
}

.value-card {
  background: transparent;
  width: 320px;
  min-height: 280px;
  max-height: 420px;
  perspective: 1000px;
  cursor: pointer;
}

.card-inner {
  position: relative;
  width: 100%;
  height: 100%;
  transition: transform 0.8s ease;
  transform-style: preserve-3d;
}

.value-card.flipped .card-inner {
  transform: rotateY(180deg);
}

/* Faces */
.card-front,
.card-back {
  position: absolute;
  width: 100%;
  height: 100%;
  border-radius: 1rem;
  backface-visibility: hidden;
  box-shadow: 0 4px 10px rgba(0, 0, 0, 0.15);
  display: flex;
  justify-content: center;
  align-items: center;
  text-align: center;
  padding: 1.8rem;
  box-sizing: border-box;
}

/* Frente */
.card-front {
  background-color: var(--color-primary, #2f3061);
  color: #fff;
}

.card-front h3 {
  font-size: 1.8rem;
  font-weight: bold;
  letter-spacing: 1px;
  margin: 0;
}

/* Verso */
.card-back {
  background-color: var(--color-white, #fff);
  color: var(--color-text, #333);
  transform: rotateY(180deg);
  display: flex;
  flex-direction: column;
  justify-content: flex-start;
  overflow-y: auto;
  scrollbar-width: thin;
  scrollbar-color: var(--color-primary, #2f3061) #f2f2f2;
}

.card-back::-webkit-scrollbar {
  width: 6px;
}
.card-back::-webkit-scrollbar-thumb {
  background-color: var(--color-primary, #2f3061);
  border-radius: 10px;
}
.card-back::-webkit-scrollbar-track {
  background-color: #f2f2f2;
}

.card-back p {
  font-size: 1rem;
  line-height: 1.6;
  text-align: left;
  margin: 0;
  padding-right: 0.5rem;
  white-space: pre-line;
}

/* Hover visual */
.value-card:hover {
  transform: scale(1.03);
}

/* ===== RESPONSIVIDADE MOBILE ===== */
@media (max-width: 1024px) {
  .about-values {
    flex-direction: column;
    align-items: center;
    gap: 2rem;
  }

  .value-card {
    width: 90%;
    max-width: 360px;
    min-height: 240px;
  }

  .card-front h3 {
    font-size: 1.4rem;
  }

  .card-back p {
    font-size: 0.95rem;
  }
}

@media (max-width: 768px) {
  .about-page {
    padding-top: 7rem; /* evita sobreposição com header */
    padding-bottom: 2rem;
  }

  .about-intro {
    font-size: 1.05rem;
    text-align: justify;
    line-height: 1.5;
  }

  .value-card {
    width: 100%;
    max-width: 340px;
    min-height: 260px;
  }

  .card-front,
  .card-back {
    padding: 2.2rem 1.5rem;
  }

  .card-front h3 {
    font-size: 1.3rem;
  }

  .card-back p {
    font-size: 0.9rem;
  }
}
</style>
